import collections
from collections import OrderedDict
import re
import warnings
from contextlib import contextmanager
from copy import deepcopy, copy
import itertools
from functools import reduce

from _plotly_utils.utils import (
    _natural_sort_strings,
    _get_int_type,
    split_multichar,
    split_string_positions,
    display_string_positions,
    chomp_empty_strings,
    find_closest_string,
    convert_to_base64,
)
from _plotly_utils.exceptions import PlotlyKeyError
from .optional_imports import get_module

from . import shapeannotation
from . import _subplots

# Create Undefined sentinel value
#   - Setting a property to None removes any existing value
#   - Setting a property to Undefined leaves existing value unmodified
Undefined = object()


def _len_dict_item(item):
    """
    Because a parsed dict path is a tuple containings strings or integers, to
    know the length of the resulting string when printing we might need to
    convert to a string before calling len on it.
    """
    try:
        temp = len(item)
    except TypeError:
        try:
            temp = len("%d" % (item,))
        except TypeError:
            raise ValueError(
                "Cannot find string length of an item that is not string-like nor an integer."
            )
    return temp


def _str_to_dict_path_full(key_path_str):
    """
    Convert a key path string into a tuple of key path elements and also
    return a tuple of indices marking the beginning of each element in the
    string.

    Parameters
    ----------
    key_path_str : str
        Key path string, where nested keys are joined on '.' characters
        and array indexes are specified using brackets
        (e.g. 'foo.bar[1]')
    Returns
    -------
    tuple[str | int]
    tuple [int]
    """
    # skip all the parsing if the string is empty
    if len(key_path_str):
        # split string on ".[]" and filter out empty strings
        key_path2 = split_multichar([key_path_str], list(".[]"))
        # Split out underscore
        # e.g. ['foo', 'bar_baz', '1'] -> ['foo', 'bar', 'baz', '1']
        key_path3 = []
        underscore_props = BaseFigure._valid_underscore_properties



        key_path2b = list(map(_make_hyphen_key, key_path2))

        # Here we want to split up each non-empty string in the list at
        # underscores and recombine the strings using chomp_empty_strings so
        # that leading, trailing and multiple _ will be preserved

        # after running _split_and_chomp on key_path2b, it will be a list
        # containing strings and lists of strings; concatenate the sublists with
        # the list ("lift" the items out of the sublists)
        key_path2c = list(
            reduce(
                lambda x, y: x + y if isinstance(y, list) else x + [y],
                map(_split_and_chomp, key_path2b),
                [],
            )
        )

        key_path2d = list(map(_make_underscore_key, key_path2c))
        all_elem_idcs = tuple(split_string_positions(list(key_path2d)))
        # remove empty strings, and indices pointing to them
        key_elem_pairs = list(filter(lambda t: len(t[1]), enumerate(key_path2d)))
        key_path3 = [x for _, x in key_elem_pairs]
        elem_idcs = [all_elem_idcs[i] for i, _ in key_elem_pairs]

        # Convert elements to ints if possible.
        # e.g. ['foo', 'bar', '0'] -> ['foo', 'bar', 0]
        for i in range(len(key_path3)):
            try:
                key_path3[i] = int(key_path3[i])
            except ValueError as _:
                pass
    else:
        key_path3 = []
        elem_idcs = []

    return (tuple(key_path3), elem_idcs)


def _remake_path_from_tuple(props):
    """
    try to remake a path using the properties in props
    """
    if len(props) == 0:
        return ""



    props_all_str = list(map(_add_square_brackets_to_number, props))
    props_w_underscore = props_all_str[:1] + list(
        map(_prepend_dot_if_not_number, props_all_str[1:])
    )
    return "".join(props_w_underscore)


def _check_path_in_prop_tree(obj, path, error_cast=None):
    """
    obj:        the object in which the first property is looked up
    path:       the path that will be split into properties to be looked up
                path can also be a tuple. In this case, it is combined using .
                and [] because it is impossible to reconstruct the string fully
                in order to give a decent error message.
    error_cast: this function walks down the property tree by looking up values
                in objects. So this will throw exceptions that are thrown by
                __getitem__, but in some cases we are checking the path for a
                different reason and would prefer throwing a more relevant
                exception (e.g., __getitem__ throws KeyError but __setitem__
                throws ValueError for subclasses of BasePlotlyType and
                BaseFigure). So the resulting error can be "casted" to the
                passed in type, if not None.
    returns
          an Exception object or None. The caller can raise this
          exception to see where the lookup error occurred.
    """
    if isinstance(path, tuple):
        path = _remake_path_from_tuple(path)
    prop, prop_idcs = _str_to_dict_path_full(path)
    prev_objs = []
    for i, p in enumerate(prop):
        arg = ""
        prev_objs.append(obj)
        try:
            obj = obj[p]
        except (ValueError, KeyError, IndexError, TypeError) as e:
            arg = e.args[0]
            if issubclass(e.__class__, TypeError):
                # If obj doesn't support subscripting, state that and show the
                # (valid) property that gives the object that doesn't support
                # subscripting.
                if i > 0:
                    validator = prev_objs[i - 1]._get_validator(prop[i - 1])
                    arg += """

Invalid value received for the '{plotly_name}' property of {parent_name}

{description}""".format(
                        parent_name=validator.parent_name,
                        plotly_name=validator.plotly_name,
                        description=validator.description(),
                    )
                # In case i is 0, the best we can do is indicate the first
                # property in the string as having caused the error
                disp_i = max(i - 1, 0)
                dict_item_len = _len_dict_item(prop[disp_i])
                # if the path has trailing underscores, the prop string will start with "_"
                trailing_underscores = ""
                if prop[i][0] == "_":
                    trailing_underscores = " and path has trailing underscores"
                # if the path has trailing underscores and the display index is
                # one less than the prop index (see above), then we can also
                # indicate the offending underscores
                if (trailing_underscores != "") and (disp_i != i):
                    dict_item_len += _len_dict_item(prop[i])
                arg += """

Property does not support subscripting%s:
%s
%s""" % (
                    trailing_underscores,
                    path,
                    display_string_positions(
                        prop_idcs, disp_i, length=dict_item_len, char="^"
                    ),
                )
            else:
                # State that the property for which subscripting was attempted
                # is bad and indicate the start of the bad property.
                arg += """
Bad property path:
%s
%s""" % (
                    path,
                    display_string_positions(
                        prop_idcs, i, length=_len_dict_item(prop[i]), char="^"
                    ),
                )
            # Make KeyError more pretty by changing it to a PlotlyKeyError,
            # because the Python interpreter has a special way of printing
            # KeyError
            if isinstance(e, KeyError):
                e = PlotlyKeyError()
            if error_cast is not None:
                e = error_cast()
            e.args = (arg,)
            return e
    return None




def _indexing_combinations(dims, alls, product=False):
    """
    Gives indexing tuples specified by the coordinates in dims.
    If a member of dims is 'all' then it is replaced by the corresponding member
    in alls.
    If product is True, then the cartesian product of all the indices is
    returned, otherwise the zip (that means index lists of mis-matched length
    will yield a list of tuples whose length is the length of the shortest
    list).
    """
    if len(dims) == 0:
        # this is because list(itertools.product(*[])) returns [()] which has non-zero
        # length!
        return []
    if len(dims) != len(alls):
        raise ValueError(
            "Must have corresponding values in alls for each value of dims. Got dims=%s and alls=%s."
            % (str(dims), str(alls))
        )
    r = []
    for d, a in zip(dims, alls):
        if d == "all":
            d = a
        elif not isinstance(d, list):
            d = [d]
        r.append(d)
    if product:
        return itertools.product(*r)
    else:
        return zip(*r)


def _is_select_subplot_coordinates_arg(*args):
    """Returns true if any args are lists or the string 'all'"""
    return any((a == "all") or isinstance(a, list) for a in args)


def _axis_spanning_shapes_docstr(shape_type):
    docstr = ""
    if shape_type == "hline":
        docstr = """
Add a horizontal line to a plot or subplot that extends infinitely in the
x-dimension.

Parameters
----------
y: float or int
    A number representing the y coordinate of the horizontal line."""
    elif shape_type == "vline":
        docstr = """
Add a vertical line to a plot or subplot that extends infinitely in the
y-dimension.

Parameters
----------
x: float or int
    A number representing the x coordinate of the vertical line."""
    elif shape_type == "hrect":
        docstr = """
Add a rectangle to a plot or subplot that extends infinitely in the
x-dimension.

Parameters
----------
y0: float or int
    A number representing the y coordinate of one side of the rectangle.
y1: float or int
    A number representing the y coordinate of the other side of the rectangle."""
    elif shape_type == "vrect":
        docstr = """
Add a rectangle to a plot or subplot that extends infinitely in the
y-dimension.

Parameters
----------
x0: float or int
    A number representing the x coordinate of one side of the rectangle.
x1: float or int
    A number representing the x coordinate of the other side of the rectangle."""
    docstr += """
exclude_empty_subplots: Boolean
    If True (default) do not place the shape on subplots that have no data
    plotted on them.
row: None, int or 'all'
    Subplot row for shape indexed starting at 1. If 'all', addresses all rows in
    the specified column(s). If both row and col are None, addresses the
    first subplot if subplots exist, or the only plot. By default is "all".
col: None, int or 'all'
    Subplot column for shape indexed starting at 1. If 'all', addresses all rows in
    the specified column(s). If both row and col are None, addresses the
    first subplot if subplots exist, or the only plot. By default is "all".
annotation: dict or plotly.graph_objects.layout.Annotation. If dict(),
    it is interpreted as describing an annotation. The annotation is
    placed relative to the shape based on annotation_position (see
    below) unless its x or y value has been specified for the annotation
    passed here. xref and yref are always the same as for the added
    shape and cannot be overridden."""
    if shape_type in ["hline", "vline"]:
        docstr += """
annotation_position: a string containing optionally ["top", "bottom"]
    and ["left", "right"] specifying where the text should be anchored
    to on the line. Example positions are "bottom left", "right top",
    "right", "bottom". If an annotation is added but annotation_position is
    not specified, this defaults to "top right"."""
    elif shape_type in ["hrect", "vrect"]:
        docstr += """
annotation_position: a string containing optionally ["inside", "outside"], ["top", "bottom"]
    and ["left", "right"] specifying where the text should be anchored
    to on the rectangle. Example positions are "outside top left", "inside
    bottom", "right", "inside left", "inside" ("outside" is not supported). If
    an annotation is added but annotation_position is not specified this
    defaults to "inside top right"."""
    docstr += """
annotation_*: any parameters to go.layout.Annotation can be passed as
    keywords by prefixing them with "annotation_". For example, to specify the
    annotation text "example" you can pass annotation_text="example" as a
    keyword argument.
**kwargs:
    Any named function parameters that can be passed to 'add_shape',
    except for x0, x1, y0, y1 or type."""
    return docstr


def _generator(i):
    """ "cast" an iterator to a generator"""
    for x in i:
        yield x


def _set_property_provided_value(obj, name, arg, provided):
    """
    Initialize a property of this object using the provided value
    or a value popped from the arguments dictionary. If neither
    is available, do not set the property.
    """
    pass


class BaseFigure(object):
    """
    Base class for all figure types (both widget and non-widget)
    """

    _bracket_re = re.compile(r"^(.*)\[(\d+)\]$")

    _valid_underscore_properties = {
        "error_x": "error-x",
        "error_y": "error-y",
        "error_z": "error-z",
        "copy_xstyle": "copy-xstyle",
        "copy_ystyle": "copy-ystyle",
        "copy_zstyle": "copy-zstyle",
        "paper_bgcolor": "paper-bgcolor",
        "plot_bgcolor": "plot-bgcolor",
    }

    _set_trace_uid = False
    _allow_disable_validation = True

    # Constructor
    # -----------
    def __init__(
        self, data=None, layout_plotly=None, frames=None, skip_invalid=False, **kwargs
    ):
        """
        Construct a BaseFigure object

        Parameters
        ----------
        data
            One of:
            - A list or tuple of trace objects (or dicts that can be coerced
            into trace objects)

            - If `data` is a dict that contains a 'data',
            'layout', or 'frames' key then these values are used to
            construct the figure.

            - If `data` is a `BaseFigure` instance then the `data`, `layout`,
            and `frames` properties are extracted from the input figure
        layout_plotly
            The plotly layout dict.

            Note: this property is named `layout_plotly` rather than `layout`
            to deconflict it with the `layout` constructor parameter of the
            `widgets.DOMWidget` ipywidgets class, as the `BaseFigureWidget`
            class is a subclass of both BaseFigure and widgets.DOMWidget.

            If the `data` property is a BaseFigure instance, or a dict that
            contains a 'layout' key, then this property is ignored.
        frames
            A list or tuple of `plotly.graph_objs.Frame` objects (or dicts
            that can be coerced into Frame objects)

            If the `data` property is a BaseFigure instance, or a dict that
            contains a 'frames' key, then this property is ignored.

        skip_invalid: bool
            If True, invalid properties in the figure specification will be
            skipped silently. If False (default) invalid properties in the
            figure specification will result in a ValueError

        Raises
        ------
        ValueError
            if a property in the specification of data, layout, or frames
            is invalid AND skip_invalid is False
        """
        from .validator_cache import ValidatorCache

        data_validator = ValidatorCache.get_validator("", "data")
        frames_validator = ValidatorCache.get_validator("", "frames")
        layout_validator = ValidatorCache.get_validator("", "layout")

        super(BaseFigure, self).__init__()

        # Initialize validation
        self._validate = kwargs.pop("_validate", True)

        # Assign layout_plotly to layout
        # ------------------------------
        # See docstring note for explanation
        layout = layout_plotly

        # Subplot properties
        # ------------------
        # These properties are used by the tools.make_subplots logic.
        # We initialize them to None here, before checking if the input data
        # object is a BaseFigure, or a dict with _grid_str and _grid_ref
        # properties, in which case we bring over the _grid* properties of
        # the input
        self._grid_str = None
        self._grid_ref = None

        # Handle case where data is a Figure or Figure-like dict
        # ------------------------------------------------------
        if isinstance(data, BaseFigure):
            # Bring over subplot fields
            self._grid_str = data._grid_str
            self._grid_ref = data._grid_ref

            # Extract data, layout, and frames
            data, layout, frames = data.data, data.layout, data.frames

        elif isinstance(data, dict) and (
            "data" in data or "layout" in data or "frames" in data
        ):
            # Bring over subplot fields
            self._grid_str = data.get("_grid_str", None)
            self._grid_ref = data.get("_grid_ref", None)

            # Extract data, layout, and frames
            data, layout, frames = (
                data.get("data", None),
                data.get("layout", None),
                data.get("frames", None),
            )

        # Handle data (traces)
        # --------------------
        # ### Construct data validator ###
        # This is the validator that handles importing sequences of trace
        # objects
        # We make a copy because we are overriding the set_uid attribute
        # and do not want to alter all other uses of the cached data_validator
        self._data_validator = copy(data_validator)
        self._data_validator.set_uid = self._set_trace_uid

        # ### Import traces ###
        data = self._data_validator.validate_coerce(
            data, skip_invalid=skip_invalid, _validate=self._validate
        )

        # ### Save tuple of trace objects ###
        self._data_objs = data

        # ### Import clone of trace properties ###
        # The _data property is a list of dicts containing the properties
        # explicitly set by the user for each trace.
        self._data = [deepcopy(trace._props) for trace in data]

        # ### Create data defaults ###
        # _data_defaults is a tuple of dicts, one for each trace. When
        # running in a widget context, these defaults are populated with
        # all property values chosen by the Plotly.js library that
        # aren't explicitly specified by the user.
        #
        # Note: No property should exist in both the _data and
        # _data_defaults for the same trace.
        self._data_defaults = [{} for _ in data]

        # ### Reparent trace objects ###
        for trace_ind, trace in enumerate(data):
            # By setting the trace's parent to be this figure, we tell the
            # trace object to use the figure's _data and _data_defaults
            # dicts to get/set its properties, rather than using the trace
            # object's internal _orphan_props dict.
            trace._parent = self

            # We clear the orphan props since the trace no longer needs then
            trace._orphan_props.clear()

            # Set trace index
            trace._trace_ind = trace_ind

        # Layout
        # ------
        # ### Construct layout validator ###
        # This is the validator that handles importing Layout objects
        self._layout_validator = layout_validator

        # ### Import Layout ###
        self._layout_obj = self._layout_validator.validate_coerce(
            layout, skip_invalid=skip_invalid, _validate=self._validate
        )

        # ### Import clone of layout properties ###
        self._layout = deepcopy(self._layout_obj._props)

        # ### Initialize layout defaults dict ###
        self._layout_defaults = {}

        # ### Reparent layout object ###
        self._layout_obj._orphan_props.clear()
        self._layout_obj._parent = self

        # Config
        # ------
        # Pass along default config to the front end. For now this just
        # ensures that the plotly domain url gets passed to the front end.
        # In the future we can extend this to allow the user to supply
        # arbitrary config options like in plotly.offline.plot/iplot.  But
        # this will require a fair amount of testing to determine which
        # options are compatible with FigureWidget.
        from plotly.offline.offline import _get_jconfig

        self._config = _get_jconfig(None)

        # Frames
        # ------

        # ### Construct frames validator ###
        # This is the validator that handles importing sequences of frame
        # objects
        self._frames_validator = frames_validator

        # ### Import frames ###
        self._frame_objs = self._frames_validator.validate_coerce(
            frames, skip_invalid=skip_invalid
        )

        # Note: Because frames are not currently supported in the widget
        # context, we don't need to follow the pattern above and create
        # _frames and _frame_defaults properties and then reparent the
        # frames. The figure doesn't need to be notified of
        # changes to the properties in the frames object hierarchy.

        # Context manager
        # ---------------

        # ### batch mode indicator ###
        # Flag that indicates whether we're currently inside a batch_*()
        # context
        self._in_batch_mode = False

        # ### Batch trace edits ###
        # Dict from trace indexes to trace edit dicts. These trace edit dicts
        # are suitable as `data` elements of Plotly.animate, but not
        # the Plotly.update (See `_build_update_params_from_batch`)
        self._batch_trace_edits = OrderedDict()

        # ### Batch layout edits ###
        # Dict from layout properties to new layout values. This dict is
        # directly suitable for use in Plotly.animate and Plotly.update
        self._batch_layout_edits = OrderedDict()

        # Animation property validators
        # -----------------------------
        from . import animation

        self._animation_duration_validator = animation.DurationValidator()
        self._animation_easing_validator = animation.EasingValidator()

        # Template
        # --------
        # ### Check for default template ###
        self._initialize_layout_template()

        # Process kwargs
        # --------------
        for k, v in kwargs.items():
            err = _check_path_in_prop_tree(self, k)
            if err is None:
                self[k] = v
            elif not skip_invalid:
                type_err = TypeError("invalid Figure property: {}".format(k))
                type_err.args = (
                    type_err.args[0]
                    + """
%s"""
                    % (err.args[0],),
                )
                raise type_err

    # Magic Methods
    # -------------
    def __reduce__(self):
        """
        Custom implementation of reduce is used to support deep copying
        and pickling
        """
        props = self.to_dict()
        props["_grid_str"] = self._grid_str
        props["_grid_ref"] = self._grid_ref
        return (self.__class__, (props,))

    def __setitem__(self, prop, value):
        # Normalize prop
        # --------------
        # Convert into a property tuple
        orig_prop = prop
        prop = BaseFigure._str_to_dict_path(prop)

        # Handle empty case
        # -----------------
        if len(prop) == 0:
            raise KeyError(orig_prop)

        # Handle scalar case
        # ------------------
        # e.g. ('foo',)
        elif len(prop) == 1:
            # ### Unwrap scalar tuple ###
            prop = prop[0]

            if prop == "data":
                self.data = value
            elif prop == "layout":
                self.layout = value
            elif prop == "frames":
                self.frames = value
            else:
                raise KeyError(prop)

        # Handle non-scalar case
        # ----------------------
        # e.g. ('foo', 1)
        else:
            err = _check_path_in_prop_tree(self, orig_prop, error_cast=ValueError)
            if err is not None:
                raise err
            res = self
            for p in prop[:-1]:
                res = res[p]

            res._validate = self._validate

            res[prop[-1]] = value

    def __setattr__(self, prop, value):
        """
        Parameters
        ----------
        prop : str
            The name of a direct child of this object
        value
            New property value
        Returns
        -------
        None
        """
        if prop.startswith("_") or hasattr(self, prop):
            # Let known properties and private properties through
            super(BaseFigure, self).__setattr__(prop, value)
        else:
            # Raise error on unknown public properties
            raise AttributeError(prop)

    def __getitem__(self, prop):
        # Normalize prop
        # --------------
        # Convert into a property tuple
        orig_prop = prop
        prop = BaseFigure._str_to_dict_path(prop)

        # Handle scalar case
        # ------------------
        # e.g. ('foo',)
        if len(prop) == 1:
            # Unwrap scalar tuple
            prop = prop[0]

            if prop == "data":
                return self._data_validator.present(self._data_objs)
            elif prop == "layout":
                return self._layout_validator.present(self._layout_obj)
            elif prop == "frames":
                return self._frames_validator.present(self._frame_objs)
            else:
                raise KeyError(orig_prop)

        # Handle non-scalar case
        # ----------------------
        # e.g. ('foo', 1)
        else:
            err = _check_path_in_prop_tree(self, orig_prop, error_cast=PlotlyKeyError)
            if err is not None:
                raise err
            res = self
            for p in prop:
                res = res[p]

            return res

    def __iter__(self):
        return iter(("data", "layout", "frames"))

    def __contains__(self, prop):
        prop = BaseFigure._str_to_dict_path(prop)
        if prop[0] not in ("data", "layout", "frames"):
            return False
        elif len(prop) == 1:
            return True
        else:
            return prop[1:] in self[prop[0]]

    def __eq__(self, other):
        if not isinstance(other, BaseFigure):
            # Require objects to both be BaseFigure instances
            return False
        else:
            # Compare plotly_json representations

            # Use _vals_equal instead of `==` to handle cases where
            # underlying dicts contain numpy arrays
            return BasePlotlyType._vals_equal(
                self.to_plotly_json(), other.to_plotly_json()
            )

    def __repr__(self):
        """
        Customize Figure representation when displayed in the
        terminal/notebook
        """
        props = self.to_plotly_json()

        # Elide template
        template_props = props.get("layout", {}).get("template", {})
        if template_props:
            props["layout"]["template"] = "..."

        repr_str = BasePlotlyType._build_repr_for_class(
            props=props, class_name=self.__class__.__name__
        )

        return repr_str

    def _repr_html_(self):
        """
        Customize html representation
        """
        pass

    def _repr_mimebundle_(self, include=None, exclude=None, validate=True, **kwargs):
        """
        Return mimebundle corresponding to default renderer.
        """
        pass

    def _ipython_display_(self):
        """
        Handle rich display of figures in ipython contexts
        """
        pass

    def _set_property(self, name, arg, provided):
        """
        Initialize a property of this object using the provided value
        or a value popped from the arguments dictionary. If neither
        is available, do not set the property.
        """
        pass

    def update(self, dict1=None, overwrite=False, **kwargs):
        """
        Update the properties of the figure with a dict and/or with
        keyword arguments.

        This recursively updates the structure of the figure
        object with the values in the input dict / keyword arguments.

        Parameters
        ----------
        dict1 : dict
            Dictionary of properties to be updated
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        kwargs :
            Keyword/value pair of properties to be updated

        Examples
        --------
        >>> import plotly.graph_objs as go
        >>> fig = go.Figure(data=[{'y': [1, 2, 3]}])
        >>> fig.update(data=[{'y': [4, 5, 6]}]) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.to_plotly_json() # doctest: +SKIP
            {'data': [{'type': 'scatter',
               'uid': 'e86a7c7a-346a-11e8-8aa8-a0999b0c017b',
               'y': array([4, 5, 6], dtype=int32)}],
             'layout': {}}

        >>> fig = go.Figure(layout={'xaxis':
        ...                         {'color': 'green',
        ...                          'range': [0, 1]}})
        >>> fig.update({'layout': {'xaxis': {'color': 'pink'}}}) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.to_plotly_json() # doctest: +SKIP
            {'data': [],
             'layout': {'xaxis':
                        {'color': 'pink',
                         'range': [0, 1]}}}

        Returns
        -------
        BaseFigure
            Updated figure
        """
        with self.batch_update():
            for d in [dict1, kwargs]:
                if d:
                    for k, v in d.items():
                        update_target = self[k]
                        if update_target == () or overwrite:
                            if k == "data":
                                # Overwrite all traces as special due to
                                # restrictions on trace assignment
                                self.data = ()
                                self.add_traces(v)
                            else:
                                # Accept v
                                self[k] = v
                        elif (
                            isinstance(update_target, BasePlotlyType)
                            and isinstance(v, (dict, BasePlotlyType))
                        ) or (
                            isinstance(update_target, tuple)
                            and isinstance(update_target[0], BasePlotlyType)
                        ):
                            BaseFigure._perform_update(self[k], v)
                        else:
                            self[k] = v
        return self

    def pop(self, key, *args):
        """
        Remove the value associated with the specified key and return it

        Parameters
        ----------
        key: str
            Property name
        dflt
            The default value to return if key was not found in figure

        Returns
        -------
        value
            The removed value that was previously associated with key

        Raises
        ------
        KeyError
            If key is not in object and no dflt argument specified
        """
        # Handle default
        if key not in self and args:
            return args[0]
        elif key in self:
            val = self[key]
            self[key] = None
            return val
        else:
            raise KeyError(key)

    # Data
    # ----
    @property
    def data(self):
        """
        The `data` property is a tuple of the figure's trace objects

        Returns
        -------
        tuple[BaseTraceType]
        """
        pass


    def select_traces(self, selector=None, row=None, col=None, secondary_y=None):
        """
        Select traces from a particular subplot cell and/or traces
        that satisfy custom selection criteria.

        Parameters
        ----------
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all traces are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each trace and those for which the function returned True
            will be in the selection. If an int N, the Nth trace matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of traces to select.
            To select traces by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  If None
            (the default), all traces are selected.
        secondary_y: boolean or None (default None)
            * If True, only select traces associated with the secondary
              y-axis of the subplot.
            * If False, only select traces associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter traces based on secondary
              y-axis.

            To select traces by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        generator
            Generator that iterates through all of the traces that satisfy
            all of the specified selection criteria
        """
        if not selector and not isinstance(selector, int):
            selector = {}

        if row is not None or col is not None or secondary_y is not None:
            grid_ref = self._validate_get_grid_ref()
            filter_by_subplot = True

            if row is None and col is not None:
                # All rows for column
                grid_subplot_ref_tuples = [ref_row[col - 1] for ref_row in grid_ref]
            elif col is None and row is not None:
                # All columns for row
                grid_subplot_ref_tuples = grid_ref[row - 1]
            elif col is not None and row is not None:
                # Single grid cell
                grid_subplot_ref_tuples = [grid_ref[row - 1][col - 1]]
            else:
                # row and col are None, secondary_y not None
                grid_subplot_ref_tuples = [
                    refs for refs_row in grid_ref for refs in refs_row
                ]

            # Collect list of subplot refs, taking secondary_y into account
            grid_subplot_refs = []
            for refs in grid_subplot_ref_tuples:
                if not refs:
                    continue
                if secondary_y is not True:
                    grid_subplot_refs.append(refs[0])

                if secondary_y is not False and len(refs) > 1:
                    grid_subplot_refs.append(refs[1])

        else:
            filter_by_subplot = False
            grid_subplot_refs = None

        return self._perform_select_traces(
            filter_by_subplot, grid_subplot_refs, selector
        )

    def _perform_select_traces(self, filter_by_subplot, grid_subplot_refs, selector):
        from plotly._subplots import _get_subplot_ref_for_trace

        # functions for filtering

        funcs = []
        if filter_by_subplot:
            funcs.append(_filter_by_subplot_ref)

        return _generator(self._filter_by_selector(self.data, funcs, selector))

    @staticmethod
    def _selector_matches(obj, selector):
        if selector is None:
            return True
        # If selector is a string then put it at the 'type' key of a dictionary
        # to select objects where "type":selector
        if isinstance(selector, str):
            selector = dict(type=selector)
        # If selector is a dict, compare the fields
        if isinstance(selector, dict) or isinstance(selector, BasePlotlyType):
            # This returns True if selector is an empty dict
            for k in selector:
                if k not in obj:
                    return False

                obj_val = obj[k]
                selector_val = selector[k]

                if isinstance(obj_val, BasePlotlyType):
                    obj_val = obj_val.to_plotly_json()

                if isinstance(selector_val, BasePlotlyType):
                    selector_val = selector_val.to_plotly_json()

                if obj_val != selector_val:
                    return False
            return True
        # If selector is a function, call it with the obj as the argument
        elif callable(selector):
            return selector(obj)
        else:
            raise TypeError(
                "selector must be dict or a function "
                "accepting a graph object returning a boolean."
            )

    def _filter_by_selector(self, objects, funcs, selector):
        """
        objects is a sequence of objects, funcs a list of functions that
        return True if the object should be included in the selection and False
        otherwise and selector is an argument to the self._selector_matches
        function.
        If selector is an integer, the resulting sequence obtained after
        sucessively filtering by each function in funcs is indexed by this
        integer.
        Otherwise selector is used as the selector argument to
        self._selector_matches which is used to filter down the sequence.
        The function returns the sequence (an iterator).
        """

        # if selector is not an int, we call it on each trace to test it for selection
        if not isinstance(selector, int):
            funcs.append(lambda obj: self._selector_matches(obj, selector))


        filtered_objects = reduce(_filt, funcs, objects)

        if isinstance(selector, int):
            return iter([list(filtered_objects)[selector]])

        return filtered_objects

    def for_each_trace(self, fn, selector=None, row=None, col=None, secondary_y=None):
        """
        Apply a function to all traces that satisfy the specified selection
        criteria

        Parameters
        ----------
        fn:
            Function that inputs a single trace object.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all traces are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each trace and those for which the function returned True
            will be in the selection. If an int N, the Nth trace matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of traces to select.
            To select traces by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  If None
            (the default), all traces are selected.
        secondary_y: boolean or None (default None)
            * If True, only select traces associated with the secondary
              y-axis of the subplot.
            * If False, only select traces associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter traces based on secondary
              y-axis.

            To select traces by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        pass

    def update_traces(
        self,
        patch=None,
        selector=None,
        row=None,
        col=None,
        secondary_y=None,
        overwrite=False,
        **kwargs,
    ):
        """
        Perform a property update operation on all traces that satisfy the
        specified selection criteria

        Parameters
        ----------
        patch: dict or None (default None)
            Dictionary of property updates to be applied to all traces that
            satisfy the selection criteria.
        selector: dict, function, int, str or None (default None)
            Dict to use as selection criteria.
            Traces will be selected if they contain properties corresponding
            to all of the dictionary's keys, with values that exactly match
            the supplied values. If None (the default), all traces are
            selected. If a function, it must be a function accepting a single
            argument and returning a boolean. The function will be called on
            each trace and those for which the function returned True
            will be in the selection. If an int N, the Nth trace matching row
            and col will be selected (N can be negative). If a string S, the selector
            is equivalent to dict(type=S).
        row, col: int or None (default None)
            Subplot row and column index of traces to select.
            To select traces by row and column, the Figure must have been
            created using plotly.subplots.make_subplots.  If None
            (the default), all traces are selected.
        secondary_y: boolean or None (default None)
            * If True, only select traces associated with the secondary
              y-axis of the subplot.
            * If False, only select traces associated with the primary
              y-axis of the subplot.
            * If None (the default), do not filter traces based on secondary
              y-axis.

            To select traces by secondary y-axis, the Figure must have been
            created using plotly.subplots.make_subplots. See the docstring
            for the specs argument to make_subplots for more info on
            creating subplots with secondary y-axes.
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        **kwargs
            Additional property updates to apply to each selected trace. If
            a property is specified in both patch and in **kwargs then the
            one in **kwargs takes precedence.

        Returns
        -------
        self
            Returns the Figure object that the method was called on
        """
        for trace in self.select_traces(
            selector=selector, row=row, col=col, secondary_y=secondary_y
        ):
            trace.update(patch, overwrite=overwrite, **kwargs)
        return self

    def update_layout(self, dict1=None, overwrite=False, **kwargs):
        """
        Update the properties of the figure's layout with a dict and/or with
        keyword arguments.

        This recursively updates the structure of the original
        layout with the values in the input dict / keyword arguments.

        Parameters
        ----------
        dict1 : dict
            Dictionary of properties to be updated
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        kwargs :
            Keyword/value pair of properties to be updated

        Returns
        -------
        BaseFigure
            The Figure object that the update_layout method was called on
        """
        self.layout.update(dict1, overwrite=overwrite, **kwargs)
        return self

    def _select_layout_subplots_by_prefix(
        self, prefix, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Helper called by code generated select_* methods
        """

        if row is not None or col is not None or secondary_y is not None:
            # Build mapping from container keys ('xaxis2', 'scene4', etc.)
            # to (row, col, secondary_y) triplets
            grid_ref = self._validate_get_grid_ref()
            container_to_row_col = {}
            for r, subplot_row in enumerate(grid_ref):
                for c, subplot_refs in enumerate(subplot_row):
                    if not subplot_refs:
                        continue

                    # collect primary keys
                    for i, subplot_ref in enumerate(subplot_refs):
                        for layout_key in subplot_ref.layout_keys:
                            if layout_key.startswith(prefix):
                                is_secondary_y = i == 1
                                container_to_row_col[layout_key] = (
                                    r + 1,
                                    c + 1,
                                    is_secondary_y,
                                )
        else:
            container_to_row_col = None

        layout_keys_filters = [
            lambda k: k.startswith(prefix) and self.layout[k] is not None,
            lambda k: row is None
            or container_to_row_col.get(k, (None, None, None))[0] == row,
            lambda k: col is None
            or container_to_row_col.get(k, (None, None, None))[1] == col,
            lambda k: (
                secondary_y is None
                or container_to_row_col.get(k, (None, None, None))[2] == secondary_y
            ),
        ]
        layout_keys = reduce(
            lambda last, f: filter(f, last),
            layout_keys_filters,
            # Natural sort keys so that xaxis20 is after xaxis3
            _natural_sort_strings(list(self.layout)),
        )
        layout_objs = [self.layout[k] for k in layout_keys]
        return _generator(self._filter_by_selector(layout_objs, [], selector))

    def _select_annotations_like(
        self, prop, selector=None, row=None, col=None, secondary_y=None
    ):
        """
        Helper to select annotation-like elements from a layout object array.
        Compatible with layout.annotations, layout.shapes, and layout.images
        """
        pass


    # Restyle
    # -------
    def plotly_restyle(self, restyle_data, trace_indexes=None, **kwargs):
        """
        Perform a Plotly restyle operation on the figure's traces

        Parameters
        ----------
        restyle_data : dict
            Dict of trace style updates.

            Keys are strings that specify the properties to be updated.
            Nested properties are expressed by joining successive keys on
            '.' characters (e.g. 'marker.color').

            Values may be scalars or lists. When values are scalars,
            that scalar value is applied to all traces specified by the
            `trace_indexes` parameter.  When values are lists,
            the restyle operation will cycle through the elements
            of the list as it cycles through the traces specified by the
            `trace_indexes` parameter.

            Caution: To use plotly_restyle to update a list property (e.g.
            the `x` property of the scatter trace), the property value
            should be a scalar list containing the list to update with. For
            example, the following command would be used to update the 'x'
            property of the first trace to the list [1, 2, 3]

            >>> import plotly.graph_objects as go
            >>> fig = go.Figure(go.Scatter(x=[2, 4, 6]))
            >>> fig.plotly_restyle({'x': [[1, 2, 3]]}, 0)

        trace_indexes : int or list of int
            Trace index, or list of trace indexes, that the restyle operation
            applies to. Defaults to all trace indexes.

        Returns
        -------
        None
        """
        pass

    def _perform_plotly_restyle(self, restyle_data, trace_indexes):
        """
        Perform a restyle operation on the figure's traces data and return
        the changes that were applied

        Parameters
        ----------
        restyle_data : dict[str, any]
            See docstring for plotly_restyle
        trace_indexes : list[int]
            List of trace indexes that restyle operation applies to
        Returns
        -------
        restyle_changes: dict[str, any]
            Subset of restyle_data including only the keys / values that
            resulted in a change to the figure's traces data
        """
        # Initialize restyle changes
        # --------------------------
        # This will be a subset of the restyle_data including only the
        # keys / values that are changed in the figure's trace data
        restyle_changes = {}

        # Process each key
        # ----------------
        for key_path_str, v in restyle_data.items():
            # Track whether any of the new values are cause a change in
            # self._data
            any_vals_changed = False
            for i, trace_ind in enumerate(trace_indexes):
                if trace_ind >= len(self._data):
                    raise ValueError(
                        "Trace index {trace_ind} out of range".format(
                            trace_ind=trace_ind
                        )
                    )

                # Get new value for this particular trace
                trace_v = v[i % len(v)] if isinstance(v, list) else v

                if trace_v is not Undefined:
                    # Get trace being updated
                    trace_obj = self.data[trace_ind]

                    # Validate key_path_str
                    if not BaseFigure._is_key_path_compatible(key_path_str, trace_obj):
                        trace_class = trace_obj.__class__.__name__
                        raise ValueError(
                            """
Invalid property path '{key_path_str}' for trace class {trace_class}
""".format(key_path_str=key_path_str, trace_class=trace_class)
                        )

                    # Apply set operation for this trace and thist value
                    val_changed = BaseFigure._set_in(
                        self._data[trace_ind], key_path_str, trace_v
                    )

                    # Update any_vals_changed status
                    any_vals_changed = any_vals_changed or val_changed

            if any_vals_changed:
                restyle_changes[key_path_str] = v

        return restyle_changes

    def _restyle_child(self, child, key_path_str, val):
        """
        Process restyle operation on a child trace object

        Note: This method name/signature must match the one in
        BasePlotlyType. BasePlotlyType objects call their parent's
        _restyle_child method without knowing whether their parent is a
        BasePlotlyType or a BaseFigure.

        Parameters
        ----------
        child : BaseTraceType
            Child being restyled
        key_path_str : str
            A key path string (e.g. 'foo.bar[0]')
        val
            Restyle value

        Returns
        -------
        None
        """
        pass

    def _normalize_trace_indexes(self, trace_indexes):
        """
        Input trace index specification and return list of the specified trace
        indexes

        Parameters
        ----------
        trace_indexes : None or int or list[int]

        Returns
        -------
        list[int]
        """
        if trace_indexes is None:
            trace_indexes = list(range(len(self.data)))
        if not isinstance(trace_indexes, (list, tuple)):
            trace_indexes = [trace_indexes]
        return list(trace_indexes)

    @staticmethod
    def _str_to_dict_path(key_path_str):
        """
        Convert a key path string into a tuple of key path elements.

        Parameters
        ----------
        key_path_str : str
            Key path string, where nested keys are joined on '.' characters
            and array indexes are specified using brackets
            (e.g. 'foo.bar[1]')
        Returns
        -------
        tuple[str | int]
        """
        if (
            isinstance(key_path_str, str)
            and "." not in key_path_str
            and "[" not in key_path_str
            and "_" not in key_path_str
        ):
            # Fast path for common case that avoids regular expressions
            return (key_path_str,)
        elif isinstance(key_path_str, tuple):
            # Nothing to do
            return key_path_str
        else:
            ret = _str_to_dict_path_full(key_path_str)[0]
            return ret

    @staticmethod
    def _set_in(d, key_path_str, v):
        """
        Set a value in a nested dict using a key path string
        (e.g. 'foo.bar[0]')

        Parameters
        ----------
        d : dict
            Input dict to set property in
        key_path_str : str
            Key path string, where nested keys are joined on '.' characters
            and array indexes are specified using brackets
            (e.g. 'foo.bar[1]')
        v
            New value
        Returns
        -------
        bool
            True if set resulted in modification of dict (i.e. v was not
            already present at the specified location), False otherwise.
        """

        # Validate inputs
        # ---------------
        assert isinstance(d, dict)

        # Compute key path
        # ----------------
        # Convert the key_path_str into a tuple of key paths
        # e.g. 'foo.bar[0]' -> ('foo', 'bar', 0)
        key_path = BaseFigure._str_to_dict_path(key_path_str)

        # Initialize val_parent
        # ---------------------
        # This variable will be assigned to the parent of the next key path
        # element currently being processed
        val_parent = d

        # Initialize parent dict or list of value to be assigned
        # -----------------------------------------------------
        for kp, key_path_el in enumerate(key_path[:-1]):
            # Extend val_parent list if needed
            if isinstance(val_parent, list) and isinstance(key_path_el, int):
                while len(val_parent) <= key_path_el:
                    val_parent.append(None)

            elif isinstance(val_parent, dict) and key_path_el not in val_parent:
                if isinstance(key_path[kp + 1], int):
                    val_parent[key_path_el] = []
                else:
                    val_parent[key_path_el] = {}

            val_parent = val_parent[key_path_el]

        # Assign value to final parent dict or list
        # --------------------------------------------
        # ### Get reference to final key path element ###
        last_key = key_path[-1]

        # ### Track whether assignment alters parent ###
        val_changed = False

        # v is Undefined
        # --------------
        # Don't alter val_parent
        if v is Undefined:
            pass

        # v is None
        # ---------
        # Check whether we can remove key from parent
        elif v is None:
            if isinstance(val_parent, dict):
                if last_key in val_parent:
                    # Parent is a dict and has last_key as a current key so
                    # we can pop the key, which alters parent
                    val_parent.pop(last_key)
                    val_changed = True
            elif isinstance(val_parent, list):
                if isinstance(last_key, int) and 0 <= last_key < len(val_parent):
                    # Parent is a list and last_key is a valid index so we
                    # can set the element value to None
                    val_parent[last_key] = None
                    val_changed = True
            else:
                # Unsupported parent type (numpy array for example)
                raise ValueError(
                    """
    Cannot remove element of type {typ} at location {raw_key}""".format(
                        typ=type(val_parent), raw_key=key_path_str
                    )
                )
        # v is a valid value
        # ------------------
        # Check whether parent should be updated
        else:
            if isinstance(val_parent, dict):
                if last_key not in val_parent or not BasePlotlyType._vals_equal(
                    val_parent[last_key], v
                ):
                    # Parent is a dict and does not already contain the
                    # value v at key last_key
                    val_parent[last_key] = v
                    val_changed = True
            elif isinstance(val_parent, list):
                if isinstance(last_key, int):
                    # Extend list with Nones if needed so that last_key is
                    # in bounds
                    while len(val_parent) <= last_key:
                        val_parent.append(None)

                    if not BasePlotlyType._vals_equal(val_parent[last_key], v):
                        # Parent is a list and does not already contain the
                        # value v at index last_key
                        val_parent[last_key] = v
                        val_changed = True
            else:
                # Unsupported parent type (numpy array for example)
                raise ValueError(
                    """
    Cannot set element of type {typ} at location {raw_key}""".format(
                        typ=type(val_parent), raw_key=key_path_str
                    )
                )
        return val_changed

    # Add traces
    # ----------
    @staticmethod
    def _raise_invalid_rows_cols(name, n, invalid):
        rows_err_msg = """
        If specified, the {name} parameter must be a list or tuple of integers
        of length {n} (The number of traces being added)

        Received: {invalid}
        """.format(name=name, n=n, invalid=invalid)

        raise ValueError(rows_err_msg)

    @staticmethod
    def _validate_rows_cols(name, n, vals):
        if vals is None:
            pass
        elif isinstance(vals, (list, tuple)):
            if len(vals) != n:
                BaseFigure._raise_invalid_rows_cols(name=name, n=n, invalid=vals)

            int_type = _get_int_type()

            if [r for r in vals if not isinstance(r, int_type)]:
                BaseFigure._raise_invalid_rows_cols(name=name, n=n, invalid=vals)
        else:
            BaseFigure._raise_invalid_rows_cols(name=name, n=n, invalid=vals)

    def add_trace(
        self, trace, row=None, col=None, secondary_y=None, exclude_empty_subplots=False
    ):
        """
        Add a trace to the figure

        Parameters
        ----------
        trace : BaseTraceType or dict
            Either:
              - An instances of a trace classe from the plotly.graph_objs
                package (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)
              - or a dicts where:

                  - The 'type' property specifies the trace type (e.g.
                    'scatter', 'bar', 'area', etc.). If the dict has no 'type'
                    property then 'scatter' is assumed.
                  - All remaining properties are passed to the constructor
                    of the specified trace type.

        row : 'all', int or None (default)
            Subplot row index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`.
            If 'all', addresses all rows in the specified column(s).
        col : 'all', int or None (default)
            Subplot col index (starting from 1) for the trace to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`.
            If 'all', addresses all columns in the specified row(s).
        secondary_y: boolean or None (default None)
            If True, associate this trace with the secondary y-axis of the
            subplot at the specified row and col. Only valid if all of the
            following conditions are satisfied:
              * The figure was created using `plotly.subplots.make_subplots`.
              * The row and col arguments are not None
              * The subplot at the specified row and col has type xy
                (which is the default) and secondary_y True.  These
                properties are specified in the specs argument to
                make_subplots. See the make_subplots docstring for more info.
              * The trace argument is a 2D cartesian trace
                (scatter, bar, etc.)
        exclude_empty_subplots: boolean
            If True, the trace will not be added to subplots that don't already
            have traces.
        Returns
        -------
        BaseFigure
            The Figure that add_trace was called on

        Examples
        --------

        >>> from plotly import subplots
        >>> import plotly.graph_objs as go

        Add two Scatter traces to a figure

        >>> fig = go.Figure()
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2])) # doctest: +ELLIPSIS
        Figure(...)


        Add two Scatter traces to vertically stacked subplots

        >>> fig = subplots.make_subplots(rows=2)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1) # doctest: +ELLIPSIS
        Figure(...)
        >>> fig.add_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1) # doctest: +ELLIPSIS
        Figure(...)
        """
        # Make sure we have both row and col or neither
        if row is not None and col is None:
            raise ValueError(
                "Received row parameter but not col.\n"
                "row and col must be specified together"
            )
        elif col is not None and row is None:
            raise ValueError(
                "Received col parameter but not row.\n"
                "row and col must be specified together"
            )

        # Address multiple subplots
        if row is not None and _is_select_subplot_coordinates_arg(row, col):
            # TODO add product argument
            rows_cols = self._select_subplot_coordinates(row, col)
            for r, c in rows_cols:
                self.add_trace(
                    trace,
                    row=r,
                    col=c,
                    secondary_y=secondary_y,
                    exclude_empty_subplots=exclude_empty_subplots,
                )
            return self

        return self.add_traces(
            data=[trace],
            rows=[row] if row is not None else None,
            cols=[col] if col is not None else None,
            secondary_ys=[secondary_y] if secondary_y is not None else None,
            exclude_empty_subplots=exclude_empty_subplots,
        )

    def add_traces(
        self,
        data,
        rows=None,
        cols=None,
        secondary_ys=None,
        exclude_empty_subplots=False,
    ):
        """
        Add traces to the figure

        Parameters
        ----------
        data : list[BaseTraceType or dict]
            A list of trace specifications to be added.
            Trace specifications may be either:

              - Instances of trace classes from the plotly.graph_objs
                package (e.g plotly.graph_objs.Scatter, plotly.graph_objs.Bar)
              - Dicts where:

                  - The 'type' property specifies the trace type (e.g.
                    'scatter', 'bar', 'area', etc.). If the dict has no 'type'
                    property then 'scatter' is assumed.
                  - All remaining properties are passed to the constructor
                    of the specified trace type.

        rows : None, list[int], or int (default None)
            List of subplot row indexes (starting from 1) for the traces to be
            added. Only valid if figure was created using
            `plotly.tools.make_subplots`
            If a single integer is passed, all traces will be added to row number

        cols : None or list[int] (default None)
            List of subplot column indexes (starting from 1) for the traces
            to be added. Only valid if figure was created using
            `plotly.tools.make_subplots`
            If a single integer is passed, all traces will be added to column number


        secondary_ys: None or list[boolean] (default None)
            List of secondary_y booleans for traces to be added. See the
            docstring for `add_trace` for more info.

        exclude_empty_subplots: boolean
            If True, the trace will not be added to subplots that don't already
            have traces.

        Returns
        -------
        BaseFigure
            The Figure that add_traces was called on

        Examples
        --------

        >>> from plotly import subplots
        >>> import plotly.graph_objs as go

        Add two Scatter traces to a figure

        >>> fig = go.Figure()
        >>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),
        ...                 go.Scatter(x=[1,2,3], y=[2,1,2])]) # doctest: +ELLIPSIS
        Figure(...)

        Add two Scatter traces to vertically stacked subplots

        >>> fig = subplots.make_subplots(rows=2)
        >>> fig.add_traces([go.Scatter(x=[1,2,3], y=[2,1,2]),
        ...                 go.Scatter(x=[1,2,3], y=[2,1,2])],
        ...                 rows=[1, 2], cols=[1, 1]) # doctest: +ELLIPSIS
        Figure(...)
        """

        # Validate traces
        data = self._data_validator.validate_coerce(data)

        # Set trace indexes
        for ind, new_trace in enumerate(data):
            new_trace._trace_ind = ind + len(self.data)

        # Allow integers as inputs to subplots
        int_type = _get_int_type()

        if isinstance(rows, int_type):
            rows = [rows] * len(data)

        if isinstance(cols, int_type):
            cols = [cols] * len(data)

        # Validate rows / cols
        n = len(data)
        BaseFigure._validate_rows_cols("rows", n, rows)
        BaseFigure._validate_rows_cols("cols", n, cols)

        # Make sure we have both rows and cols or neither
        if rows is not None and cols is None:
            raise ValueError(
                "Received rows parameter but not cols.\n"
                "rows and cols must be specified together"
            )
        elif cols is not None and rows is None:
            raise ValueError(
                "Received cols parameter but not rows.\n"
                "rows and cols must be specified together"
            )

        # Process secondary_ys defaults
        if secondary_ys is not None and rows is None:
            # Default rows/cols to 1s if secondary_ys specified but not rows
            # or cols
            rows = [1] * len(secondary_ys)
            cols = rows
        elif secondary_ys is None and rows is not None:
            # Default secondary_ys to Nones if secondary_ys is not specified
            # but not rows and cols are specified
            secondary_ys = [None] * len(rows)

        # Apply rows / cols
        if rows is not None:
            for trace, row, col, secondary_y in zip(data, rows, cols, secondary_ys):
                self._set_trace_grid_position(trace, row, col, secondary_y)

        if exclude_empty_subplots:
            data = list(
                filter(
                    lambda trace: self._subplot_not_empty(
                        trace["xaxis"], trace["yaxis"], bool(exclude_empty_subplots)
                    ),
                    data,
                )
            )

        # Make deep copy of trace data (Optimize later if needed)
        new_traces_data = [deepcopy(trace._props) for trace in data]

        # Update trace parent
        for trace in data:
            trace._parent = self
            trace._orphan_props.clear()

        # Update python side
        #  Use extend instead of assignment so we don't trigger serialization
        self._data.extend(new_traces_data)
        self._data_defaults = self._data_defaults + [{} for _ in data]
        self._data_objs = self._data_objs + data

        # Update messages
        self._send_addTraces_msg(new_traces_data)

        return self

    # Subplots
    # --------
    def print_grid(self):
        """
        Print a visual layout of the figure's axes arrangement.
        This is only valid for figures that are created
        with plotly.tools.make_subplots.
        """
        pass

    def append_trace(self, trace, row, col):
        """
        Add a trace to the figure bound to axes at the specified row,
        col index.

        A row, col index grid is generated for figures created with
        plotly.tools.make_subplots, and can be viewed with the `print_grid`
        method

        Parameters
        ----------
        trace
            The data trace to be bound
        row: int
            Subplot row index (see Figure.print_grid)
        col: int
            Subplot column index (see Figure.print_grid)

        Examples
        --------

        >>> from plotly import tools
        >>> import plotly.graph_objs as go
        >>> # stack two subplots vertically
        >>> fig = tools.make_subplots(rows=2)

        This is the format of your plot grid:
        [ (1,1) x1,y1 ]
        [ (2,1) x2,y2 ]

        >>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=1, col=1)
        >>> fig.append_trace(go.Scatter(x=[1,2,3], y=[2,1,2]), row=2, col=1)
        """
        pass

    def _set_trace_grid_position(self, trace, row, col, secondary_y=False):
        from plotly._subplots import _set_trace_grid_reference

        grid_ref = self._validate_get_grid_ref()
        return _set_trace_grid_reference(
            trace, self.layout, grid_ref, row, col, secondary_y
        )

    def _validate_get_grid_ref(self):
        try:
            grid_ref = self._grid_ref
            if grid_ref is None:
                raise AttributeError("_grid_ref")
        except AttributeError:
            raise Exception(
                "In order to reference traces by row and column, "
                "you must first use "
                "plotly.tools.make_subplots "
                "to create the figure with a subplot grid."
            )
        return grid_ref

    def _get_subplot_rows_columns(self):
        """
        Returns a pair of lists, the first containing all the row indices and
        the second all the column indices.
        """
        # currently, this just iterates over all the rows and columns (because
        # self._grid_ref is currently always rectangular)
        grid_ref = self._validate_get_grid_ref()
        nrows = len(grid_ref)
        ncols = len(grid_ref[0])
        return (range(1, nrows + 1), range(1, ncols + 1))

    def _get_subplot_coordinates(self):
        """
        Returns an iterator over (row,col) pairs representing all the possible
        subplot coordinates.
        """
        pass

    def _select_subplot_coordinates(self, rows, cols, product=False):
        """
        Allows selecting all or a subset of the subplots.
        If any of rows or columns is 'all', product is set to True. This is
        probably the expected behaviour, so that rows=1,cols='all' selects all
        the columns in row 1 (otherwise it would just select the subplot in the
        first row and first column).
        """
        product |= any([s == "all" for s in [rows, cols]])
        # TODO: If grid_ref ever becomes non-rectangular, then t should be the
        # set-intersection of the result of _indexing_combinations and
        # _get_subplot_coordinates, because some coordinates given by
        # the _indexing_combinations function might be invalid.
        t = _indexing_combinations(
            [rows, cols],
            list(self._get_subplot_rows_columns()),
            product=product,
        )
        t = list(t)
        # remove rows and cols where the subplot is "None"
        grid_ref = self._validate_get_grid_ref()
        t = list(filter(lambda u: grid_ref[u[0] - 1][u[1] - 1] is not None, t))
        return t

    def get_subplot(self, row, col, secondary_y=False):
        """
        Return an object representing the subplot at the specified row
        and column.  May only be used on Figures created using
        plotly.tools.make_subplots

        Parameters
        ----------
        row: int
            1-based index of subplot row
        col: int
            1-based index of subplot column
        secondary_y: bool
            If True, select the subplot that consists of the x-axis and the
            secondary y-axis at the specified row/col. Only valid if the
            subplot at row/col is an 2D cartesian subplot that was created
            with a secondary y-axis.  See the docstring for the specs argument
            to make_subplots for more info on creating a subplot with a
            secondary y-axis.
        Returns
        -------
        subplot
            * None: if subplot is empty
            * plotly.graph_objs.layout.Scene: if subplot type is 'scene'
            * plotly.graph_objs.layout.Polar: if subplot type is 'polar'
            * plotly.graph_objs.layout.Ternary: if subplot type is 'ternary'
            * plotly.graph_objs.layout.Mapbox: if subplot type is 'ternary'
            * SubplotDomain namedtuple with `x` and `y` fields:
              if subplot type is 'domain'.
                - x: length 2 list of the subplot start and stop width
                - y: length 2 list of the subplot start and stop height
            * SubplotXY namedtuple with `xaxis` and `yaxis` fields:
              if subplot type is 'xy'.
                - xaxis: plotly.graph_objs.layout.XAxis instance for subplot
                - yaxis: plotly.graph_objs.layout.YAxis instance for subplot
        """
        pass

    # Child property operations
    # -------------------------
    def _get_child_props(self, child):
        """
        Return the properties dict for a child trace or child layout

        Note: this method must match the name/signature of one on
        BasePlotlyType

        Parameters
        ----------
        child : BaseTraceType | BaseLayoutType

        Returns
        -------
        dict
        """
        pass

    def _get_child_prop_defaults(self, child):
        """
        Return the default properties dict for a child trace or child layout

        Note: this method must match the name/signature of one on
        BasePlotlyType

        Parameters
        ----------
        child : BaseTraceType | BaseLayoutType

        Returns
        -------
        dict
        """
        pass

    def _init_child_props(self, child):
        """
        Initialize the properties dict for a child trace or layout

        Note: this method must match the name/signature of one on
        BasePlotlyType

        Parameters
        ----------
        child : BaseTraceType | BaseLayoutType

        Returns
        -------
        None
        """
        # layout and traces dict are initialize when figure is constructed
        # and when new traces are added to the figure
        pass

    # Layout
    # ------

    @property
    def layout(self):
        """
        The `layout` property of the figure

        Returns
        -------
        plotly.graph_objs.Layout
        """
        pass


    def plotly_relayout(self, relayout_data, **kwargs):
        """
        Perform a Plotly relayout operation on the figure's layout

        Parameters
        ----------
        relayout_data : dict
            Dict of layout updates

            dict keys are strings that specify the properties to be updated.
            Nested properties are expressed by joining successive keys on
            '.' characters (e.g. 'xaxis.range')

            dict values are the values to use to update the layout.

        Returns
        -------
        None
        """
        pass

    def _perform_plotly_relayout(self, relayout_data):
        """
        Perform a relayout operation on the figure's layout data and return
        the changes that were applied

        Parameters
        ----------
        relayout_data : dict[str, any]
            See the docstring for plotly_relayout
        Returns
        -------
        relayout_changes: dict[str, any]
            Subset of relayout_data including only the keys / values that
            resulted in a change to the figure's layout data
        """
        # Initialize relayout changes
        # ---------------------------
        # This will be a subset of the relayout_data including only the
        # keys / values that are changed in the figure's layout data
        relayout_changes = {}

        # Process each key
        # ----------------
        for key_path_str, v in relayout_data.items():
            if not BaseFigure._is_key_path_compatible(key_path_str, self.layout):
                raise ValueError(
                    """
Invalid property path '{key_path_str}' for layout
""".format(key_path_str=key_path_str)
                )

            # Apply set operation on the layout dict
            val_changed = BaseFigure._set_in(self._layout, key_path_str, v)

            if val_changed:
                relayout_changes[key_path_str] = v

        return relayout_changes

    @staticmethod
    def _is_key_path_compatible(key_path_str, plotly_obj):
        """
        Return whether the specifieid key path string is compatible with
        the specified plotly object for the purpose of relayout/restyle
        operation
        """

        # Convert string to tuple of path components
        # e.g. 'foo[0].bar[1]' -> ('foo', 0, 'bar', 1)
        key_path_tuple = BaseFigure._str_to_dict_path(key_path_str)

        # Remove trailing integer component
        # e.g. ('foo', 0, 'bar', 1) -> ('foo', 0, 'bar')
        # We do this because it's fine for relayout/restyle to create new
        # elements in the final array in the path.
        if isinstance(key_path_tuple[-1], int):
            key_path_tuple = key_path_tuple[:-1]

        # Test whether modified key path tuple is in plotly_obj
        return key_path_tuple in plotly_obj

    def _relayout_child(self, child, key_path_str, val):
        """
        Process relayout operation on child layout object

        Parameters
        ----------
        child : BaseLayoutType
            The figure's layout
        key_path_str :
            A key path string (e.g. 'foo.bar[0]')
        val
            Relayout value

        Returns
        -------
        None
        """
        pass

    # Dispatch change callbacks
    # -------------------------
    @staticmethod
    def _build_dispatch_plan(key_path_strs):
        """
        Build a dispatch plan for a list of key path strings

        A dispatch plan is a dict:
           - *from* path tuples that reference an object that has descendants
             that are referenced in `key_path_strs`.
           - *to* sets of tuples that correspond to descendants of the object
             above.

        Parameters
        ----------
        key_path_strs : list[str]
            List of key path strings. For example:

            ['xaxis.rangeselector.font.color', 'xaxis.rangeselector.bgcolor']

        Returns
        -------
        dispatch_plan: dict[tuple[str|int], set[tuple[str|int]]]

        Examples
        --------

        >>> key_path_strs = ['xaxis.rangeselector.font.color',
        ...                  'xaxis.rangeselector.bgcolor']

        >>> BaseFigure._build_dispatch_plan(key_path_strs) # doctest: +SKIP
            {(): {'xaxis',
                  ('xaxis', 'rangeselector'),
                  ('xaxis', 'rangeselector', 'bgcolor'),
                  ('xaxis', 'rangeselector', 'font'),
                  ('xaxis', 'rangeselector', 'font', 'color')},
             ('xaxis',): {('rangeselector',),
                          ('rangeselector', 'bgcolor'),
                          ('rangeselector', 'font'),
                          ('rangeselector', 'font', 'color')},
             ('xaxis', 'rangeselector'): {('bgcolor',),
                                          ('font',),
                                          ('font', 'color')},
             ('xaxis', 'rangeselector', 'font'): {('color',)}}
        """
        dispatch_plan = {}

        for key_path_str in key_path_strs:
            key_path = BaseFigure._str_to_dict_path(key_path_str)
            key_path_so_far = ()
            keys_left = key_path

            # Iterate down the key path
            for next_key in key_path:
                if key_path_so_far not in dispatch_plan:
                    dispatch_plan[key_path_so_far] = set()

                to_add = [keys_left[: i + 1] for i in range(len(keys_left))]
                dispatch_plan[key_path_so_far].update(to_add)

                key_path_so_far = key_path_so_far + (next_key,)
                keys_left = keys_left[1:]

        return dispatch_plan

    def _dispatch_layout_change_callbacks(self, relayout_data):
        """
        Dispatch property change callbacks given relayout_data

        Parameters
        ----------
        relayout_data : dict[str, any]
            See docstring for plotly_relayout.

        Returns
        -------
        None
        """
        # Build dispatch plan
        # -------------------
        key_path_strs = list(relayout_data.keys())
        dispatch_plan = BaseFigure._build_dispatch_plan(key_path_strs)

        # Dispatch changes to each layout objects
        # ---------------------------------------
        for path_tuple, changed_paths in dispatch_plan.items():
            if path_tuple in self.layout:
                dispatch_obj = self.layout[path_tuple]
                if isinstance(dispatch_obj, BasePlotlyType):
                    dispatch_obj._dispatch_change_callbacks(changed_paths)

    def _dispatch_trace_change_callbacks(self, restyle_data, trace_indexes):
        """
        Dispatch property change callbacks given restyle_data

        Parameters
        ----------
        restyle_data : dict[str, any]
            See docstring for plotly_restyle.

        trace_indexes : list[int]
            List of trace indexes that restyle operation applied to

        Returns
        -------
        None
        """

        # Build dispatch plan
        # -------------------
        key_path_strs = list(restyle_data.keys())
        dispatch_plan = BaseFigure._build_dispatch_plan(key_path_strs)

        # Dispatch changes to each object in each trace
        # ---------------------------------------------
        for path_tuple, changed_paths in dispatch_plan.items():
            for trace_ind in trace_indexes:
                trace = self.data[trace_ind]
                if path_tuple in trace:
                    dispatch_obj = trace[path_tuple]
                    if isinstance(dispatch_obj, BasePlotlyType):
                        dispatch_obj._dispatch_change_callbacks(changed_paths)

    # Frames
    # ------
    @property
    def frames(self):
        """
        The `frames` property is a tuple of the figure's frame objects

        Returns
        -------
        tuple[plotly.graph_objs.Frame]
        """
        pass


    # Update
    # ------
    def plotly_update(
        self, restyle_data=None, relayout_data=None, trace_indexes=None, **kwargs
    ):
        """
        Perform a Plotly update operation on the figure.

        Note: This operation both mutates and returns the figure

        Parameters
        ----------
        restyle_data : dict
            Traces update specification. See the docstring for the
            `plotly_restyle` method for details
        relayout_data : dict
            Layout update specification. See the docstring for the
            `plotly_relayout` method for details
        trace_indexes :
            Trace index, or list of trace indexes, that the update operation
            applies to. Defaults to all trace indexes.

        Returns
        -------
        BaseFigure
            None
        """

        # Handle source_view_id
        # ---------------------
        # If not None, the source_view_id is the UID of the frontend
        # Plotly.js view that initially triggered this update operation
        # (e.g. the user clicked a button that triggered an update
        # operation). We pass this UID along so that the frontend views can
        # determine whether they need to apply the update operation on
        # themselves.
        if "source_view_id" in kwargs:
            msg_kwargs = {"source_view_id": kwargs["source_view_id"]}
        else:
            msg_kwargs = {}

        # Perform update operation
        # ------------------------
        # This updates the _data and _layout dicts, and returns the changes
        # to the traces (restyle_changes) and layout (relayout_changes)
        (
            restyle_changes,
            relayout_changes,
            trace_indexes,
        ) = self._perform_plotly_update(
            restyle_data=restyle_data,
            relayout_data=relayout_data,
            trace_indexes=trace_indexes,
        )

        # Send update message
        # -------------------
        # Send a plotly_update message to the frontend (if any)
        if restyle_changes or relayout_changes:
            self._send_update_msg(
                restyle_data=restyle_changes,
                relayout_data=relayout_changes,
                trace_indexes=trace_indexes,
                **msg_kwargs,
            )

        # Dispatch changes
        # ----------------
        # ### Dispatch restyle changes ###
        if restyle_changes:
            self._dispatch_trace_change_callbacks(restyle_changes, trace_indexes)

        # ### Dispatch relayout changes ###
        if relayout_changes:
            self._dispatch_layout_change_callbacks(relayout_changes)

    def _perform_plotly_update(
        self, restyle_data=None, relayout_data=None, trace_indexes=None
    ):
        # Check for early exist
        # ---------------------
        if not restyle_data and not relayout_data:
            # Nothing to do
            return None, None, None

        # Normalize input
        # ---------------
        if restyle_data is None:
            restyle_data = {}
        if relayout_data is None:
            relayout_data = {}

        trace_indexes = self._normalize_trace_indexes(trace_indexes)

        # Perform relayout
        # ----------------
        relayout_changes = self._perform_plotly_relayout(relayout_data)

        # Perform restyle
        # ---------------
        restyle_changes = self._perform_plotly_restyle(restyle_data, trace_indexes)

        # Return changes
        # --------------
        return restyle_changes, relayout_changes, trace_indexes

    # Plotly message stubs
    # --------------------
    # send-message stubs that may be overridden by the widget subclass
    def _send_addTraces_msg(self, new_traces_data):
        pass

    def _send_moveTraces_msg(self, current_inds, new_inds):
        pass

    def _send_deleteTraces_msg(self, delete_inds):
        pass

    def _send_restyle_msg(self, style, trace_indexes=None, source_view_id=None):
        pass

    def _send_relayout_msg(self, layout, source_view_id=None):
        pass

    def _send_update_msg(
        self, restyle_data, relayout_data, trace_indexes=None, source_view_id=None
    ):
        pass

    def _send_animate_msg(
        self, styles_data, relayout_data, trace_indexes, animation_opts
    ):
        pass

    # Context managers
    # ----------------
    @contextmanager
    def batch_update(self):
        """
        A context manager that batches up trace and layout assignment
        operations into a singe plotly_update message that is executed when
        the context exits.

        Examples
        --------
        For example, suppose we have a figure widget, `fig`, with a single
        trace.

        >>> import plotly.graph_objs as go
        >>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])

        If we want to update the xaxis range, the yaxis range, and the
        marker color, we could do so using a series of three property
        assignments as follows:

        >>> fig.layout.xaxis.range = [0, 5]
        >>> fig.layout.yaxis.range = [0, 10]
        >>> fig.data[0].marker.color = 'green'

        This will work, however it will result in three messages being
        sent to the front end (two relayout messages for the axis range
        updates followed by one restyle message for the marker color
        update). This can cause the plot to appear to stutter as the
        three updates are applied incrementally.

        We can avoid this problem by performing these three assignments in a
        `batch_update` context as follows:

        >>> with fig.batch_update():
        ...     fig.layout.xaxis.range = [0, 5]
        ...     fig.layout.yaxis.range = [0, 10]
        ...     fig.data[0].marker.color = 'green'

        Now, these three property updates will be sent to the frontend in a
        single update message, and they will be applied by the front end
        simultaneously.
        """
        if self._in_batch_mode is True:
            yield
        else:
            try:
                self._in_batch_mode = True
                yield
            finally:
                # ### Disable batch mode ###
                self._in_batch_mode = False

                # ### Build plotly_update params ###
                (
                    restyle_data,
                    relayout_data,
                    trace_indexes,
                ) = self._build_update_params_from_batch()

                # ### Call plotly_update ###
                self.plotly_update(
                    restyle_data=restyle_data,
                    relayout_data=relayout_data,
                    trace_indexes=trace_indexes,
                )

                # ### Clear out saved batch edits ###
                self._batch_layout_edits.clear()
                self._batch_trace_edits.clear()

    def _build_update_params_from_batch(self):
        """
        Convert `_batch_trace_edits` and `_batch_layout_edits` into the
        `restyle_data`, `relayout_data`, and `trace_indexes` params accepted
        by the `plotly_update` method.

        Returns
        -------
        (dict, dict, list[int])
        """

        # Handle Style / Trace Indexes
        # ----------------------------
        batch_style_commands = self._batch_trace_edits
        trace_indexes = sorted(set([trace_ind for trace_ind in batch_style_commands]))

        all_props = sorted(
            set(
                [
                    prop
                    for trace_style in self._batch_trace_edits.values()
                    for prop in trace_style
                ]
            )
        )

        # Initialize restyle_data dict with all values undefined
        restyle_data = {
            prop: [Undefined for _ in range(len(trace_indexes))] for prop in all_props
        }

        # Fill in values
        for trace_ind, trace_style in batch_style_commands.items():
            for trace_prop, trace_val in trace_style.items():
                restyle_trace_index = trace_indexes.index(trace_ind)
                restyle_data[trace_prop][restyle_trace_index] = trace_val

        # Handle Layout
        # -------------
        relayout_data = self._batch_layout_edits

        # Return plotly_update params
        # ---------------------------
        return restyle_data, relayout_data, trace_indexes

    @contextmanager
    def batch_animate(self, duration=500, easing="cubic-in-out"):
        """
        Context manager to animate trace / layout updates

        Parameters
        ----------
        duration : number
            The duration of the transition, in milliseconds.
            If equal to zero, updates are synchronous.
        easing : string
            The easing function used for the transition.
            One of:
                - linear
                - quad
                - cubic
                - sin
                - exp
                - circle
                - elastic
                - back
                - bounce
                - linear-in
                - quad-in
                - cubic-in
                - sin-in
                - exp-in
                - circle-in
                - elastic-in
                - back-in
                - bounce-in
                - linear-out
                - quad-out
                - cubic-out
                - sin-out
                - exp-out
                - circle-out
                - elastic-out
                - back-out
                - bounce-out
                - linear-in-out
                - quad-in-out
                - cubic-in-out
                - sin-in-out
                - exp-in-out
                - circle-in-out
                - elastic-in-out
                - back-in-out
                - bounce-in-out

        Examples
        --------
        Suppose we have a figure widget, `fig`, with a single trace.

        >>> import plotly.graph_objs as go
        >>> fig = go.FigureWidget(data=[{'y': [3, 4, 2]}])

        1) Animate a change in the xaxis and yaxis ranges using default
        duration and easing parameters.

        >>> with fig.batch_animate():
        ...     fig.layout.xaxis.range = [0, 5]
        ...     fig.layout.yaxis.range = [0, 10]

        2) Animate a change in the size and color of the trace's markers
        over 2 seconds using the elastic-in-out easing method

        >>> with fig.batch_animate(duration=2000, easing='elastic-in-out'):
        ...     fig.data[0].marker.color = 'green'
        ...     fig.data[0].marker.size = 20
        """
        pass

    def _perform_batch_animate(self, animation_opts):
        """
        Perform the batch animate operation

        This method should be called with the batch_animate() context
        manager exits.

        Parameters
        ----------
        animation_opts : dict
            Animation options as accepted by frontend Plotly.animation command

        Returns
        -------
        None
        """
        pass

    # Exports
    # -------
    def to_dict(self):
        """
        Convert figure to a dictionary

        Note: the dictionary includes the properties explicitly set by the
        user, it does not include default values of unspecified properties

        Returns
        -------
        dict
        """
        # Handle data
        # -----------
        data = deepcopy(self._data)

        # Handle layout
        # -------------
        layout = deepcopy(self._layout)

        # Handle frames
        # -------------
        # Frame key is only added if there are any frames
        res = {"data": data, "layout": layout}
        frames = deepcopy([frame._props for frame in self._frame_objs])

        if frames:
            res["frames"] = frames

        # Add base64 conversion before sending to the front-end
        convert_to_base64(res)

        return res

    def to_plotly_json(self):
        """
        Convert figure to a JSON representation as a Python dict

        Note: May include some JSON-invalid data types, use the `PlotlyJSONEncoder` util
        or the `to_json` method to encode to a string.

        Returns
        -------
        dict
        """
        return self.to_dict()

    @staticmethod
    def _to_ordered_dict(d, skip_uid=False):
        """
        Static helper for converting dict or list to structure of ordered
        dictionaries
        """
        pass


    # plotly.io methods
    # -----------------
    # Note that docstrings are auto-generated in plotly/_docstring_gen.py
    def show(self, *args, **kwargs):
        """
        Show a figure using either the default renderer(s) or the renderer(s)
        specified by the renderer argument

        Parameters
        ----------
        renderer: str or None (default None)
            A string containing the names of one or more registered renderers
            (separated by '+' characters) or None.  If None, then the default
            renderers specified in plotly.io.renderers.default are used.

        validate: bool (default True)
            True if the figure should be validated before being shown,
            False otherwise.

        width: int or float
            An integer or float that determines the number of pixels wide the
            plot is. The default is set in plotly.js.

        height: int or float
            An integer or float specifying the height of the plot in pixels.
            The default is set in plotly.js.

        config: dict
            A dict of parameters to configure the figure. The defaults are set
            in plotly.js.

        Returns
        -------
        None
        """
        import plotly.io as pio

        return pio.show(self, *args, **kwargs)

    def to_json(self, *args, **kwargs):
        """
        Convert a figure to a JSON string representation

        Parameters
        ----------
        validate: bool (default True)
            True if the figure should be validated before being converted to
            JSON, False otherwise.

        pretty: bool (default False)
            True if JSON representation should be pretty-printed, False if
            representation should be as compact as possible.

        remove_uids: bool (default True)
            True if trace UIDs should be omitted from the JSON representation

        engine: str (default None)
            The JSON encoding engine to use. One of:
              - "json" for an encoder based on the built-in Python json module
              - "orjson" for a fast encoder the requires the orjson package
            If not specified, the default encoder is set to the current value of
            plotly.io.json.config.default_encoder.

        Returns
        -------
        str
            Representation of figure as a JSON string
        """
        import plotly.io as pio

        return pio.to_json(self, *args, **kwargs)

    def full_figure_for_development(self, warn=True, as_dict=False):
        """
        Compute default values for all attributes not specified in the input figure and
        returns the output as a "full" figure. This function calls Plotly.js via Kaleido
        to populate unspecified attributes. This function is intended for interactive use
        during development to learn more about how Plotly.js computes default values and is
        not generally necessary or recommended for production use.

        Parameters
        ----------
        fig:
            Figure object or dict representing a figure

        warn: bool
            If False, suppress warnings about not using this in production.

        as_dict: bool
            If True, output is a dict with some keys that go.Figure can't parse.
            If False, output is a go.Figure with unparseable keys skipped.

        Returns
        -------
        plotly.graph_objects.Figure or dict
            The full figure
        """
        pass

    def write_json(self, *args, **kwargs):
        """
        Convert a figure to JSON and write it to a file or writeable
        object

        Parameters
        ----------
        file: str or writeable
            A string representing a local file path or a writeable object
            (e.g. an open file descriptor)

        pretty: bool (default False)
            True if JSON representation should be pretty-printed, False if
            representation should be as compact as possible.

        remove_uids: bool (default True)
            True if trace UIDs should be omitted from the JSON representation

        engine: str (default None)
            The JSON encoding engine to use. One of:
              - "json" for an encoder based on the built-in Python json module
              - "orjson" for a fast encoder the requires the orjson package
            If not specified, the default encoder is set to the current value of
            plotly.io.json.config.default_encoder.

        Returns
        -------
        None
        """
        pass

    def to_html(self, *args, **kwargs):
        """
        Convert a figure to an HTML string representation.

        Parameters
        ----------
        config: dict or None (default None)
            Plotly.js figure config options
        auto_play: bool (default=True)
            Whether to automatically start the animation sequence on page load
            if the figure contains frames. Has no effect if the figure does not
            contain frames.
        include_plotlyjs: bool or string (default True)
            Specifies how the plotly.js library is included/loaded in the output
            div string.

            If True, a script tag containing the plotly.js source code (~3MB)
            is included in the output.  HTML files generated with this option are
            fully self-contained and can be used offline.

            If 'cdn', a script tag that references the plotly.js CDN is included
            in the output. HTML files generated with this option are about 3MB
            smaller than those generated with include_plotlyjs=True, but they
            require an active internet connection in order to load the plotly.js
            library.

            If 'directory', a script tag is included that references an external
            plotly.min.js bundle that is assumed to reside in the same
            directory as the HTML file.

            If a string that ends in '.js', a script tag is included that
            references the specified path. This approach can be used to point
            the resulting HTML file to an alternative CDN or local bundle.

            If False, no script tag referencing plotly.js is included. This is
            useful when the resulting div string will be placed inside an HTML
            document that already loads plotly.js. This option is not advised
            when full_html=True as it will result in a non-functional html file.
        include_mathjax: bool or string (default False)
            Specifies how the MathJax.js library is included in the output html
            div string.  MathJax is required in order to display labels
            with LaTeX typesetting.

            If False, no script tag referencing MathJax.js will be included in the
            output.

            If 'cdn', a script tag that references a MathJax CDN location will be
            included in the output.  HTML div strings generated with this option
            will be able to display LaTeX typesetting as long as internet access
            is available.

            If a string that ends in '.js', a script tag is included that
            references the specified path. This approach can be used to point the
            resulting HTML div string to an alternative CDN.
        post_script: str or list or None (default None)
            JavaScript snippet(s) to be included in the resulting div just after
            plot creation.  The string(s) may include '{plot_id}' placeholders
            that will then be replaced by the `id` of the div element that the
            plotly.js figure is associated with.  One application for this script
            is to install custom plotly.js event handlers.
        full_html: bool (default True)
            If True, produce a string containing a complete HTML document
            starting with an <html> tag.  If False, produce a string containing
            a single <div> element.
        animation_opts: dict or None (default None)
            dict of custom animation parameters to be passed to the function
            Plotly.animate in Plotly.js. See
            https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
            for available options. Has no effect if the figure does not contain
            frames, or auto_play is False.
        default_width, default_height: number or str (default '100%')
            The default figure width/height to use if the provided figure does not
            specify its own layout.width/layout.height property.  May be
            specified in pixels as an integer (e.g. 500), or as a css width style
            string (e.g. '500px', '100%').
        validate: bool (default True)
            True if the figure should be validated before being converted to
            JSON, False otherwise.
        div_id: str (default None)
            If provided, this is the value of the id attribute of the div tag. If None, the
            id attribute is a UUID.

        Returns
        -------
        str
            Representation of figure as an HTML div string
        """
        import plotly.io as pio

        return pio.to_html(self, *args, **kwargs)

    def write_html(self, *args, **kwargs):
        """
        Write a figure to an HTML file representation

        Parameters
        ----------
        file: str or writeable
            A string representing a local file path or a writeable object
            (e.g. a pathlib.Path object or an open file descriptor)
        config: dict or None (default None)
            Plotly.js figure config options
        auto_play: bool (default=True)
            Whether to automatically start the animation sequence on page load
            if the figure contains frames. Has no effect if the figure does not
            contain frames.
        include_plotlyjs: bool or string (default True)
            Specifies how the plotly.js library is included/loaded in the output
            div string.

            If True, a script tag containing the plotly.js source code (~3MB)
            is included in the output.  HTML files generated with this option are
            fully self-contained and can be used offline.

            If 'cdn', a script tag that references the plotly.js CDN is included
            in the output. HTML files generated with this option are about 3MB
            smaller than those generated with include_plotlyjs=True, but they
            require an active internet connection in order to load the plotly.js
            library.

            If 'directory', a script tag is included that references an external
            plotly.min.js bundle that is assumed to reside in the same
            directory as the HTML file. If `file` is a string to a local file
            path and `full_html` is True, then the plotly.min.js bundle is copied
            into the directory of the resulting HTML file. If a file named
            plotly.min.js already exists in the output directory then this file
            is left unmodified and no copy is performed. HTML files generated
            with this option can be used offline, but they require a copy of
            the plotly.min.js bundle in the same directory. This option is
            useful when many figures will be saved as HTML files in the same
            directory because the plotly.js source code will be included only
            once per output directory, rather than once per output file.

            If a string that ends in '.js', a script tag is included that
            references the specified path. This approach can be used to point
            the resulting HTML file to an alternative CDN or local bundle.

            If False, no script tag referencing plotly.js is included. This is
            useful when the resulting div string will be placed inside an HTML
            document that already loads plotly.js.  This option is not advised
            when full_html=True as it will result in a non-functional html file.

        include_mathjax: bool or string (default False)
            Specifies how the MathJax.js library is included in the output html
            div string.  MathJax is required in order to display labels
            with LaTeX typesetting.

            If False, no script tag referencing MathJax.js will be included in the
            output.

            If 'cdn', a script tag that references a MathJax CDN location will be
            included in the output.  HTML div strings generated with this option
            will be able to display LaTeX typesetting as long as internet access
            is available.

            If a string that ends in '.js', a script tag is included that
            references the specified path. This approach can be used to point the
            resulting HTML div string to an alternative CDN.
        post_script: str or list or None (default None)
            JavaScript snippet(s) to be included in the resulting div just after
            plot creation.  The string(s) may include '{plot_id}' placeholders
            that will then be replaced by the `id` of the div element that the
            plotly.js figure is associated with.  One application for this script
            is to install custom plotly.js event handlers.
        full_html: bool (default True)
            If True, produce a string containing a complete HTML document
            starting with an <html> tag.  If False, produce a string containing
            a single <div> element.
        animation_opts: dict or None (default None)
            dict of custom animation parameters to be passed to the function
            Plotly.animate in Plotly.js. See
            https://github.com/plotly/plotly.js/blob/master/src/plots/animation_attributes.js
            for available options. Has no effect if the figure does not contain
            frames, or auto_play is False.
        default_width, default_height: number or str (default '100%')
            The default figure width/height to use if the provided figure does not
            specify its own layout.width/layout.height property.  May be
            specified in pixels as an integer (e.g. 500), or as a css width style
            string (e.g. '500px', '100%').
        validate: bool (default True)
            True if the figure should be validated before being converted to
            JSON, False otherwise.
        auto_open: bool (default True)
            If True, open the saved file in a web browser after saving.
            This argument only applies if `full_html` is True.
        div_id: str (default None)
            If provided, this is the value of the id attribute of the div tag. If None, the
            id attribute is a UUID.

        Returns
        -------
        None
        """
        import plotly.io as pio

        return pio.write_html(self, *args, **kwargs)

    def to_image(self, *args, **kwargs):
        """
        Convert a figure to a static image bytes string

        Parameters
        ----------
        format: str or None
            The desired image format. One of
              - 'png'
              - 'jpg' or 'jpeg'
              - 'webp'
              - 'svg'
              - 'pdf'
              - 'eps' (deprecated) (Requires the poppler library to be installed)

            If not specified, will default to:
                - `plotly.io.defaults.default_format` if engine is "kaleido"
                - `plotly.io.orca.config.default_format` if engine is "orca" (deprecated)

        width: int or None
            The width of the exported image in layout pixels. If the `scale`
            property is 1.0, this will also be the width of the exported image
            in physical pixels.

            If not specified, will default to:
                - `plotly.io.defaults.default_width` if engine is "kaleido"
                - `plotly.io.orca.config.default_width` if engine is "orca" (deprecated)

        height: int or None
            The height of the exported image in layout pixels. If the `scale`
            property is 1.0, this will also be the height of the exported image
            in physical pixels.

            If not specified, will default to:
                - `plotly.io.defaults.default_height` if engine is "kaleido"
                - `plotly.io.orca.config.default_height` if engine is "orca" (deprecated)

        scale: int or float or None
            The scale factor to use when exporting the figure. A scale factor
            larger than 1.0 will increase the image resolution with respect
            to the figure's layout pixel dimensions. Whereas as scale factor of
            less than 1.0 will decrease the image resolution.

            If not specified, will default to:
                - `plotly.io.defaults.default_scale` if engine is "kaliedo"
                - `plotly.io.orca.config.default_scale` if engine is "orca" (deprecated)

        validate: bool
            True if the figure should be validated before being converted to
            an image, False otherwise.

        engine (deprecated): str
            Image export engine to use. This parameter is deprecated and Orca engine support will be
            dropped in the next major Plotly version. Until then, the following values are supported:
            - "kaleido": Use Kaleido for image export
            - "orca": Use Orca for image export
            - "auto" (default): Use Kaleido if installed, otherwise use Orca

        Returns
        -------
        bytes
            The image data
        """
        import plotly.io as pio
        from plotly.io.kaleido import (
            kaleido_available,
            kaleido_major,
            ENABLE_KALEIDO_V0_DEPRECATION_WARNINGS,
            KALEIDO_DEPRECATION_MSG,
            ORCA_DEPRECATION_MSG,
            ENGINE_PARAM_DEPRECATION_MSG,
        )

        if ENABLE_KALEIDO_V0_DEPRECATION_WARNINGS:
            if (
                kwargs.get("engine", None) in {None, "auto", "kaleido"}
                and kaleido_available()
                and kaleido_major() < 1
            ):
                warnings.warn(KALEIDO_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
            if kwargs.get("engine", None) == "orca":
                warnings.warn(ORCA_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
            if kwargs.get("engine", None):
                warnings.warn(
                    ENGINE_PARAM_DEPRECATION_MSG, DeprecationWarning, stacklevel=2
                )

        return pio.to_image(self, *args, **kwargs)

    def write_image(self, *args, **kwargs):
        """
        Convert a figure to a static image and write it to a file or writeable
        object

        Parameters
        ----------
        file: str or writeable
            A string representing a local file path or a writeable object
            (e.g. a pathlib.Path object or an open file descriptor)

        format: str or None
            The desired image format. One of
              - 'png'
              - 'jpg' or 'jpeg'
              - 'webp'
              - 'svg'
              - 'pdf'
              - 'eps' (deprecated) (Requires the poppler library to be installed)

            If not specified and `file` is a string then this will default to the
            file extension. If not specified and `file` is not a string then this
            will default to:
                - `plotly.io.defaults.default_format` if engine is "kaleido"
                - `plotly.io.orca.config.default_format` if engine is "orca" (deprecated)

        width: int or None
            The width of the exported image in layout pixels. If the `scale`
            property is 1.0, this will also be the width of the exported image
            in physical pixels.

            If not specified, will default to:
                - `plotly.io.defaults.default_width` if engine is "kaleido"
                - `plotly.io.orca.config.default_width` if engine is "orca" (deprecated)

        height: int or None
            The height of the exported image in layout pixels. If the `scale`
            property is 1.0, this will also be the height of the exported image
            in physical pixels.

            If not specified, will default to:
                - `plotly.io.defaults.default_height` if engine is "kaleido"
                - `plotly.io.orca.config.default_height` if engine is "orca" (deprecated)

        scale: int or float or None
            The scale factor to use when exporting the figure. A scale factor
            larger than 1.0 will increase the image resolution with respect
            to the figure's layout pixel dimensions. Whereas as scale factor of
            less than 1.0 will decrease the image resolution.

            If not specified, will default to:
                - `plotly.io.defaults.default_scale` if engine is "kaleido"
                - `plotly.io.orca.config.default_scale` if engine is "orca" (deprecated)

        validate: bool
            True if the figure should be validated before being converted to
            an image, False otherwise.

        engine (deprecated): str
            Image export engine to use. This parameter is deprecated and Orca engine support will be
            dropped in the next major Plotly version. Until then, the following values are supported:
            - "kaleido": Use Kaleido for image export
            - "orca": Use Orca for image export
            - "auto" (default): Use Kaleido if installed, otherwise use Orca

        Returns
        -------
        None
        """
        import plotly.io as pio
        from plotly.io.kaleido import (
            kaleido_available,
            kaleido_major,
            ENABLE_KALEIDO_V0_DEPRECATION_WARNINGS,
            KALEIDO_DEPRECATION_MSG,
            ORCA_DEPRECATION_MSG,
            ENGINE_PARAM_DEPRECATION_MSG,
        )

        if ENABLE_KALEIDO_V0_DEPRECATION_WARNINGS:
            if (
                kwargs.get("engine", None) in {None, "auto", "kaleido"}
                and kaleido_available()
                and kaleido_major() < 1
            ):
                warnings.warn(KALEIDO_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
            if kwargs.get("engine", None) == "orca":
                warnings.warn(ORCA_DEPRECATION_MSG, DeprecationWarning, stacklevel=2)
            if kwargs.get("engine", None):
                warnings.warn(
                    ENGINE_PARAM_DEPRECATION_MSG, DeprecationWarning, stacklevel=2
                )
        return pio.write_image(self, *args, **kwargs)

    # Static helpers
    # --------------
    @staticmethod
    def _is_dict_list(v):
        """
        Return true of the input object is a list of dicts
        """
        pass

    @staticmethod
    def _perform_update(plotly_obj, update_obj, overwrite=False):
        """
        Helper to support the update() methods on :class:`BaseFigure` and
        :class:`BasePlotlyType`

        Parameters
        ----------
        plotly_obj : BasePlotlyType|tuple[BasePlotlyType]
            Object to up updated
        update_obj : dict|list[dict]|tuple[dict]
            When ``plotly_obj`` is an instance of :class:`BaseFigure`,
            ``update_obj`` should be a dict

            When ``plotly_obj`` is a tuple of instances of
            :class:`BasePlotlyType`, ``update_obj`` should be a tuple or list
            of dicts
        """
        from _plotly_utils.basevalidators import (
            CompoundValidator,
            CompoundArrayValidator,
        )

        if update_obj is None:
            # Nothing to do
            return
        elif isinstance(plotly_obj, BasePlotlyType):
            # Handle initializing subplot ids
            # -------------------------------
            # This should be valid even if xaxis2 hasn't been initialized:
            # >>> layout.update(xaxis2={'title': 'xaxis 2'})
            for key in update_obj:
                # special handling for missing keys that match _subplot_re_match
                if key not in plotly_obj and isinstance(plotly_obj, BaseLayoutType):
                    # try _subplot_re_match
                    match = plotly_obj._subplot_re_match(key)
                    if match:
                        # We need to create a subplotid object
                        plotly_obj[key] = {}
                        continue

                err = _check_path_in_prop_tree(plotly_obj, key, error_cast=ValueError)
                if err is not None:
                    raise err

            # Convert update_obj to dict
            # --------------------------
            if isinstance(update_obj, BasePlotlyType):
                update_obj = update_obj.to_plotly_json()

            # Process valid properties
            # ------------------------
            for key in update_obj:
                val = update_obj[key]

                if overwrite:
                    # Don't recurse and assign property as-is
                    plotly_obj[key] = val
                    continue

                validator = plotly_obj._get_prop_validator(key)

                if isinstance(validator, CompoundValidator) and isinstance(val, dict):
                    # Update compound objects recursively
                    # plotly_obj[key].update(val)
                    BaseFigure._perform_update(plotly_obj[key], val)
                elif isinstance(validator, CompoundArrayValidator):
                    if plotly_obj[key]:
                        # plotly_obj has an existing non-empty array for key
                        # In this case we merge val into the existing elements
                        BaseFigure._perform_update(plotly_obj[key], val)

                        # If update tuple is longer that current tuple, append the
                        # extra elements to the end
                        if isinstance(val, (list, tuple)) and len(val) > len(
                            plotly_obj[key]
                        ):
                            plotly_obj[key] = plotly_obj[key] + tuple(
                                val[len(plotly_obj[key]) :]
                            )
                    else:
                        # plotly_obj is an empty or uninitialized list for key
                        # In this case we accept val as is
                        plotly_obj[key] = val
                else:
                    # Assign non-compound value
                    plotly_obj[key] = val

        elif isinstance(plotly_obj, tuple):
            if len(update_obj) == 0:
                # Nothing to do
                return
            else:
                for i, plotly_element in enumerate(plotly_obj):
                    if isinstance(update_obj, dict):
                        if i in update_obj:
                            update_element = update_obj[i]
                        else:
                            continue
                    else:
                        update_element = update_obj[i % len(update_obj)]
                    BaseFigure._perform_update(plotly_element, update_element)
        else:
            raise ValueError(
                "Unexpected plotly object with type {typ}".format(typ=type(plotly_obj))
            )

    @staticmethod
    def _index_is(iterable, val):
        """
        Return the index of a value in an iterable using object identity
        (not object equality as is the case for list.index)

        """
        pass

    def _make_axis_spanning_layout_object(self, direction, shape):
        """
        Convert a shape drawn on a plot or a subplot into one whose yref or xref
        ends with " domain" and has coordinates so that the shape will seem to
        extend infinitely in that dimension. This is useful for drawing lines or
        boxes on a plot where one dimension of the shape will not move out of
        bounds when moving the plot's view.
        Note that the shape already added to the (sub)plot must have the
        corresponding axis reference referring to an actual axis (e.g., 'x',
        'y2' etc. are accepted, but not 'paper'). This will be the case if the
        shape was added with "add_shape".
        Shape must have the x0, x1, y0, y1 fields already initialized.
        """
        pass

    def _process_multiple_axis_spanning_shapes(
        self,
        shape_args,
        row,
        col,
        shape_type,
        exclude_empty_subplots=True,
        annotation=None,
        **kwargs,
    ):
        """
        Add a shape or multiple shapes and call _make_axis_spanning_layout_object on
        all the new shapes.
        """
        pass


    add_vline.__doc__ = _axis_spanning_shapes_docstr("vline")


    add_hline.__doc__ = _axis_spanning_shapes_docstr("hline")


    add_vrect.__doc__ = _axis_spanning_shapes_docstr("vrect")


    add_hrect.__doc__ = _axis_spanning_shapes_docstr("hrect")

    def _has_subplots(self):
        """Returns True if figure contains subplots, otherwise it contains a
        single plot and so this returns False."""
        pass

    def _subplot_not_empty(self, xref, yref, selector="all"):
        """
        xref: string representing the axis. Objects in the plot will be checked
              for this xref (for layout objects) or xaxis (for traces) to
              determine if they lie in a certain subplot.
        yref: string representing the axis. Objects in the plot will be checked
              for this yref (for layout objects) or yaxis (for traces) to
              determine if they lie in a certain subplot.
        selector: can be "all" or an iterable containing some combination of
                  "traces", "shapes", "annotations", "images". Only the presence
                  of objects specified in selector will be checked. So if
                  ["traces","shapes"] is passed then a plot we be considered
                  non-empty if it contains traces or shapes. If
                  bool(selector) returns False, no checking is performed and
                  this function returns True. If selector is True, it is
                  converted to "all".
        """
        if not selector:
            # If nothing to select was specified then a subplot is always deemed non-empty
            return True
        if selector is True:
            selector = "all"
        if selector == "all":
            selector = ["traces", "shapes", "annotations", "images"]
        ret = False
        for s in selector:
            if s == "traces":
                obj = self.data
                xaxiskw = "xaxis"
                yaxiskw = "yaxis"
            elif s in ["shapes", "annotations", "images"]:
                obj = self.layout[s]
                xaxiskw = "xref"
                yaxiskw = "yref"
            else:
                obj = None
            if obj:
                ret |= any(
                    t == (xref, yref)
                    for t in [
                        # if an object exists but has no xaxis or yaxis keys, then it
                        # is plotted with xaxis/xref 'x' and yaxis/yref 'y'
                        (
                            "x" if d[xaxiskw] is None else d[xaxiskw],
                            "y" if d[yaxiskw] is None else d[yaxiskw],
                        )
                        for d in obj
                    ]
                )
        return ret

    def set_subplots(self, rows=None, cols=None, **make_subplots_args):
        """
        Add subplots to this figure. If the figure already contains subplots,
        then this throws an error. Accepts any keyword arguments that
        plotly.subplots.make_subplots accepts.
        """
        pass


class BasePlotlyType(object):
    """
    BasePlotlyType is the base class for all objects in the trace, layout,
    and frame object hierarchies
    """

    # ### Mapped (deprecated) properties ###
    # dict for deprecated property name (e.g. 'title_font') to tuple
    # of relative path to new property (e.g. ('title', 'font')
    _mapped_properties = {}

    _parent_path_str = ""
    _path_str = ""
    _valid_props = set()

    def __init__(self, plotly_name, **kwargs):
        """
        Construct a new BasePlotlyType

        Parameters
        ----------
        plotly_name : str
            The lowercase name of the plotly object
        kwargs : dict
            Invalid props/values to raise on
        """
        # ### _skip_invalid ##
        # If True, then invalid properties should be skipped, if False then
        # invalid properties will result in an exception
        self._skip_invalid = False

        self._validate = True

        # Validate inputs
        # ---------------
        self._process_kwargs(**kwargs)

        # Store params
        # ------------
        self._plotly_name = plotly_name

        # Initialize properties
        # ---------------------
        # ### _compound_props ###
        # A dict from compound property names to compound objects
        self._compound_props = {}

        # ### _compound_array_props ###
        # A dict from compound array property names to tuples of compound
        # objects
        self._compound_array_props = {}

        # ### _orphan_props ###
        # A dict of properties for use while object has no parent. When
        # object has a parent, it requests its properties dict from its
        # parent and doesn't use this.
        self._orphan_props = {}

        # ### _parent ###
        # The parent of the object. May be another BasePlotlyType or it may
        # be a BaseFigure (as is the case for the Layout and Trace objects)
        self._parent = None

        # ### _change_callbacks ###
        # A dict from tuples of child property path tuples to lists
        # of callbacks that should be executed whenever any of these
        # properties is modified
        self._change_callbacks = {}

        # ### Backing property for backward compatible _validator property ##
        self.__validators = None

    # @property
    # def _validate(self):
    #     fig = self.figure
    #     if fig is None:
    #         return True
    #     else:
    #         return fig._validate

    def _get_validator(self, prop):
        from .validator_cache import ValidatorCache

        return ValidatorCache.get_validator(self._path_str, prop)

    def _set_property(self, name, arg, provided):
        """
        Initialize a property of this object using the provided value
        or a value popped from the arguments dictionary. If neither
        is available, do not set the property.
        """
        pass

    @property
    def _validators(self):
        """
        Validators used to be stored in a private _validators property. This was
        eliminated when we switched to building validators on demand using the
        _get_validator method.

        This property returns a simple object that

        Returns
        -------
        dict-like interface for accessing the object's validators
        """
        pass

    def _process_kwargs(self, **kwargs):
        """
        Process any extra kwargs that are not predefined as constructor params
        """
        pass
        # No need to call _raise_on_invalid_property_error here,
        # because we have it set up so that the singular case of calling
        # __setitem__ will raise this. If _check_path_in_prop_tree
        # raised that in its travels, it will already be in the error
        # message.

    @property
    def plotly_name(self):
        """
        The plotly name of the object

        Returns
        -------
        str
        """
        pass

    @property
    def _prop_descriptions(self):
        """
        Formatted string containing all of this obejcts child properties
        and their descriptions

        Returns
        -------
        str
        """
        raise NotImplementedError

    @property
    def _props(self):
        """
        Dictionary used to store this object properties.  When the object
        has a parent, this dict is retreived from the parent. When the
        object does not have a parent, this dict is the object's
        `_orphan_props` property

        Note: Property will return None if the object has a parent and the
        object's properties have not been initialized using the
        `_init_props` method.

        Returns
        -------
        dict|None
        """
        pass

    def _get_child_props(self, child):
        """
        Return properties dict for child

        Parameters
        ----------
        child : BasePlotlyType

        Returns
        -------
        dict
        """
        pass

    def _init_props(self):
        """
        Ensure that this object's properties dict has been initialized. When
        the object has a parent, this ensures that the parent has an
        initialized properties dict with this object's plotly_name as a key.

        Returns
        -------
        None
        """
        pass

    def _init_child_props(self, child):
        """
        Ensure that a properties dict has been initialized for a child object

        Parameters
        ----------
        child : BasePlotlyType

        Returns
        -------
        None
        """
        pass

    def _get_child_prop_defaults(self, child):
        """
        Return default properties dict for child

        Parameters
        ----------
        child : BasePlotlyType

        Returns
        -------
        dict
        """
        pass

    @property
    def _prop_defaults(self):
        """
        Return default properties dict

        Returns
        -------
        dict
        """
        pass

    def _get_prop_validator(self, prop):
        """
        Return the validator associated with the specified property

        Parameters
        ----------
        prop: str
            A property that exists in this object

        Returns
        -------
        BaseValidator
        """

        # Handle remapping
        # ----------------
        if prop in self._mapped_properties:
            prop_path = self._mapped_properties[prop]
            plotly_obj = self[prop_path[:-1]]
            prop = prop_path[-1]
        else:
            prop_path = BaseFigure._str_to_dict_path(prop)
            plotly_obj = self[prop_path[:-1]]
            prop = prop_path[-1]

        # Return validator
        # ----------------
        return plotly_obj._get_validator(prop)

    @property
    def parent(self):
        """
        Return the object's parent, or None if the object has no parent
        Returns
        -------
        BasePlotlyType|BaseFigure
        """
        return self._parent

    @property
    def figure(self):
        """
        Reference to the top-level Figure or FigureWidget that this object
        belongs to. None if the object does not belong to a Figure

        Returns
        -------
        Union[BaseFigure, None]
        """
        pass

    # Magic Methods
    # -------------
    def __reduce__(self):
        """
        Custom implementation of reduce is used to support deep copying
        and pickling
        """
        props = self.to_plotly_json()
        return (self.__class__, (props,))

    def __getitem__(self, prop):
        """
        Get item or nested item from object

        Parameters
        ----------
        prop : str|tuple

            If prop is the name of a property of this object, then the
            property is returned.

            If prop is a nested property path string (e.g. 'foo[1].bar'),
            then a nested property is returned (e.g. obj['foo'][1]['bar'])

            If prop is a path tuple (e.g. ('foo', 1, 'bar')), then a nested
            property is returned (e.g. obj['foo'][1]['bar']).

        Returns
        -------
        Any
        """
        from _plotly_utils.basevalidators import (
            CompoundValidator,
            CompoundArrayValidator,
            BaseDataValidator,
        )

        # Normalize prop
        # --------------
        # Convert into a property tuple
        orig_prop = prop
        prop = BaseFigure._str_to_dict_path(prop)

        # Handle remapping
        # ----------------
        if prop and prop[0] in self._mapped_properties:
            prop = self._mapped_properties[prop[0]] + prop[1:]
            orig_prop = _remake_path_from_tuple(prop)

        # Handle scalar case
        # ------------------
        # e.g. ('foo',)
        if len(prop) == 1:
            # Unwrap scalar tuple
            prop = prop[0]
            if prop not in self._valid_props:
                self._raise_on_invalid_property_error(_error_to_raise=PlotlyKeyError)(
                    prop
                )

            validator = self._get_validator(prop)

            if isinstance(validator, CompoundValidator):
                if self._compound_props.get(prop, None) is None:
                    # Init compound objects
                    self._compound_props[prop] = validator.data_class(
                        _parent=self, plotly_name=prop
                    )
                    # Update plotly_name value in case the validator applies
                    # non-standard name (e.g. imagedefaults instead of image)
                    self._compound_props[prop]._plotly_name = prop

                return validator.present(self._compound_props[prop])
            elif isinstance(validator, (CompoundArrayValidator, BaseDataValidator)):
                if self._compound_array_props.get(prop, None) is None:
                    # Init list of compound objects
                    if self._props is not None:
                        self._compound_array_props[prop] = [
                            validator.data_class(_parent=self)
                            for _ in self._props.get(prop, [])
                        ]
                    else:
                        self._compound_array_props[prop] = []

                return validator.present(self._compound_array_props[prop])
            elif self._props is not None and prop in self._props:
                return validator.present(self._props[prop])
            elif self._prop_defaults is not None:
                return validator.present(self._prop_defaults.get(prop, None))
            else:
                return None

        # Handle non-scalar case
        # ----------------------
        # e.g. ('foo', 1), ()
        else:
            err = _check_path_in_prop_tree(self, orig_prop, error_cast=PlotlyKeyError)
            if err is not None:
                raise err
            res = self
            for p in prop:
                res = res[p]

            return res

    def __contains__(self, prop):
        """
        Determine whether object contains a property or nested property

        Parameters
        ----------
        prop : str|tuple
            If prop is a simple string (e.g. 'foo'), then return true of the
            object contains an element named 'foo'

            If prop is a property path string (e.g. 'foo[0].bar'),
            then return true if the obejct contains the nested elements for
            each entry in the path string (e.g. 'bar' in obj['foo'][0])

            If prop is a property path tuple (e.g. ('foo', 0, 'bar')),
            then return true if the object contains the nested elements for
            each entry in the path string (e.g. 'bar' in obj['foo'][0])

        Returns
        -------
        bool
        """
        prop = BaseFigure._str_to_dict_path(prop)

        # Handle remapping
        if prop and prop[0] in self._mapped_properties:
            prop = self._mapped_properties[prop[0]] + prop[1:]

        obj = self
        for p in prop:
            if isinstance(p, int):
                if isinstance(obj, tuple) and 0 <= p < len(obj):
                    obj = obj[p]
                else:
                    return False
            else:
                if hasattr(obj, "_valid_props") and p in obj._valid_props:
                    obj = obj[p]
                else:
                    return False

        return True

    def __setitem__(self, prop, value):
        """
        Parameters
        ----------
        prop : str
            The name of a direct child of this object

            Note: Setting nested properties using property path string or
            property path tuples is not supported.
        value
            New property value

        Returns
        -------
        None
        """
        from _plotly_utils.basevalidators import (
            CompoundValidator,
            CompoundArrayValidator,
            BaseDataValidator,
        )

        # Normalize prop
        # --------------
        # Convert into a property tuple
        orig_prop = prop
        prop = BaseFigure._str_to_dict_path(prop)

        # Handle empty case
        # -----------------
        if len(prop) == 0:
            raise KeyError(orig_prop)

        # Handle remapping
        # ----------------
        if prop[0] in self._mapped_properties:
            prop = self._mapped_properties[prop[0]] + prop[1:]

        # Handle scalar case
        # ------------------
        # e.g. ('foo',)
        if len(prop) == 1:
            # ### Unwrap scalar tuple ###
            prop = prop[0]

            if self._validate:
                if prop not in self._valid_props:
                    self._raise_on_invalid_property_error()(prop)

                # ### Get validator for this property ###
                validator = self._get_validator(prop)

                # ### Handle compound property ###
                if isinstance(validator, CompoundValidator):
                    self._set_compound_prop(prop, value)

                # ### Handle compound array property ###
                elif isinstance(validator, (CompoundArrayValidator, BaseDataValidator)):
                    self._set_array_prop(prop, value)

                # ### Handle simple property ###
                else:
                    self._set_prop(prop, value)
            else:
                # Make sure properties dict is initialized
                self._init_props()

                if isinstance(value, BasePlotlyType):
                    # Extract json from graph objects
                    value = value.to_plotly_json()

                # Check for list/tuple of graph objects
                if (
                    isinstance(value, (list, tuple))
                    and value
                    and isinstance(value[0], BasePlotlyType)
                ):
                    value = [
                        v.to_plotly_json() if isinstance(v, BasePlotlyType) else v
                        for v in value
                    ]

                self._props[prop] = value

                # Remove any already constructed graph object so that it will be
                # reconstructed on property access
                self._compound_props.pop(prop, None)
                self._compound_array_props.pop(prop, None)

        # Handle non-scalar case
        # ----------------------
        # e.g. ('foo', 1), ()
        else:
            err = _check_path_in_prop_tree(self, orig_prop, error_cast=ValueError)
            if err is not None:
                raise err
            res = self
            for p in prop[:-1]:
                res = res[p]

            res._validate = self._validate

            res[prop[-1]] = value

    def __setattr__(self, prop, value):
        """
        Parameters
        ----------
        prop : str
            The name of a direct child of this object
        value
            New property value
        Returns
        -------
        None
        """
        if prop.startswith("_") or hasattr(self, prop) or prop in self._valid_props:
            # Let known properties and private properties through
            super(BasePlotlyType, self).__setattr__(prop, value)
        else:
            # Raise error on unknown public properties
            self._raise_on_invalid_property_error()(prop)

    def __iter__(self):
        """
        Return an iterator over the object's properties
        """
        res = list(self._valid_props)
        for prop in self._mapped_properties:
            res.append(prop)
        return iter(res)

    def __eq__(self, other):
        """
        Test for equality

        To be considered equal, `other` must have the same type as this object
        and their `to_plotly_json` representaitons must be identical.

        Parameters
        ----------
        other
            The object to compare against

        Returns
        -------
        bool
        """
        if not isinstance(other, self.__class__):
            # Require objects to be of the same plotly type
            return False
        else:
            # Compare plotly_json representations

            # Use _vals_equal instead of `==` to handle cases where
            # underlying dicts contain numpy arrays
            return BasePlotlyType._vals_equal(
                self._props if self._props is not None else {},
                other._props if other._props is not None else {},
            )

    @staticmethod
    def _build_repr_for_class(props, class_name, parent_path_str=None):
        """
        Helper to build representation string for a class

        Parameters
        ----------
        class_name : str
            Name of the class being represented
        parent_path_str : str of None (default)
            Name of the class's parent package to display
        props : dict
            Properties to unpack into the constructor

        Returns
        -------
        str
            The representation string
        """
        pass

    def __repr__(self):
        """
        Customize object representation when displayed in the
        terminal/notebook
        """
        from _plotly_utils.basevalidators import LiteralValidator

        # Get all properties
        props = self._props if self._props is not None else {}

        # Remove literals (These can't be specified in the constructor)
        props = {
            p: v
            for p, v in props.items()
            if p in self._valid_props
            and not isinstance(self._get_validator(p), LiteralValidator)
        }

        # Elide template
        if "template" in props:
            props["template"] = "..."

        # Build repr string
        repr_str = BasePlotlyType._build_repr_for_class(
            props=props,
            class_name=self.__class__.__name__,
            parent_path_str=self._parent_path_str,
        )

        return repr_str

    def _raise_on_invalid_property_error(self, _error_to_raise=None):
        """
        Returns a function that raises informative exception when invalid
        property names are encountered. The _error_to_raise argument allows
        specifying the exception to raise, which is ValueError if None.

        Parameters
        ----------
        args : list[str]
            List of property names that have already been determined to be
            invalid

        Raises
        ------
        ValueError by default, or _error_to_raise if not None
        """
        pass

    def update(self, dict1=None, overwrite=False, **kwargs):
        """
        Update the properties of an object with a dict and/or with
        keyword arguments.

        This recursively updates the structure of the original
        object with the values in the input dict / keyword arguments.

        Parameters
        ----------
        dict1 : dict
            Dictionary of properties to be updated
        overwrite: bool
            If True, overwrite existing properties. If False, apply updates
            to existing properties recursively, preserving existing
            properties that are not specified in the update operation.
        kwargs :
            Keyword/value pair of properties to be updated

        Returns
        -------
        BasePlotlyType
            Updated plotly object
        """
        if self.figure:
            with self.figure.batch_update():
                BaseFigure._perform_update(self, dict1, overwrite=overwrite)
                BaseFigure._perform_update(self, kwargs, overwrite=overwrite)
        else:
            BaseFigure._perform_update(self, dict1, overwrite=overwrite)
            BaseFigure._perform_update(self, kwargs, overwrite=overwrite)

        return self

    def pop(self, key, *args):
        """
        Remove the value associated with the specified key and return it

        Parameters
        ----------
        key: str
            Property name
        dflt
            The default value to return if key was not found in object

        Returns
        -------
        value
            The removed value that was previously associated with key

        Raises
        ------
        KeyError
            If key is not in object and no dflt argument specified
        """
        # Handle default
        if key not in self and args:
            return args[0]
        elif key in self:
            val = self[key]
            self[key] = None
            return val
        else:
            raise KeyError(key)

    @property
    def _in_batch_mode(self):
        """
        True if the object belongs to a figure that is currently in batch mode
        Returns
        -------
        bool
        """
        pass

    def _set_prop(self, prop, val):
        """
        Set the value of a simple property

        Parameters
        ----------
        prop : str
            Name of a simple (non-compound, non-array) property
        val
            The new property value

        Returns
        -------
        Any
            The coerced assigned value
        """
        pass

    def _set_compound_prop(self, prop, val):
        """
        Set the value of a compound property

        Parameters
        ----------
        prop : str
            Name of a compound property
        val
            The new property value

        Returns
        -------
        BasePlotlyType
            The coerced assigned object
        """
        pass

    def _set_array_prop(self, prop, val):
        """
        Set the value of a compound property

        Parameters
        ----------
        prop : str
            Name of a compound property
        val
            The new property value

        Returns
        -------
        tuple[BasePlotlyType]
            The coerced assigned object
        """
        pass

    def _send_prop_set(self, prop_path_str, val):
        """
        Notify parent that a property has been set to a new value

        Parameters
        ----------
        prop_path_str : str
            Property path string (e.g. 'foo[0].bar') of property that
            was set, relative to this object
        val
            New value for property. Either a simple value, a dict,
            or a tuple of dicts. This should *not* be a BasePlotlyType object.

        Returns
        -------
        None
        """
        raise NotImplementedError()

    def _prop_set_child(self, child, prop_path_str, val):
        """
        Propagate property setting notification from child to parent

        Parameters
        ----------
        child : BasePlotlyType
            Child object
        prop_path_str : str
            Property path string (e.g. 'foo[0].bar') of property that
            was set, relative to `child`
        val
            New value for property. Either a simple value, a dict,
            or a tuple of dicts. This should *not* be a BasePlotlyType object.

        Returns
        -------
        None
        """
        pass

    def _restyle_child(self, child, prop, val):
        """
        Propagate _restyle_child to parent

        Note: This method must match the name and signature of the
        corresponding method on BaseFigure
        """
        pass

    def _relayout_child(self, child, prop, val):
        """
        Propagate _relayout_child to parent

        Note: This method must match the name and signature of the
        corresponding method on BaseFigure
        """
        pass

    # Callbacks
    # ---------
    def _dispatch_change_callbacks(self, changed_paths):
        """
        Execute the appropriate change callback functions given a set of
        changed property path tuples

        Parameters
        ----------
        changed_paths : set[tuple[int|str]]

        Returns
        -------
        None
        """
        # Loop over registered callbacks
        # ------------------------------
        for prop_path_tuples, callbacks in self._change_callbacks.items():
            # ### Compute callback paths that changed ###
            common_paths = changed_paths.intersection(set(prop_path_tuples))
            if common_paths:
                # #### Invoke callback ####
                callback_args = [self[cb_path] for cb_path in prop_path_tuples]

                for callback in callbacks:
                    callback(self, *callback_args)

    def on_change(self, callback, *args, **kwargs):
        """
        Register callback function to be called when certain properties or
        subproperties of this object are modified.

        Callback will be invoked whenever ANY of these properties is
        modified. Furthermore, the callback will only be invoked once even
        if multiple properties are modified during the same restyle /
        relayout / update operation.

        Parameters
        ----------
        callback : function
            Function that accepts 1 + len(`args`) parameters. First parameter
            is this object. Second through last parameters are the
            property / subpropery values referenced by args.
        args : list[str|tuple[int|str]]
            List of property references where each reference may be one of:

              1) A property name string (e.g. 'foo') for direct properties
              2) A property path string (e.g. 'foo[0].bar') for
                 subproperties
              3) A property path tuple (e.g. ('foo', 0, 'bar')) for
                 subproperties

        append : bool
            True if callback should be appended to previously registered
            callback on the same properties, False if callback should replace
            previously registered callbacks on the same properties. Defaults
            to False.

        Examples
        --------

        Register callback that prints out the range extents of the xaxis and
        yaxis whenever either either of them changes.

        >>> import plotly.graph_objects as go
        >>> fig = go.Figure(go.Scatter(x=[1, 2], y=[1, 0]))
        >>> fig.layout.on_change(
        ...   lambda obj, xrange, yrange: print("%s-%s" % (xrange, yrange)),
        ...   ('xaxis', 'range'), ('yaxis', 'range'))


        Returns
        -------
        None
        """
        pass

    def to_plotly_json(self):
        """
        Return plotly JSON representation of object as a Python dict

        Note: May include some JSON-invalid data types, use the `PlotlyJSONEncoder` util
        or the `to_json` method to encode to a string.

        Returns
        -------
        dict
        """
        return deepcopy(self._props if self._props is not None else {})

    def to_json(self, *args, **kwargs):
        """
        Convert object to a JSON string representation

        Parameters
        ----------
        validate: bool (default True)
            True if the object should be validated before being converted to
            JSON, False otherwise.

        pretty: bool (default False)
            True if JSON representation should be pretty-printed, False if
            representation should be as compact as possible.

        remove_uids: bool (default True)
            True if trace UIDs should be omitted from the JSON representation

        engine: str (default None)
            The JSON encoding engine to use. One of:
              - "json" for an encoder based on the built-in Python json module
              - "orjson" for a fast encoder the requires the orjson package
            If not specified, the default encoder is set to the current value of
            plotly.io.json.config.default_encoder.

        Returns
        -------
        str
            Representation of object as a JSON string
        """
        import plotly.io as pio

        return pio.to_json(self, *args, **kwargs)

    @staticmethod
    def _vals_equal(v1, v2):
        """
        Recursive equality function that handles nested dicts / tuples / lists
        that contain numpy arrays.

        v1
            First value to compare
        v2
            Second value to compare

        Returns
        -------
        bool
            True if v1 and v2 are equal, False otherwise
        """
        np = get_module("numpy", should_load=False)
        if np is not None and (
            isinstance(v1, np.ndarray) or isinstance(v2, np.ndarray)
        ):
            return np.array_equal(v1, v2)
        elif isinstance(v1, (list, tuple)):
            # Handle recursive equality on lists and tuples
            return (
                isinstance(v2, (list, tuple))
                and len(v1) == len(v2)
                and all(BasePlotlyType._vals_equal(e1, e2) for e1, e2 in zip(v1, v2))
            )
        elif isinstance(v1, dict):
            # Handle recursive equality on dicts
            return (
                isinstance(v2, dict)
                and set(v1.keys()) == set(v2.keys())
                and all(BasePlotlyType._vals_equal(v1[k], v2[k]) for k in v1)
            )
        else:
            return v1 == v2


class BaseLayoutHierarchyType(BasePlotlyType):
    """
    Base class for all types in the layout hierarchy
    """

    @property
    def _parent_path_str(self):
        pass

    def __init__(self, plotly_name, **kwargs):
        super(BaseLayoutHierarchyType, self).__init__(plotly_name, **kwargs)



class BaseLayoutType(BaseLayoutHierarchyType):
    """
    Base class for the layout type. The Layout class itself is a
    code-generated subclass.
    """

    # Dynamic properties
    # ------------------
    # Unlike all other plotly types, BaseLayoutType has dynamic properties.
    # These are used when a layout has multiple instances of subplot types
    # (xaxis2, yaxis3, geo4, etc.)
    #
    # The base version of each subplot type is defined in the schema and code
    # generated. So the Layout subclass has statically defined properties
    # for xaxis, yaxis, geo, ternary, and scene. But, we need to dynamically
    # generated properties/validators as needed for xaxis2, yaxis3, etc.

    @property
    def _subplotid_validators(self):
        """
        dict of validator classes for each subplot type

        Returns
        -------
        dict
        """
        raise NotImplementedError()

    def _subplot_re_match(self, prop):
        raise NotImplementedError()

    def __init__(self, plotly_name, **kwargs):
        """
        Construct a new BaseLayoutType object

        Parameters
        ----------
        plotly_name : str
            Name of the object (should always be 'layout')
        kwargs : dict[str, any]
            Properties that were not recognized by the Layout subclass.
            These are subplot identifiers (xaxis2, geo4, etc.) or they are
            invalid properties.
        """
        # Validate inputs
        # ---------------
        assert plotly_name == "layout"

        # Call superclass constructor
        # ---------------------------
        super(BaseLayoutHierarchyType, self).__init__(plotly_name)

        # Initialize _subplotid_props
        # ---------------------------
        # This is a set storing the names of the layout's dynamic subplot
        # properties
        self._subplotid_props = set()

        # Process kwargs
        # --------------
        self._process_kwargs(**kwargs)

    def _process_kwargs(self, **kwargs):
        """
        Process any extra kwargs that are not predefined as constructor params
        """
        pass

    def _set_subplotid_prop(self, prop, value):
        """
        Set a subplot property on the layout

        Parameters
        ----------
        prop : str
            A valid subplot property
        value
            Subplot value
        """
        pass

    def _strip_subplot_suffix_of_1(self, prop):
        """
        Strip the suffix for subplot property names that have a suffix of 1.
        All other properties are returned unchanged

        e.g. 'xaxis1' -> 'xaxis'

        Parameters
        ----------
        prop : str|tuple

        Returns
        -------
        str|tuple
        """
        # Let parent handle non-scalar cases
        # ----------------------------------
        # e.g. ('xaxis', 'range') or 'xaxis.range'
        prop_tuple = BaseFigure._str_to_dict_path(prop)
        if len(prop_tuple) != 1 or not isinstance(prop_tuple[0], str):
            return prop
        else:
            # Unwrap to scalar string
            prop = prop_tuple[0]

        # Handle subplot suffix digit of 1
        # --------------------------------
        # Remove digit of 1 from subplot id (e.g.. xaxis1 -> xaxis)
        match = self._subplot_re_match(prop)

        if match:
            subplot_prop = match.group(1)
            suffix_digit = int(match.group(2))
            if subplot_prop and suffix_digit == 1:
                prop = subplot_prop

        return prop

    def _get_prop_validator(self, prop):
        """
        Custom _get_prop_validator that handles subplot properties
        """
        prop = self._strip_subplot_suffix_of_1(prop)
        return super(BaseLayoutHierarchyType, self)._get_prop_validator(prop)

    def __getattr__(self, prop):
        """
        Custom __getattr__ that handles dynamic subplot properties
        """
        prop = self._strip_subplot_suffix_of_1(prop)
        if prop != "_subplotid_props" and prop in self._subplotid_props:
            validator = self._get_validator(prop)
            return validator.present(self._compound_props[prop])
        else:
            return super(BaseLayoutHierarchyType, self).__getattribute__(prop)

    def __getitem__(self, prop):
        """
        Custom __getitem__ that handles dynamic subplot properties
        """
        prop = self._strip_subplot_suffix_of_1(prop)
        return super(BaseLayoutHierarchyType, self).__getitem__(prop)

    def __contains__(self, prop):
        """
        Custom __contains__ that handles dynamic subplot properties
        """
        prop = self._strip_subplot_suffix_of_1(prop)
        return super(BaseLayoutHierarchyType, self).__contains__(prop)

    def __setitem__(self, prop, value):
        """
        Custom __setitem__ that handles dynamic subplot properties
        """
        # Convert prop to prop tuple
        # --------------------------
        prop_tuple = BaseFigure._str_to_dict_path(prop)
        if len(prop_tuple) != 1 or not isinstance(prop_tuple[0], str):
            # Let parent handle non-scalar non-string cases
            super(BaseLayoutHierarchyType, self).__setitem__(prop, value)
            return
        else:
            # Unwrap prop tuple
            prop = prop_tuple[0]

        # Check for subplot assignment
        # ----------------------------
        match = self._subplot_re_match(prop)
        if match is None:
            # Set as ordinary property
            super(BaseLayoutHierarchyType, self).__setitem__(prop, value)
        else:
            # Set as subplotid property
            self._set_subplotid_prop(prop, value)

    def __setattr__(self, prop, value):
        """
        Custom __setattr__ that handles dynamic subplot properties
        """
        # Check for subplot assignment
        # ----------------------------
        match = self._subplot_re_match(prop)
        if match is None:
            # Set as ordinary property
            super(BaseLayoutHierarchyType, self).__setattr__(prop, value)
        else:
            # Set as subplotid property
            self._set_subplotid_prop(prop, value)

    def __dir__(self):
        """
        Custom __dir__ that handles dynamic subplot properties
        """
        # Include any active subplot values
        return list(super(BaseLayoutHierarchyType, self).__dir__()) + sorted(
            self._subplotid_props
        )


class BaseTraceHierarchyType(BasePlotlyType):
    """
    Base class for all types in the trace hierarchy
    """

    def __init__(self, plotly_name, **kwargs):
        super(BaseTraceHierarchyType, self).__init__(plotly_name, **kwargs)



class BaseTraceType(BaseTraceHierarchyType):
    """
    Base class for the all trace types.

    Specific trace type classes (Scatter, Bar, etc.) are code generated as
    subclasses of this class.
    """

    def __init__(self, plotly_name, **kwargs):
        super(BaseTraceHierarchyType, self).__init__(plotly_name, **kwargs)

        # Initialize callback function lists
        # ----------------------------------
        # ### Callbacks to be called on hover ###
        self._hover_callbacks = []

        # ### Callbacks to be called on unhover ###
        self._unhover_callbacks = []

        # ### Callbacks to be called on click ###
        self._click_callbacks = []

        # ### Callbacks to be called on selection ###
        self._select_callbacks = []

        # ### Callbacks to be called on deselect ###
        self._deselect_callbacks = []

        # ### Trace index in figure ###
        self._trace_ind = None

    # uid
    # ---
    # All trace types must have a top-level UID
    @property
    def uid(self):
        raise NotImplementedError

    @uid.setter
    def uid(self, val):
        raise NotImplementedError

    # Hover
    # -----
    def on_hover(self, callback, append=False):
        """
        Register function to be called when the user hovers over one or more
        points in this trace

        Note: Callbacks will only be triggered when the trace belongs to a
        instance of plotly.graph_objs.FigureWidget and it is displayed in an
        ipywidget context. Callbacks will not be triggered on figures
        that are displayed using plot/iplot.

        Parameters
        ----------
        callback
            Callable function that accepts 3 arguments

            - this trace
            - plotly.callbacks.Points object
            - plotly.callbacks.InputDeviceState object

        append : bool
            If False (the default), this callback replaces any previously
            defined on_hover callbacks for this trace. If True,
            this callback is appended to the list of any previously defined
            callbacks.

        Returns
        -------
        None

        Examples
        --------

        >>> import plotly.graph_objects as go
        >>> from plotly.callbacks import Points, InputDeviceState
        >>> points, state = Points(), InputDeviceState()

        >>> def hover_fn(trace, points, state):
        ...     inds = points.point_inds
        ...     # Do something

        >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
        >>> trace.on_hover(hover_fn)

        Note: The creation of the `points` and `state` objects is optional,
        it's simply a convenience to help the text editor perform completion
        on the arguments inside `hover_fn`
        """
        pass

    def _dispatch_on_hover(self, points, state):
        """
        Dispatch points and device state all all hover callbacks
        """
        pass

    # Unhover
    # -------
    def on_unhover(self, callback, append=False):
        """
        Register function to be called when the user unhovers away from one
        or more points in this trace.

        Note: Callbacks will only be triggered when the trace belongs to a
        instance of plotly.graph_objs.FigureWidget and it is displayed in an
        ipywidget context. Callbacks will not be triggered on figures
        that are displayed using plot/iplot.

        Parameters
        ----------
        callback
            Callable function that accepts 3 arguments

            - this trace
            - plotly.callbacks.Points object
            - plotly.callbacks.InputDeviceState object

        append : bool
            If False (the default), this callback replaces any previously
            defined on_unhover callbacks for this trace. If True,
            this callback is appended to the list of any previously defined
            callbacks.

        Returns
        -------
        None

        Examples
        --------

        >>> import plotly.graph_objects as go
        >>> from plotly.callbacks import Points, InputDeviceState
        >>> points, state = Points(), InputDeviceState()

        >>> def unhover_fn(trace, points, state):
        ...     inds = points.point_inds
        ...     # Do something

        >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
        >>> trace.on_unhover(unhover_fn)

        Note: The creation of the `points` and `state` objects is optional,
        it's simply a convenience to help the text editor perform completion
        on the arguments inside `unhover_fn`
        """
        pass

    def _dispatch_on_unhover(self, points, state):
        """
        Dispatch points and device state all all hover callbacks
        """
        pass

    # Click
    # -----
    def on_click(self, callback, append=False):
        """
        Register function to be called when the user clicks on one or more
        points in this trace.

        Note: Callbacks will only be triggered when the trace belongs to a
        instance of plotly.graph_objs.FigureWidget and it is displayed in an
        ipywidget context. Callbacks will not be triggered on figures
        that are displayed using plot/iplot.

        Parameters
        ----------
        callback
            Callable function that accepts 3 arguments

            - this trace
            - plotly.callbacks.Points object
            - plotly.callbacks.InputDeviceState object

        append : bool
            If False (the default), this callback replaces any previously
            defined on_click callbacks for this trace. If True,
            this callback is appended to the list of any previously defined
            callbacks.

        Returns
        -------
        None

        Examples
        --------

        >>> import plotly.graph_objects as go
        >>> from plotly.callbacks import Points, InputDeviceState
        >>> points, state = Points(), InputDeviceState()

        >>> def click_fn(trace, points, state):
        ...     inds = points.point_inds
        ...     # Do something

        >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
        >>> trace.on_click(click_fn)

        Note: The creation of the `points` and `state` objects is optional,
        it's simply a convenience to help the text editor perform completion
        on the arguments inside `click_fn`
        """
        pass

    def _dispatch_on_click(self, points, state):
        """
        Dispatch points and device state all all hover callbacks
        """
        pass

    # Select
    # ------
    def on_selection(self, callback, append=False):
        """
        Register function to be called when the user selects one or more
        points in this trace.

        Note: Callbacks will only be triggered when the trace belongs to a
        instance of plotly.graph_objs.FigureWidget and it is displayed in an
        ipywidget context. Callbacks will not be triggered on figures
        that are displayed using plot/iplot.

        Parameters
        ----------
        callback
            Callable function that accepts 4 arguments

            - this trace
            - plotly.callbacks.Points object
            - plotly.callbacks.BoxSelector or plotly.callbacks.LassoSelector

        append : bool
            If False (the default), this callback replaces any previously
            defined on_selection callbacks for this trace. If True,
            this callback is appended to the list of any previously defined
            callbacks.

        Returns
        -------
        None

        Examples
        --------

        >>> import plotly.graph_objects as go
        >>> from plotly.callbacks import Points
        >>> points = Points()

        >>> def selection_fn(trace, points, selector):
        ...     inds = points.point_inds
        ...     # Do something

        >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
        >>> trace.on_selection(selection_fn)

        Note: The creation of the `points` object is optional,
        it's simply a convenience to help the text editor perform completion
        on the `points` arguments inside `selection_fn`
        """
        pass

    def _dispatch_on_selection(self, points, selector):
        """
        Dispatch points and selector info to selection callbacks
        """
        pass

    # deselect
    # --------
    def on_deselect(self, callback, append=False):
        """
        Register function to be called when the user deselects points
        in this trace using doubleclick.

        Note: Callbacks will only be triggered when the trace belongs to a
        instance of plotly.graph_objs.FigureWidget and it is displayed in an
        ipywidget context. Callbacks will not be triggered on figures
        that are displayed using plot/iplot.

        Parameters
        ----------
        callback
            Callable function that accepts 3 arguments

            - this trace
            - plotly.callbacks.Points object

        append : bool
            If False (the default), this callback replaces any previously
            defined on_deselect callbacks for this trace. If True,
            this callback is appended to the list of any previously defined
            callbacks.

        Returns
        -------
        None

        Examples
        --------

        >>> import plotly.graph_objects as go
        >>> from plotly.callbacks import Points
        >>> points = Points()

        >>> def deselect_fn(trace, points):
        ...     inds = points.point_inds
        ...     # Do something

        >>> trace = go.Scatter(x=[1, 2], y=[3, 0])
        >>> trace.on_deselect(deselect_fn)

        Note: The creation of the `points` object is optional,
        it's simply a convenience to help the text editor perform completion
        on the `points` arguments inside `selection_fn`
        """
        pass

    def _dispatch_on_deselect(self, points):
        """
        Dispatch points info to deselection callbacks
        """
        pass


class BaseFrameHierarchyType(BasePlotlyType):
    """
    Base class for all types in the trace hierarchy
    """

    def __init__(self, plotly_name, **kwargs):
        super(BaseFrameHierarchyType, self).__init__(plotly_name, **kwargs)

    def _send_prop_set(self, prop_path_str, val):
        # Note: Frames are not supported by FigureWidget, and updates are not
        # propagated to parents
        pass

    def _restyle_child(self, child, key_path_str, val):
        # Note: Frames are not supported by FigureWidget, and updates are not
        # propagated to parents
        pass

    def on_change(self, callback, *args):
        raise NotImplementedError("Change callbacks are not supported on Frames")

    def _get_child_props(self, child):
        """
        Return the properties dict for a child trace or child layout

        Note: this method must match the name/signature of one on
        BasePlotlyType

        Parameters
        ----------
        child : BaseTraceType | BaseLayoutType

        Returns
        -------
        dict
        """
        pass
