#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseTraceType as _BaseTraceType
import copy as _copy


class Scatter(_BaseTraceType):
    _parent_path_str = ""
    _path_str = "scatter"
    _valid_props = {
        "alignmentgroup",
        "cliponaxis",
        "connectgaps",
        "customdata",
        "customdatasrc",
        "dx",
        "dy",
        "error_x",
        "error_y",
        "fill",
        "fillcolor",
        "fillgradient",
        "fillpattern",
        "groupnorm",
        "hoverinfo",
        "hoverinfosrc",
        "hoverlabel",
        "hoveron",
        "hovertemplate",
        "hovertemplatefallback",
        "hovertemplatesrc",
        "hovertext",
        "hovertextsrc",
        "ids",
        "idssrc",
        "legend",
        "legendgroup",
        "legendgrouptitle",
        "legendrank",
        "legendwidth",
        "line",
        "marker",
        "meta",
        "metasrc",
        "mode",
        "name",
        "offsetgroup",
        "opacity",
        "orientation",
        "selected",
        "selectedpoints",
        "showlegend",
        "stackgaps",
        "stackgroup",
        "stream",
        "text",
        "textfont",
        "textposition",
        "textpositionsrc",
        "textsrc",
        "texttemplate",
        "texttemplatefallback",
        "texttemplatesrc",
        "type",
        "uid",
        "uirevision",
        "unselected",
        "visible",
        "x",
        "x0",
        "xaxis",
        "xcalendar",
        "xhoverformat",
        "xperiod",
        "xperiod0",
        "xperiodalignment",
        "xsrc",
        "y",
        "y0",
        "yaxis",
        "ycalendar",
        "yhoverformat",
        "yperiod",
        "yperiod0",
        "yperiodalignment",
        "ysrc",
        "zorder",
    }

    @property
    def alignmentgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same alignmentgroup. This controls whether bars
        compute their positional range dependently or independently.

        The 'alignmentgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def cliponaxis(self):
        """
        Determines whether or not markers and text nodes are clipped
        about the subplot axes. To show markers and text nodes above
        axis lines and tick labels, make sure to set `xaxis.layer` and
        `yaxis.layer` to *below traces*.

        The 'cliponaxis' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def connectgaps(self):
        """
        Determines whether or not gaps (i.e. {nan} or missing values)
        in the provided data arrays are connected.

        The 'connectgaps' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def customdata(self):
        """
        Assigns extra data each datum. This may be useful when
        listening to hover, click and selection events. Note that,
        "scatter" traces also appends customdata items in the markers
        DOM elements

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
    def dx(self):
        """
        Sets the x coordinate step. See `x0` for more info.

        The 'dx' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def dy(self):
        """
        Sets the y coordinate step. See `y0` for more info.

        The 'dy' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def error_x(self):
        """
        The 'error_x' property is an instance of ErrorX
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.ErrorX`
          - A dict of string/value properties that will be passed
            to the ErrorX constructor

        Returns
        -------
        plotly.graph_objs.scatter.ErrorX
        """
        pass


    @property
    def error_y(self):
        """
        The 'error_y' property is an instance of ErrorY
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.ErrorY`
          - A dict of string/value properties that will be passed
            to the ErrorY constructor

        Returns
        -------
        plotly.graph_objs.scatter.ErrorY
        """
        pass


    @property
    def fill(self):
        """
        Sets the area to fill with a solid color. Defaults to "none"
        unless this trace is stacked, then it gets "tonexty"
        ("tonextx") if `orientation` is "v" ("h") Use with `fillcolor`
        if not "none". "tozerox" and "tozeroy" fill to x=0 and y=0
        respectively. "tonextx" and "tonexty" fill between the
        endpoints of this trace and the endpoints of the trace before
        it, connecting those endpoints with straight lines (to make a
        stacked area graph); if there is no trace before it, they
        behave like "tozerox" and "tozeroy". "toself" connects the
        endpoints of the trace (or each segment of the trace if it has
        gaps) into a closed shape. "tonext" fills the space between two
        traces if one completely encloses the other (eg consecutive
        contour lines), and behaves like "toself" if there is no trace
        before it. "tonext" should not be used if one trace does not
        enclose the other. Traces in a `stackgroup` will only fill to
        (or be filled to) other traces in the same group. With multiple
        `stackgroup`s or some traces stacked and some not, if fill-
        linked traces are not already consecutive, the later ones will
        be pushed down in the drawing order.

        The 'fill' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['none', 'tozeroy', 'tozerox', 'tonexty', 'tonextx',
                'toself', 'tonext']

        Returns
        -------
        Any
        """
        return self["fill"]

    @fill.setter
    def fill(self, val):
        self["fill"] = val

    @property
    def fillcolor(self):
        """
        Sets the fill color. Defaults to a half-transparent variant of
        the line color, marker color, or marker line color, whichever
        is available. If fillgradient is specified, fillcolor is
        ignored except for setting the background color of the hover
        label, if any.

        The 'fillcolor' property is a color and may be specified as:
          - A hex string (e.g. '#ff0000')
          - An rgb/rgba string (e.g. 'rgb(255,0,0)')
          - An hsl/hsla string (e.g. 'hsl(0,100%,50%)')
          - An hsv/hsva string (e.g. 'hsv(0,100%,100%)')
          - A named CSS color: see https://plotly.com/python/css-colors/ for a list

        Returns
        -------
        str
        """
        pass


    @property
    def fillgradient(self):
        """
        Sets a fill gradient. If not specified, the fillcolor is used
        instead.

        The 'fillgradient' property is an instance of Fillgradient
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Fillgradient`
          - A dict of string/value properties that will be passed
            to the Fillgradient constructor

        Returns
        -------
        plotly.graph_objs.scatter.Fillgradient
        """
        pass


    @property
    def fillpattern(self):
        """
        Sets the pattern within the marker.

        The 'fillpattern' property is an instance of Fillpattern
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Fillpattern`
          - A dict of string/value properties that will be passed
            to the Fillpattern constructor

        Returns
        -------
        plotly.graph_objs.scatter.Fillpattern
        """
        pass


    @property
    def groupnorm(self):
        """
        Only relevant when `stackgroup` is used, and only the first
        `groupnorm` found in the `stackgroup` will be used - including
        if `visible` is "legendonly" but not if it is `false`. Sets the
        normalization for the sum of this `stackgroup`. With
        "fraction", the value of each trace at each location is divided
        by the sum of all trace values at that location. "percent" is
        the same but multiplied by 100 to show percentages. If there
        are multiple subplots, or multiple `stackgroup`s on one
        subplot, each will be normalized within its own set.

        The 'groupnorm' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['', 'fraction', 'percent']

        Returns
        -------
        Any
        """
        pass


    @property
    def hoverinfo(self):
        """
        Determines which trace information appear on hover. If `none`
        or `skip` are set, no information is displayed upon hovering.
        But, if `none` is set, click and hover events are still fired.

        The 'hoverinfo' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['x', 'y', 'z', 'text', 'name'] joined with '+' characters
            (e.g. 'x+y')
            OR exactly one of ['all', 'none', 'skip'] (e.g. 'skip')
          - A list or array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        pass


    @property
    def hoverinfosrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hoverinfo`.

        The 'hoverinfosrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def hoverlabel(self):
        """
        The 'hoverlabel' property is an instance of Hoverlabel
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Hoverlabel`
          - A dict of string/value properties that will be passed
            to the Hoverlabel constructor

        Returns
        -------
        plotly.graph_objs.scatter.Hoverlabel
        """
        pass


    @property
    def hoveron(self):
        """
        Do the hover effects highlight individual points (markers or
        line points) or do they highlight filled regions? If the fill
        is "toself" or "tonext" and there are no markers or text, then
        the default is "fills", otherwise it is "points".

        The 'hoveron' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['points', 'fills'] joined with '+' characters
            (e.g. 'points+fills')

        Returns
        -------
        Any
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
        Anything contained in tag `<extra>` is displayed in the
        secondary box, for example `<extra>%{fullData.name}</extra>`.
        To hide the secondary box completely, use an empty tag
        `<extra></extra>`.

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
    def hovertext(self):
        """
        Sets hover text elements associated with each (x,y) pair. If a
        single string, the same string appears over all the data
        points. If an array of string, the items are mapped in order to
        the this trace's (x,y) coordinates. To be seen, trace
        `hoverinfo` must contain a "text" flag.

        The 'hovertext' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def hovertextsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `hovertext`.

        The 'hovertextsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def ids(self):
        """
        Assigns id labels to each datum. These ids for object constancy
        of data points during animation. Should be an array of strings,
        not numbers or any other type.

        The 'ids' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def idssrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `ids`.

        The 'idssrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def legend(self):
        """
        Sets the reference to a legend to show this trace in.
        References to these legends are "legend", "legend2", "legend3",
        etc. Settings for these legends are set in the layout, under
        `layout.legend`, `layout.legend2`, etc.

        The 'legend' property is an identifier of a particular
        subplot, of type 'legend', that may be specified as:
          - the string 'legend' optionally followed by an integer >= 1
            (e.g. 'legend', 'legend1', 'legend2', 'legend3', etc.)

        Returns
        -------
        str
        """
        pass


    @property
    def legendgroup(self):
        """
        Sets the legend group for this trace. Traces and shapes part of
        the same legend group hide/show at the same time when toggling
        legend items.

        The 'legendgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def legendgrouptitle(self):
        """
        The 'legendgrouptitle' property is an instance of Legendgrouptitle
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Legendgrouptitle`
          - A dict of string/value properties that will be passed
            to the Legendgrouptitle constructor

        Returns
        -------
        plotly.graph_objs.scatter.Legendgrouptitle
        """
        pass


    @property
    def legendrank(self):
        """
        Sets the legend rank for this trace. Items and groups with
        smaller ranks are presented on top/left side while with
        "reversed" `legend.traceorder` they are on bottom/right side.
        The default legendrank is 1000, so that you can use ranks less
        than 1000 to place certain items before all unranked items, and
        ranks greater than 1000 to go after all unranked items. When
        having unranked or equal rank items shapes would be displayed
        after traces i.e. according to their order in data and layout.

        The 'legendrank' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def legendwidth(self):
        """
        Sets the width (in px or fraction) of the legend for this
        trace.

        The 'legendwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def line(self):
        """
        The 'line' property is an instance of Line
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Line`
          - A dict of string/value properties that will be passed
            to the Line constructor

        Returns
        -------
        plotly.graph_objs.scatter.Line
        """
        return self["line"]

    @line.setter
    def line(self, val):
        self["line"] = val

    @property
    def marker(self):
        """
        The 'marker' property is an instance of Marker
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Marker`
          - A dict of string/value properties that will be passed
            to the Marker constructor

        Returns
        -------
        plotly.graph_objs.scatter.Marker
        """
        pass


    @property
    def meta(self):
        """
        Assigns extra meta information associated with this trace that
        can be used in various text attributes. Attributes such as
        trace `name`, graph, axis and colorbar `title.text`, annotation
        `text` `rangeselector`, `updatemenues` and `sliders` `label`
        text all support `meta`. To access the trace `meta` values in
        an attribute in the same trace, simply use `%{meta[i]}` where
        `i` is the index or key of the `meta` item in question. To
        access trace `meta` in layout attributes, use
        `%{data[n[.meta[i]}` where `i` is the index or key of the
        `meta` and `n` is the trace index.

        The 'meta' property accepts values of any type

        Returns
        -------
        Any|numpy.ndarray
        """
        pass


    @property
    def metasrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `meta`.

        The 'metasrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def mode(self):
        """
        Determines the drawing mode for this scatter trace. If the
        provided `mode` includes "text" then the `text` elements appear
        at the coordinates. Otherwise, the `text` elements appear on
        hover. If there are less than 20 points and the trace is not
        stacked then the default is "lines+markers". Otherwise,
        "lines".

        The 'mode' property is a flaglist and may be specified
        as a string containing:
          - Any combination of ['lines', 'markers', 'text'] joined with '+' characters
            (e.g. 'lines+markers')
            OR exactly one of ['none'] (e.g. 'none')

        Returns
        -------
        Any
        """
        pass


    @property
    def name(self):
        """
        Sets the trace name. The trace name appears as the legend item
        and on hover.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def offsetgroup(self):
        """
        Set several traces linked to the same position axis or matching
        axes to the same offsetgroup where bars of the same position
        coordinate will line up.

        The 'offsetgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def opacity(self):
        """
        Sets the opacity of the trace.

        The 'opacity' property is a number and may be specified as:
          - An int or float in the interval [0, 1]

        Returns
        -------
        int|float
        """
        pass


    @property
    def orientation(self):
        """
        Only relevant in the following cases: 1. when `scattermode` is
        set to "group". 2. when `stackgroup` is used, and only the
        first `orientation` found in the `stackgroup` will be used -
        including if `visible` is "legendonly" but not if it is
        `false`. Sets the stacking direction. With "v" ("h"), the y (x)
        values of subsequent traces are added. Also affects the default
        value of `fill`.

        The 'orientation' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['v', 'h']

        Returns
        -------
        Any
        """
        pass


    @property
    def selected(self):
        """
        The 'selected' property is an instance of Selected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Selected`
          - A dict of string/value properties that will be passed
            to the Selected constructor

        Returns
        -------
        plotly.graph_objs.scatter.Selected
        """
        pass


    @property
    def selectedpoints(self):
        """
        Array containing integer indices of selected points. Has an
        effect only for traces that support selections. Note that an
        empty array means an empty selection where the `unselected` are
        turned on for all points, whereas, any other non-array values
        means no selection all where the `selected` and `unselected`
        styles have no effect.

        The 'selectedpoints' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def showlegend(self):
        """
        Determines whether or not an item corresponding to this trace
        is shown in the legend.

        The 'showlegend' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def stackgaps(self):
        """
        Only relevant when `stackgroup` is used, and only the first
        `stackgaps` found in the `stackgroup` will be used - including
        if `visible` is "legendonly" but not if it is `false`.
        Determines how we handle locations at which other traces in
        this group have data but this one does not. With *infer zero*
        we insert a zero at these locations. With "interpolate" we
        linearly interpolate between existing values, and extrapolate a
        constant beyond the existing values.

        The 'stackgaps' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['infer zero', 'interpolate']

        Returns
        -------
        Any
        """
        pass


    @property
    def stackgroup(self):
        """
        Set several scatter traces (on the same subplot) to the same
        stackgroup in order to add their y values (or their x values if
        `orientation` is "h"). If blank or omitted this trace will not
        be stacked. Stacking also turns `fill` on by default, using
        "tonexty" ("tonextx") if `orientation` is "h" ("v") and sets
        the default `mode` to "lines" irrespective of point count. You
        can only stack on a numeric (linear or log) axis. Traces in a
        `stackgroup` will only fill to (or be filled to) other traces
        in the same group. With multiple `stackgroup`s or some traces
        stacked and some not, if fill-linked traces are not already
        consecutive, the later ones will be pushed down in the drawing
        order.

        The 'stackgroup' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def stream(self):
        """
        The 'stream' property is an instance of Stream
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Stream`
          - A dict of string/value properties that will be passed
            to the Stream constructor

        Returns
        -------
        plotly.graph_objs.scatter.Stream
        """
        pass


    @property
    def text(self):
        """
        Sets text elements associated with each (x,y) pair. If a single
        string, the same string appears over all the data points. If an
        array of string, the items are mapped in order to the this
        trace's (x,y) coordinates. If trace `hoverinfo` contains a
        "text" flag and "hovertext" is not set, these elements will be
        seen in the hover labels.

        The 'text' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def textfont(self):
        """
        Sets the text font.

        The 'textfont' property is an instance of Textfont
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Textfont`
          - A dict of string/value properties that will be passed
            to the Textfont constructor

        Returns
        -------
        plotly.graph_objs.scatter.Textfont
        """
        pass


    @property
    def textposition(self):
        """
        Sets the positions of the `text` elements with respects to the
        (x,y) coordinates.

        The 'textposition' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['top left', 'top center', 'top right', 'middle left',
                'middle center', 'middle right', 'bottom left', 'bottom
                center', 'bottom right']
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        Any|numpy.ndarray
        """
        pass


    @property
    def textpositionsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `textposition`.

        The 'textpositionsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def textsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `text`.

        The 'textsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def texttemplate(self):
        """
        Template string used for rendering the information text that
        appears on points. Note that this will override `textinfo`.
        Variables are inserted using %{variable}, for example "y:
        %{y}". Numbers are formatted using d3-format's syntax
        %{variable:d3-format}, for example "Price: %{y:$.2f}".
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format for
        details on the formatting syntax. Dates are formatted using
        d3-time-format's syntax %{variable|d3-time-format}, for example
        "Day: %{2019-01-01|%A}". https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format for details on the date
        formatting syntax. Variables that can't be found will be
        replaced with the specifier. For example, a template of "data:
        %{x}, %{y}" will result in a value of "data: 1, %{y}" if x is 1
        and y is missing. Variables with an undefined value will be
        replaced with the fallback value. All attributes that can be
        specified per-point (the ones that are `arrayOk: true`) are
        available.

        The 'texttemplate' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string
          - A tuple, list, or one-dimensional numpy array of the above

        Returns
        -------
        str|numpy.ndarray
        """
        pass


    @property
    def texttemplatefallback(self):
        """
        Fallback string that's displayed when a variable referenced in
        a template is missing. If the boolean value 'false' is passed
        in, the specifier with the missing variable will be displayed.

        The 'texttemplatefallback' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def texttemplatesrc(self):
        """
        Sets the source reference on Chart Studio Cloud for
        `texttemplate`.

        The 'texttemplatesrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def uid(self):
        """
        Assign an id to this trace, Use this to provide object
        constancy between traces during animations and transitions.

        The 'uid' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def uirevision(self):
        """
        Controls persistence of some user-driven changes to the trace:
        `constraintrange` in `parcoords` traces, as well as some
        `editable: true` modifications such as `name` and
        `colorbar.title`. Defaults to `layout.uirevision`. Note that
        other user-driven trace attribute changes are controlled by
        `layout` attributes: `trace.visible` is controlled by
        `layout.legend.uirevision`, `selectedpoints` is controlled by
        `layout.selectionrevision`, and `colorbar.(x|y)` (accessible
        with `config: {editable: true}`) is controlled by
        `layout.editrevision`. Trace changes are tracked by `uid`,
        which only falls back on trace index if no `uid` is provided.
        So if your app can add/remove traces before the end of the
        `data` array, such that the same trace has a different index,
        you can still preserve user-driven changes if you give each
        trace a `uid` that stays with it as it moves.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def unselected(self):
        """
        The 'unselected' property is an instance of Unselected
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.scatter.Unselected`
          - A dict of string/value properties that will be passed
            to the Unselected constructor

        Returns
        -------
        plotly.graph_objs.scatter.Unselected
        """
        pass


    @property
    def visible(self):
        """
        Determines whether or not this trace is visible. If
        "legendonly", the trace is not drawn, but can appear as a
        legend item (provided that the legend itself is visible).

        The 'visible' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [True, False, 'legendonly']

        Returns
        -------
        Any
        """
        pass


    @property
    def x(self):
        """
        Sets the x coordinates.

        The 'x' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def x0(self):
        """
        Alternate to `x`. Builds a linear space of x coordinates. Use
        with `dx` where `x0` is the starting coordinate and `dx` the
        step.

        The 'x0' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def xaxis(self):
        """
        Sets a reference between this trace's x coordinates and a 2D
        cartesian x axis. If "x" (the default value), the x coordinates
        refer to `layout.xaxis`. If "x2", the x coordinates refer to
        `layout.xaxis2`, and so on.

        The 'xaxis' property is an identifier of a particular
        subplot, of type 'x', that may be specified as:
          - the string 'x' optionally followed by an integer >= 1
            (e.g. 'x', 'x1', 'x2', 'x3', etc.)

        Returns
        -------
        str
        """
        pass


    @property
    def xcalendar(self):
        """
        Sets the calendar system to use with `x` date data.

        The 'xcalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['chinese', 'coptic', 'discworld', 'ethiopian',
                'gregorian', 'hebrew', 'islamic', 'jalali', 'julian',
                'mayan', 'nanakshahi', 'nepali', 'persian', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        pass


    @property
    def xhoverformat(self):
        """
        Sets the hover text formatting rulefor `x`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `xaxis.hoverformat`.

        The 'xhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def xperiod(self):
        """
        Only relevant when the axis `type` is "date". Sets the period
        positioning in milliseconds or "M<n>" on the x axis. Special
        values in the form of "M<n>" could be used to declare the
        number of months. In this case `n` must be a positive integer.

        The 'xperiod' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def xperiod0(self):
        """
        Only relevant when the axis `type` is "date". Sets the base for
        period positioning in milliseconds or date string on the x0
        axis. When `x0period` is round number of weeks, the `x0period0`
        by default would be on a Sunday i.e. 2000-01-02, otherwise it
        would be at 2000-01-01.

        The 'xperiod0' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def xperiodalignment(self):
        """
        Only relevant when the axis `type` is "date". Sets the
        alignment of data points on the x axis.

        The 'xperiodalignment' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'middle', 'end']

        Returns
        -------
        Any
        """
        pass


    @property
    def xsrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `x`.

        The 'xsrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def y(self):
        """
        Sets the y coordinates.

        The 'y' property is an array that may be specified as a tuple,
        list, numpy array, or pandas Series

        Returns
        -------
        numpy.ndarray
        """
        pass


    @property
    def y0(self):
        """
        Alternate to `y`. Builds a linear space of y coordinates. Use
        with `dy` where `y0` is the starting coordinate and `dy` the
        step.

        The 'y0' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def yaxis(self):
        """
        Sets a reference between this trace's y coordinates and a 2D
        cartesian y axis. If "y" (the default value), the y coordinates
        refer to `layout.yaxis`. If "y2", the y coordinates refer to
        `layout.yaxis2`, and so on.

        The 'yaxis' property is an identifier of a particular
        subplot, of type 'y', that may be specified as:
          - the string 'y' optionally followed by an integer >= 1
            (e.g. 'y', 'y1', 'y2', 'y3', etc.)

        Returns
        -------
        str
        """
        pass


    @property
    def ycalendar(self):
        """
        Sets the calendar system to use with `y` date data.

        The 'ycalendar' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['chinese', 'coptic', 'discworld', 'ethiopian',
                'gregorian', 'hebrew', 'islamic', 'jalali', 'julian',
                'mayan', 'nanakshahi', 'nepali', 'persian', 'taiwan',
                'thai', 'ummalqura']

        Returns
        -------
        Any
        """
        pass


    @property
    def yhoverformat(self):
        """
        Sets the hover text formatting rulefor `y`  using d3 formatting
        mini-languages which are very similar to those in Python. For
        numbers, see:
        https://github.com/d3/d3-format/tree/v1.4.5#d3-format. And for
        dates see: https://github.com/d3/d3-time-
        format/tree/v2.2.3#locale_format. We add two items to d3's date
        formatter: "%h" for half of the year as a decimal number as
        well as "%{n}f" for fractional seconds with n digits. For
        example, *2016-10-13 09:15:23.456* with tickformat
        "%H~%M~%S.%2f" would display *09~15~23.46*By default the values
        are formatted using `yaxis.hoverformat`.

        The 'yhoverformat' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def yperiod(self):
        """
        Only relevant when the axis `type` is "date". Sets the period
        positioning in milliseconds or "M<n>" on the y axis. Special
        values in the form of "M<n>" could be used to declare the
        number of months. In this case `n` must be a positive integer.

        The 'yperiod' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def yperiod0(self):
        """
        Only relevant when the axis `type` is "date". Sets the base for
        period positioning in milliseconds or date string on the y0
        axis. When `y0period` is round number of weeks, the `y0period0`
        by default would be on a Sunday i.e. 2000-01-02, otherwise it
        would be at 2000-01-01.

        The 'yperiod0' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def yperiodalignment(self):
        """
        Only relevant when the axis `type` is "date". Sets the
        alignment of data points on the y axis.

        The 'yperiodalignment' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['start', 'middle', 'end']

        Returns
        -------
        Any
        """
        pass


    @property
    def ysrc(self):
        """
        Sets the source reference on Chart Studio Cloud for `y`.

        The 'ysrc' property must be specified as a string or
        as a plotly.grid_objs.Column object

        Returns
        -------
        str
        """
        pass


    @property
    def zorder(self):
        """
        Sets the layer on which this trace is displayed, relative to
        other SVG traces on the same subplot. SVG traces with higher
        `zorder` appear in front of those with lower `zorder`.

        The 'zorder' property is a integer and may be specified as:
          - An int (or float that will be cast to an int)

        Returns
        -------
        int
        """
        pass




    def __init__(
        self,
        arg=None,
        alignmentgroup=None,
        cliponaxis=None,
        connectgaps=None,
        customdata=None,
        customdatasrc=None,
        dx=None,
        dy=None,
        error_x=None,
        error_y=None,
        fill=None,
        fillcolor=None,
        fillgradient=None,
        fillpattern=None,
        groupnorm=None,
        hoverinfo=None,
        hoverinfosrc=None,
        hoverlabel=None,
        hoveron=None,
        hovertemplate=None,
        hovertemplatefallback=None,
        hovertemplatesrc=None,
        hovertext=None,
        hovertextsrc=None,
        ids=None,
        idssrc=None,
        legend=None,
        legendgroup=None,
        legendgrouptitle=None,
        legendrank=None,
        legendwidth=None,
        line=None,
        marker=None,
        meta=None,
        metasrc=None,
        mode=None,
        name=None,
        offsetgroup=None,
        opacity=None,
        orientation=None,
        selected=None,
        selectedpoints=None,
        showlegend=None,
        stackgaps=None,
        stackgroup=None,
        stream=None,
        text=None,
        textfont=None,
        textposition=None,
        textpositionsrc=None,
        textsrc=None,
        texttemplate=None,
        texttemplatefallback=None,
        texttemplatesrc=None,
        uid=None,
        uirevision=None,
        unselected=None,
        visible=None,
        x=None,
        x0=None,
        xaxis=None,
        xcalendar=None,
        xhoverformat=None,
        xperiod=None,
        xperiod0=None,
        xperiodalignment=None,
        xsrc=None,
        y=None,
        y0=None,
        yaxis=None,
        ycalendar=None,
        yhoverformat=None,
        yperiod=None,
        yperiod0=None,
        yperiodalignment=None,
        ysrc=None,
        zorder=None,
        **kwargs,
    ):
        """
        Construct a new Scatter object

        The scatter trace type encompasses line charts, scatter charts,
        text charts, and bubble charts. The data visualized as scatter
        point or lines is set in `x` and `y`. Text (appearing either on
        the chart or on hover only) is via `text`. Bubble charts are
        achieved by setting `marker.size` and/or `marker.color` to
        numerical arrays.

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.Scatter`
        alignmentgroup
            Set several traces linked to the same position axis or
            matching axes to the same alignmentgroup. This controls
            whether bars compute their positional range dependently
            or independently.
        cliponaxis
            Determines whether or not markers and text nodes are
            clipped about the subplot axes. To show markers and
            text nodes above axis lines and tick labels, make sure
            to set `xaxis.layer` and `yaxis.layer` to *below
            traces*.
        connectgaps
            Determines whether or not gaps (i.e. {nan} or missing
            values) in the provided data arrays are connected.
        customdata
            Assigns extra data each datum. This may be useful when
            listening to hover, click and selection events. Note
            that, "scatter" traces also appends customdata items in
            the markers DOM elements
        customdatasrc
            Sets the source reference on Chart Studio Cloud for
            `customdata`.
        dx
            Sets the x coordinate step. See `x0` for more info.
        dy
            Sets the y coordinate step. See `y0` for more info.
        error_x
            :class:`plotly.graph_objects.scatter.ErrorX` instance
            or dict with compatible properties
        error_y
            :class:`plotly.graph_objects.scatter.ErrorY` instance
            or dict with compatible properties
        fill
            Sets the area to fill with a solid color. Defaults to
            "none" unless this trace is stacked, then it gets
            "tonexty" ("tonextx") if `orientation` is "v" ("h") Use
            with `fillcolor` if not "none". "tozerox" and "tozeroy"
            fill to x=0 and y=0 respectively. "tonextx" and
            "tonexty" fill between the endpoints of this trace and
            the endpoints of the trace before it, connecting those
            endpoints with straight lines (to make a stacked area
            graph); if there is no trace before it, they behave
            like "tozerox" and "tozeroy". "toself" connects the
            endpoints of the trace (or each segment of the trace if
            it has gaps) into a closed shape. "tonext" fills the
            space between two traces if one completely encloses the
            other (eg consecutive contour lines), and behaves like
            "toself" if there is no trace before it. "tonext"
            should not be used if one trace does not enclose the
            other. Traces in a `stackgroup` will only fill to (or
            be filled to) other traces in the same group. With
            multiple `stackgroup`s or some traces stacked and some
            not, if fill-linked traces are not already consecutive,
            the later ones will be pushed down in the drawing
            order.
        fillcolor
            Sets the fill color. Defaults to a half-transparent
            variant of the line color, marker color, or marker line
            color, whichever is available. If fillgradient is
            specified, fillcolor is ignored except for setting the
            background color of the hover label, if any.
        fillgradient
            Sets a fill gradient. If not specified, the fillcolor
            is used instead.
        fillpattern
            Sets the pattern within the marker.
        groupnorm
            Only relevant when `stackgroup` is used, and only the
            first `groupnorm` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Sets the normalization for the sum of
            this `stackgroup`. With "fraction", the value of each
            trace at each location is divided by the sum of all
            trace values at that location. "percent" is the same
            but multiplied by 100 to show percentages. If there are
            multiple subplots, or multiple `stackgroup`s on one
            subplot, each will be normalized within its own set.
        hoverinfo
            Determines which trace information appear on hover. If
            `none` or `skip` are set, no information is displayed
            upon hovering. But, if `none` is set, click and hover
            events are still fired.
        hoverinfosrc
            Sets the source reference on Chart Studio Cloud for
            `hoverinfo`.
        hoverlabel
            :class:`plotly.graph_objects.scatter.Hoverlabel`
            instance or dict with compatible properties
        hoveron
            Do the hover effects highlight individual points
            (markers or line points) or do they highlight filled
            regions? If the fill is "toself" or "tonext" and there
            are no markers or text, then the default is "fills",
            otherwise it is "points".
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
            are available.  Anything contained in tag `<extra>` is
            displayed in the secondary box, for example
            `<extra>%{fullData.name}</extra>`. To hide the
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
        hovertext
            Sets hover text elements associated with each (x,y)
            pair. If a single string, the same string appears over
            all the data points. If an array of string, the items
            are mapped in order to the this trace's (x,y)
            coordinates. To be seen, trace `hoverinfo` must contain
            a "text" flag.
        hovertextsrc
            Sets the source reference on Chart Studio Cloud for
            `hovertext`.
        ids
            Assigns id labels to each datum. These ids for object
            constancy of data points during animation. Should be an
            array of strings, not numbers or any other type.
        idssrc
            Sets the source reference on Chart Studio Cloud for
            `ids`.
        legend
            Sets the reference to a legend to show this trace in.
            References to these legends are "legend", "legend2",
            "legend3", etc. Settings for these legends are set in
            the layout, under `layout.legend`, `layout.legend2`,
            etc.
        legendgroup
            Sets the legend group for this trace. Traces and shapes
            part of the same legend group hide/show at the same
            time when toggling legend items.
        legendgrouptitle
            :class:`plotly.graph_objects.scatter.Legendgrouptitle`
            instance or dict with compatible properties
        legendrank
            Sets the legend rank for this trace. Items and groups
            with smaller ranks are presented on top/left side while
            with "reversed" `legend.traceorder` they are on
            bottom/right side. The default legendrank is 1000, so
            that you can use ranks less than 1000 to place certain
            items before all unranked items, and ranks greater than
            1000 to go after all unranked items. When having
            unranked or equal rank items shapes would be displayed
            after traces i.e. according to their order in data and
            layout.
        legendwidth
            Sets the width (in px or fraction) of the legend for
            this trace.
        line
            :class:`plotly.graph_objects.scatter.Line` instance or
            dict with compatible properties
        marker
            :class:`plotly.graph_objects.scatter.Marker` instance
            or dict with compatible properties
        meta
            Assigns extra meta information associated with this
            trace that can be used in various text attributes.
            Attributes such as trace `name`, graph, axis and
            colorbar `title.text`, annotation `text`
            `rangeselector`, `updatemenues` and `sliders` `label`
            text all support `meta`. To access the trace `meta`
            values in an attribute in the same trace, simply use
            `%{meta[i]}` where `i` is the index or key of the
            `meta` item in question. To access trace `meta` in
            layout attributes, use `%{data[n[.meta[i]}` where `i`
            is the index or key of the `meta` and `n` is the trace
            index.
        metasrc
            Sets the source reference on Chart Studio Cloud for
            `meta`.
        mode
            Determines the drawing mode for this scatter trace. If
            the provided `mode` includes "text" then the `text`
            elements appear at the coordinates. Otherwise, the
            `text` elements appear on hover. If there are less than
            20 points and the trace is not stacked then the default
            is "lines+markers". Otherwise, "lines".
        name
            Sets the trace name. The trace name appears as the
            legend item and on hover.
        offsetgroup
            Set several traces linked to the same position axis or
            matching axes to the same offsetgroup where bars of the
            same position coordinate will line up.
        opacity
            Sets the opacity of the trace.
        orientation
            Only relevant in the following cases: 1. when
            `scattermode` is set to "group". 2. when `stackgroup`
            is used, and only the first `orientation` found in the
            `stackgroup` will be used - including if `visible` is
            "legendonly" but not if it is `false`. Sets the
            stacking direction. With "v" ("h"), the y (x) values of
            subsequent traces are added. Also affects the default
            value of `fill`.
        selected
            :class:`plotly.graph_objects.scatter.Selected` instance
            or dict with compatible properties
        selectedpoints
            Array containing integer indices of selected points.
            Has an effect only for traces that support selections.
            Note that an empty array means an empty selection where
            the `unselected` are turned on for all points, whereas,
            any other non-array values means no selection all where
            the `selected` and `unselected` styles have no effect.
        showlegend
            Determines whether or not an item corresponding to this
            trace is shown in the legend.
        stackgaps
            Only relevant when `stackgroup` is used, and only the
            first `stackgaps` found in the `stackgroup` will be
            used - including if `visible` is "legendonly" but not
            if it is `false`. Determines how we handle locations at
            which other traces in this group have data but this one
            does not. With *infer zero* we insert a zero at these
            locations. With "interpolate" we linearly interpolate
            between existing values, and extrapolate a constant
            beyond the existing values.
        stackgroup
            Set several scatter traces (on the same subplot) to the
            same stackgroup in order to add their y values (or
            their x values if `orientation` is "h"). If blank or
            omitted this trace will not be stacked. Stacking also
            turns `fill` on by default, using "tonexty" ("tonextx")
            if `orientation` is "h" ("v") and sets the default
            `mode` to "lines" irrespective of point count. You can
            only stack on a numeric (linear or log) axis. Traces in
            a `stackgroup` will only fill to (or be filled to)
            other traces in the same group. With multiple
            `stackgroup`s or some traces stacked and some not, if
            fill-linked traces are not already consecutive, the
            later ones will be pushed down in the drawing order.
        stream
            :class:`plotly.graph_objects.scatter.Stream` instance
            or dict with compatible properties
        text
            Sets text elements associated with each (x,y) pair. If
            a single string, the same string appears over all the
            data points. If an array of string, the items are
            mapped in order to the this trace's (x,y) coordinates.
            If trace `hoverinfo` contains a "text" flag and
            "hovertext" is not set, these elements will be seen in
            the hover labels.
        textfont
            Sets the text font.
        textposition
            Sets the positions of the `text` elements with respects
            to the (x,y) coordinates.
        textpositionsrc
            Sets the source reference on Chart Studio Cloud for
            `textposition`.
        textsrc
            Sets the source reference on Chart Studio Cloud for
            `text`.
        texttemplate
            Template string used for rendering the information text
            that appears on points. Note that this will override
            `textinfo`. Variables are inserted using %{variable},
            for example "y: %{y}". Numbers are formatted using
            d3-format's syntax %{variable:d3-format}, for example
            "Price: %{y:$.2f}".
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
            the fallback value. All attributes that can be
            specified per-point (the ones that are `arrayOk: true`)
            are available.
        texttemplatefallback
            Fallback string that's displayed when a variable
            referenced in a template is missing. If the boolean
            value 'false' is passed in, the specifier with the
            missing variable will be displayed.
        texttemplatesrc
            Sets the source reference on Chart Studio Cloud for
            `texttemplate`.
        uid
            Assign an id to this trace, Use this to provide object
            constancy between traces during animations and
            transitions.
        uirevision
            Controls persistence of some user-driven changes to the
            trace: `constraintrange` in `parcoords` traces, as well
            as some `editable: true` modifications such as `name`
            and `colorbar.title`. Defaults to `layout.uirevision`.
            Note that other user-driven trace attribute changes are
            controlled by `layout` attributes: `trace.visible` is
            controlled by `layout.legend.uirevision`,
            `selectedpoints` is controlled by
            `layout.selectionrevision`, and `colorbar.(x|y)`
            (accessible with `config: {editable: true}`) is
            controlled by `layout.editrevision`. Trace changes are
            tracked by `uid`, which only falls back on trace index
            if no `uid` is provided. So if your app can add/remove
            traces before the end of the `data` array, such that
            the same trace has a different index, you can still
            preserve user-driven changes if you give each trace a
            `uid` that stays with it as it moves.
        unselected
            :class:`plotly.graph_objects.scatter.Unselected`
            instance or dict with compatible properties
        visible
            Determines whether or not this trace is visible. If
            "legendonly", the trace is not drawn, but can appear as
            a legend item (provided that the legend itself is
            visible).
        x
            Sets the x coordinates.
        x0
            Alternate to `x`. Builds a linear space of x
            coordinates. Use with `dx` where `x0` is the starting
            coordinate and `dx` the step.
        xaxis
            Sets a reference between this trace's x coordinates and
            a 2D cartesian x axis. If "x" (the default value), the
            x coordinates refer to `layout.xaxis`. If "x2", the x
            coordinates refer to `layout.xaxis2`, and so on.
        xcalendar
            Sets the calendar system to use with `x` date data.
        xhoverformat
            Sets the hover text formatting rulefor `x`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `xaxis.hoverformat`.
        xperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the x
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        xperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the x0 axis. When `x0period` is round number
            of weeks, the `x0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        xperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the x axis.
        xsrc
            Sets the source reference on Chart Studio Cloud for
            `x`.
        y
            Sets the y coordinates.
        y0
            Alternate to `y`. Builds a linear space of y
            coordinates. Use with `dy` where `y0` is the starting
            coordinate and `dy` the step.
        yaxis
            Sets a reference between this trace's y coordinates and
            a 2D cartesian y axis. If "y" (the default value), the
            y coordinates refer to `layout.yaxis`. If "y2", the y
            coordinates refer to `layout.yaxis2`, and so on.
        ycalendar
            Sets the calendar system to use with `y` date data.
        yhoverformat
            Sets the hover text formatting rulefor `y`  using d3
            formatting mini-languages which are very similar to
            those in Python. For numbers, see:
            https://github.com/d3/d3-format/tree/v1.4.5#d3-format.
            And for dates see: https://github.com/d3/d3-time-
            format/tree/v2.2.3#locale_format. We add two items to
            d3's date formatter: "%h" for half of the year as a
            decimal number as well as "%{n}f" for fractional
            seconds with n digits. For example, *2016-10-13
            09:15:23.456* with tickformat "%H~%M~%S.%2f" would
            display *09~15~23.46*By default the values are
            formatted using `yaxis.hoverformat`.
        yperiod
            Only relevant when the axis `type` is "date". Sets the
            period positioning in milliseconds or "M<n>" on the y
            axis. Special values in the form of "M<n>" could be
            used to declare the number of months. In this case `n`
            must be a positive integer.
        yperiod0
            Only relevant when the axis `type` is "date". Sets the
            base for period positioning in milliseconds or date
            string on the y0 axis. When `y0period` is round number
            of weeks, the `y0period0` by default would be on a
            Sunday i.e. 2000-01-02, otherwise it would be at
            2000-01-01.
        yperiodalignment
            Only relevant when the axis `type` is "date". Sets the
            alignment of data points on the y axis.
        ysrc
            Sets the source reference on Chart Studio Cloud for
            `y`.
        zorder
            Sets the layer on which this trace is displayed,
            relative to other SVG traces on the same subplot. SVG
            traces with higher `zorder` appear in front of those
            with lower `zorder`.

        Returns
        -------
        Scatter
        """
        super().__init__("scatter")
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
The first argument to the plotly.graph_objs.Scatter
constructor must be a dict or
an instance of :class:`plotly.graph_objs.Scatter`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("alignmentgroup", arg, alignmentgroup)
        self._set_property("cliponaxis", arg, cliponaxis)
        self._set_property("connectgaps", arg, connectgaps)
        self._set_property("customdata", arg, customdata)
        self._set_property("customdatasrc", arg, customdatasrc)
        self._set_property("dx", arg, dx)
        self._set_property("dy", arg, dy)
        self._set_property("error_x", arg, error_x)
        self._set_property("error_y", arg, error_y)
        self._set_property("fill", arg, fill)
        self._set_property("fillcolor", arg, fillcolor)
        self._set_property("fillgradient", arg, fillgradient)
        self._set_property("fillpattern", arg, fillpattern)
        self._set_property("groupnorm", arg, groupnorm)
        self._set_property("hoverinfo", arg, hoverinfo)
        self._set_property("hoverinfosrc", arg, hoverinfosrc)
        self._set_property("hoverlabel", arg, hoverlabel)
        self._set_property("hoveron", arg, hoveron)
        self._set_property("hovertemplate", arg, hovertemplate)
        self._set_property("hovertemplatefallback", arg, hovertemplatefallback)
        self._set_property("hovertemplatesrc", arg, hovertemplatesrc)
        self._set_property("hovertext", arg, hovertext)
        self._set_property("hovertextsrc", arg, hovertextsrc)
        self._set_property("ids", arg, ids)
        self._set_property("idssrc", arg, idssrc)
        self._set_property("legend", arg, legend)
        self._set_property("legendgroup", arg, legendgroup)
        self._set_property("legendgrouptitle", arg, legendgrouptitle)
        self._set_property("legendrank", arg, legendrank)
        self._set_property("legendwidth", arg, legendwidth)
        self._set_property("line", arg, line)
        self._set_property("marker", arg, marker)
        self._set_property("meta", arg, meta)
        self._set_property("metasrc", arg, metasrc)
        self._set_property("mode", arg, mode)
        self._set_property("name", arg, name)
        self._set_property("offsetgroup", arg, offsetgroup)
        self._set_property("opacity", arg, opacity)
        self._set_property("orientation", arg, orientation)
        self._set_property("selected", arg, selected)
        self._set_property("selectedpoints", arg, selectedpoints)
        self._set_property("showlegend", arg, showlegend)
        self._set_property("stackgaps", arg, stackgaps)
        self._set_property("stackgroup", arg, stackgroup)
        self._set_property("stream", arg, stream)
        self._set_property("text", arg, text)
        self._set_property("textfont", arg, textfont)
        self._set_property("textposition", arg, textposition)
        self._set_property("textpositionsrc", arg, textpositionsrc)
        self._set_property("textsrc", arg, textsrc)
        self._set_property("texttemplate", arg, texttemplate)
        self._set_property("texttemplatefallback", arg, texttemplatefallback)
        self._set_property("texttemplatesrc", arg, texttemplatesrc)
        self._set_property("uid", arg, uid)
        self._set_property("uirevision", arg, uirevision)
        self._set_property("unselected", arg, unselected)
        self._set_property("visible", arg, visible)
        self._set_property("x", arg, x)
        self._set_property("x0", arg, x0)
        self._set_property("xaxis", arg, xaxis)
        self._set_property("xcalendar", arg, xcalendar)
        self._set_property("xhoverformat", arg, xhoverformat)
        self._set_property("xperiod", arg, xperiod)
        self._set_property("xperiod0", arg, xperiod0)
        self._set_property("xperiodalignment", arg, xperiodalignment)
        self._set_property("xsrc", arg, xsrc)
        self._set_property("y", arg, y)
        self._set_property("y0", arg, y0)
        self._set_property("yaxis", arg, yaxis)
        self._set_property("ycalendar", arg, ycalendar)
        self._set_property("yhoverformat", arg, yhoverformat)
        self._set_property("yperiod", arg, yperiod)
        self._set_property("yperiod0", arg, yperiod0)
        self._set_property("yperiodalignment", arg, yperiodalignment)
        self._set_property("ysrc", arg, ysrc)
        self._set_property("zorder", arg, zorder)

        self._props["type"] = "scatter"
        arg.pop("type", None)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
