#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceHierarchyType as _BaseTraceHierarchyType
import copy as _copy


class Link(_BaseTraceHierarchyType):
    _parent_path_str = "sankey"
    _path_str = "sankey.link"
    _valid_props = {
        "arrowlen",
        "color",
        "colorscaledefaults",
        "colorscales",
        "colorsrc",
        "customdata",
        "customdatasrc",
        "hovercolor",
        "hovercolorsrc",
        "hoverinfo",
        "hoverlabel",
        "hovertemplate",
        "hovertemplatefallback",
        "hovertemplatesrc",
        "label",
        "labelsrc",
        "line",
        "source",
        "sourcesrc",
        "target",
        "targetsrc",
        "value",
        "valuesrc",
    }

    @property
    def arrowlen(self):
        """
        Sets the length (in px) of the links arrow, if 0 no arrow will
        be drawn.

        The 'arrowlen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def color(self):
        """
        Sets the `link` color. It can be a single value, or an array
        for specifying color for each `link`. If `link.color` is
        omitted, then by default, a translucent grey link will be used.

        The 'color' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color: see https://plotly.com/python/css-colors/ for a list
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def colorscales(self):
        """
        The 'colorscales' property is a tuple of instances of
        Colorscale that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.sankey.link.Colorscale
          - A list or tuple of dicts of string/value properties that
            will be passed to the Colorscale constructor

        Returns
        -------
        tuple[plotly.graph_objs.sankey.link.Colorscale]
        """
        pass


    @property
    def colorscaledefaults(self):
        """
        When used in a template (as
        layout.template.data.sankey.link.colorscaledefaults), sets the
        default property values to use for elements of
        sankey.link.colorscales

        The 'colorscaledefaults' property is an instance of Colorscale
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Colorscale`
          - A dict of string/value properties that will be passed
            to the Colorscale constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Colorscale
        """
        pass


    @property
    def colorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `color`.

        The 'colorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def customdata(self):
        """
        Assigns extra data to each link.

        The 'customdata' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def customdatasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `customdata`.

        The 'customdatasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def hovercolor(self):
        """
        Sets the `link` hover color. It can be a single value, or an
        array for specifying hover colors for each `link`. If
        `link.hovercolor` is omitted, then by default, links will
        become slightly more opaque when hovered over.

        The 'hovercolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color: see https://plotly.com/python/css-colors/ for a list
          - A list or array of any of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def hovercolorsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovercolor`.

        The 'hovercolorsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def hoverinfo(self):
        """
        Determines which trace information appear when hovering links.
        If `none` or `skip` are set, no information is displayed upon
        hovering. But, if `none` is set, click and hover events are
        still fired.

        The 'hoverinfo' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['all', 'none', 'skip']

        Returns
        -------
        Any
        """
        pass


    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Hoverlabel
        """
        pass


    @property
    def hovertemplate(self):
        """
        Template string used for rendering the information that appear
        on hover box. Note that this will override `hoverinfo`.
        Variables are inserted using %{variable}, for example "y: %{y}"
        as well as %{xother}, {%_xother}, {%_xother_}, {%xother_}. When
        showing info for several points, "xother" will be added to
        those with different x positions from the first point. An
        underscore before or after "(x|y)other" will add a space on
        that side, only when this field is shown. Numbers are formatted
        using d3-format's syntax %{variable:d3-format}, for example
        "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. Variables that can't be found will be
        replaced with the specifier. For example, a template of "data:
        %{x}, %{y}" will result in a value of "data: 1, %{y}" if x is 1
        and y is missing. Variables with an undefined value will be
        replaced with the fallback value. The variables available in
        `hovertemplate` are the ones emitted as event data described at
        this link https://plotly.com/javascript/plotlyjs-events/#event-
        data. Additionally, all attributes that can be specified per-
        point (the ones that are `arrayOk: true`) are available.
        Finally, the template string has access to variables `value`
        and `label`. Anything contained in tag `<extra>` is displayed
        in the secondary box, for example
        `<extra>%{fullData.name}</extra>`. To hide the secondary box
        completely, use an empty tag `<extra></extra>`.

        The 'hovertemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def hovertemplatefallback(self):
        """
        Fallback string that's displayed when a variable referenced in
        a template is missing. If the boolean value 'false' is passed
        in, the specifier with the missing variable will be displayed.

        The 'hovertemplatefallback' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def hovertemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertemplate`.

        The 'hovertemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def label(self):
        """
        The shown name of the link.

        The 'label' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def labelsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `label`.

        The 'labelsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.sankey.link.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.sankey.link.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def source(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        source node.

        The 'source' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def sourcesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `source`.

        The 'sourcesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def target(self):
        """
        An integer number `[0..nodes.length - 1]` that represents the
        target node.

        The 'target' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def targetsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `target`.

        The 'targetsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def value(self):
        """
        A numeric value representing the flow volume value.

        The 'value' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def valuesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `value`.

        The 'valuesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass



    def __init__(
        self,
        arg=None,
        arrowlen=None,
        color=None,
        colorscales=None,
        colorscaledefaults=None,
        colorsrc=None,
        customdata=None,
        customdatasrc=None,
        hovercolor=None,
        hovercolorsrc=None,
        hoverinfo=None,
        hoverlabel=None,
        hovertemplate=None,
        hovertemplatefallback=None,
        hovertemplatesrc=None,
        label=None,
        labelsrc=None,
        line=None,
        source=None,
        sourcesrc=None,
        target=None,
        targetsrc=None,
        value=None,
        valuesrc=None,
        **kwargs,
    ):
        """
        Construct a new Link object

        The links of the Sankey plot.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.sankey.Link`
        arrowlen
            Sets the length (in px) of the links arrow, if 0 no
            arrow will be drawn.
        color
            Sets the `link` color. It can be a single value, or an
            array for specifying color for each `link`. If
            `link.color` is omitted, then by default, a translucent
            grey link will be used.
        colorscales
            A tuple of
            :class:`plotly.graph_objects.sankey.link.Colorscale`
            instances or dicts with compatible properties
        colorscaledefaults
            When used in a template (as
            layout.template.data.sankey.link.colorscaledefaults),
            sets the default property values to use for elements of
            sankey.link.colorscales
        colorsrc
            Sets the source reference on Chart Studio Cloud for
            `color`.
        customdata
            Assigns extra data to each link.
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        hovercolor
            Sets the `link` hover color. It can be a single value,
            or an array for specifying hover colors for each
            `link`. If `link.hovercolor` is omitted, then by
            default, links will become slightly more opaque when
            hovered over.
        hovercolorsrc
            Sets the source reference on Chart Studio Cloud for
            `hovercolor`.
        hoverinfo
            Determines which trace information appear when hovering
            links. If `none` or `skip` are set, no information is
            displayed upon hovering. But, if `none` is set, click
            and hover events are still fired.
        hoverlabel
            :class:`plotly.graph_objects.sankey.link.Hoverlabel`
            instance or dict with compatible properties
        hovertemplate
            Template string used for rendering the information that
            appear on hover box. Note that this will override
            `hoverinfo`. Variables are inserted using %{variable},
            for example "y: %{y}" as well as %{xother}, {%_xother},
            {%_xother_}, {%xother_}. When showing info for several
            points, "xother" will be added to those with different
            x positions from the first point. An underscore before
            or after "(x|y)other" will add a space on that side,
            only when this field is shown. Numbers are formatted
            using d3-format's syntax %{variable:d3-format}, for
            example "Price: %{y:$.2f}".
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format
            for details on the formatting syntax. Dates are
            formatted using d3-time-format's syntax
            %{variable|d3-time-format}, for example "Day:
            %{2019-01-01|%A}". https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format for details on the
            date formatting syntax. Variables that can't be found
            will be replaced with the specifier. For example, a
            template of "data: %{x}, %{y}" will result in a value
            of "data: 1, %{y}" if x is 1 and y is missing.
            Variables with an undefined value will be replaced with
            the fallback value. The variables available in
            `hovertemplate` are the ones emitted as event data
            described at this link
            https://plotly.com/javascript/plotlyjs-events/#event-
            data. Additionally, all attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.  Finally, the template string has access
            to variables `value` and `label`. Anything contained in
            tag `<extra>` is displayed in the secondary box, for
            example `<extra>%{fullData.name}</extra>`. To hide the
            secondary box completely, use an empty tag
            `<extra></extra>`.
        hovertemplatefallback
            Fallback string that's displayed when a variable
            referenced in a template is missing. If the boolean
            value 'false' is passed in, the specifier with the
            missing variable will be displayed.
        hovertemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `hovertemplate`.
        label
            The shown name of the link.
        labelsrc
            Sets the source reference on Chart Studio Cloud for
            `label`.
        line
            :class:`plotly.graph_objects.sankey.link.Line` instance
            or dict with compatible properties
        source
            An integer number `[0..nodes.length - 1]` that
            represents the source node.
        sourcesrc
            Sets the source reference on Chart Studio Cloud for
            `source`.
        target
            An integer number `[0..nodes.length - 1]` that
            represents the target node.
        targetsrc
            Sets the source reference on Chart Studio Cloud for
            `target`.
        value
            A numeric value representing the flow volume value.
        valuesrc
            Sets the source reference on Chart Studio Cloud for
            `value`.

        Returns
        -------
        Link
        """
        super().__init__("link")
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
The first argument to the plotly.graph_objs.sankey.Link
constructor must be a dict or
an instance of :class:`plotly.graph_objs.sankey.Link`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("arrowlen", arg, arrowlen)
        self._set_property("color", arg, color)
        self._set_property("colorscales", arg, colorscales)
        self._set_property("colorscaledefaults", arg, colorscaledefaults)
        self._set_property("colorsrc", arg, colorsrc)
        self._set_property("customdata", arg, customdata)
        self._set_property("customdatasrc", arg, customdatasrc)
        self._set_property("hovercolor", arg, hovercolor)
        self._set_property("hovercolorsrc", arg, hovercolorsrc)
        self._set_property("hoverinfo", arg, hoverinfo)
        self._set_property("hoverlabel", arg, hoverlabel)
        self._set_property("hovertemplate", arg, hovertemplate)
        self._set_property("hovertemplatefallback", arg, hovertemplatefallback)
        self._set_property("hovertemplatesrc", arg, hovertemplatesrc)
        self._set_property("label", arg, label)
        self._set_property("labelsrc", arg, labelsrc)
        self._set_property("line", arg, line)
        self._set_property("source", arg, source)
        self._set_property("sourcesrc", arg, sourcesrc)
        self._set_property("target", arg, target)
        self._set_property("targetsrc", arg, targetsrc)
        self._set_property("value", arg, value)
        self._set_property("valuesrc", arg, valuesrc)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
