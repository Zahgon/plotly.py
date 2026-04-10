#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Currentvalue(_BaseLayoutHierarchyType):
    _parent_path_str = "layout.slider"
    _path_str = "layout.slider.currentvalue"
    _valid_props = {"font", "offset", "prefix", "suffix", "visible", "xanchor"}

    @property
    def font(self):
        """
        Sets the font of the current value label text.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.currentvalue.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.currentvalue.Font
        """
        pass


    @property
    def offset(self):
        """
        The amount of space, in pixels, between the current value label
        and the slider.

        The 'offset' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def prefix(self):
        """
        When currentvalue.visible is true, this sets the prefix of the
        label.

        The 'prefix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def suffix(self):
        """
        When currentvalue.visible is true, this sets the suffix of the
        label.

        The 'suffix' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def visible(self):
        """
        Shows the currently-selected value above the slider.

        The 'visible' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def xanchor(self):
        """
        The alignment of the value readout relative to the length of
        the slider.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['left', 'center', 'right']

        Returns
        -------
        Any
        """
        pass



    def __init__(
        self,
        arg=None,
        font=None,
        offset=None,
        prefix=None,
        suffix=None,
        visible=None,
        xanchor=None,
        **kwargs,
    ):
        """
        Construct a new Currentvalue object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.slider.Currentvalue`
        font
            Sets the font of the current value label text.
        offset
            The amount of space, in pixels, between the current
            value label and the slider.
        prefix
            When currentvalue.visible is true, this sets the prefix
            of the label.
        suffix
            When currentvalue.visible is true, this sets the suffix
            of the label.
        visible
            Shows the currently-selected value above the slider.
        xanchor
            The alignment of the value readout relative to the
            length of the slider.

        Returns
        -------
        Currentvalue
        """
        super().__init__("currentvalue")
        if "_parent" in kwargs:
            self._parent = kwargs["_parent"]
            return

        if arg is None:
            arg = {}
        elif isinstance(arg, self.__class__):
            arg = arg.to_plotly_json()
        elif isinstance(arg, dict):
            arg = _copy.copy(arg)
        else:
            raise ValueError("""\
The first argument to the plotly.graph_objs.layout.slider.Currentvalue
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.slider.Currentvalue`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("font", arg, font)
        self._set_property("offset", arg, offset)
        self._set_property("prefix", arg, prefix)
        self._set_property("suffix", arg, suffix)
        self._set_property("visible", arg, visible)
        self._set_property("xanchor", arg, xanchor)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
