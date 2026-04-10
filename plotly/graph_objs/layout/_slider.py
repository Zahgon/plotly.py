#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Slider(_BaseLayoutHierarchyType):
    _parent_path_str = "layout"
    _path_str = "layout.slider"
    _valid_props = {
        "active",
        "activebgcolor",
        "bgcolor",
        "bordercolor",
        "borderwidth",
        "currentvalue",
        "font",
        "len",
        "lenmode",
        "minorticklen",
        "name",
        "pad",
        "stepdefaults",
        "steps",
        "templateitemname",
        "tickcolor",
        "ticklen",
        "tickwidth",
        "transition",
        "visible",
        "x",
        "xanchor",
        "y",
        "yanchor",
    }

    @property
    def active(self):
        """
        Determines which button (by index starting from 0) is
        considered active.

        The 'active' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def activebgcolor(self):
        """
        Sets the background color of the slider grip while dragging.

        The 'activebgcolor' property is a color and may be specified as:
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
    def bgcolor(self):
        """
        Sets the background color of the slider.

        The 'bgcolor' property is a color and may be specified as:
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
    def bordercolor(self):
        """
        Sets the color of the border enclosing the slider.

        The 'bordercolor' property is a color and may be specified as:
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
    def borderwidth(self):
        """
        Sets the width (in px) of the border enclosing the slider.

        The 'borderwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def currentvalue(self):
        """
        The 'currentvalue' property is an instance of Currentvalue
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Currentvalue`
          - A dict of string/value properties that will be passed
            to the Currentvalue constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Currentvalue
        """
        pass


    @property
    def font(self):
        """
        Sets the font of the slider step labels.

        The 'font' property is an instance of Font
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Font`
          - A dict of string/value properties that will be passed
            to the Font constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Font
        """
        pass


    @property
    def len(self):
        """
        Sets the length of the slider This measure excludes the padding
        of both ends. That is, the slider's length is this length minus
        the padding on both ends.

        The 'len' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def lenmode(self):
        """
        Determines whether this slider length is set in units of plot
        "fraction" or in *pixels. Use `len` to set the value.

        The 'lenmode' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['fraction', 'pixels']

        Returns
        -------
        Any
        """
        pass


    @property
    def minorticklen(self):
        """
        Sets the length in pixels of minor step tick marks

        The 'minorticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def name(self):
        """
        When used in a template, named items are created in the output
        figure in addition to any items the figure already has in this
        array. You can modify these items in the output figure by
        making your own item with `templateitemname` matching this
        `name` alongside your modifications (including `visible: false`
        or `enabled: false` to hide it). Has no effect outside of a
        template.

        The 'name' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def pad(self):
        """
        Set the padding of the slider component along each side.

        The 'pad' property is an instance of Pad
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Pad`
          - A dict of string/value properties that will be passed
            to the Pad constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Pad
        """
        pass


    @property
    def steps(self):
        """
        The 'steps' property is a tuple of instances of
        Step that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.slider.Step
          - A list or tuple of dicts of string/value properties that
            will be passed to the Step constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.slider.Step]
        """
        pass


    @property
    def stepdefaults(self):
        """
        When used in a template (as
        layout.template.layout.slider.stepdefaults), sets the default
        property values to use for elements of layout.slider.steps

        The 'stepdefaults' property is an instance of Step
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Step`
          - A dict of string/value properties that will be passed
            to the Step constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Step
        """
        pass


    @property
    def templateitemname(self):
        """
        Used to refer to a named item in this array in the template.
        Named items from the template will be created even without a
        matching item in the input figure, but you can modify one by
        making an item with `templateitemname` matching its `name`,
        alongside your modifications (including `visible: false` or
        `enabled: false` to hide it). If there is no template or no
        matching item, this item will be hidden unless you explicitly
        show it with `visible: true`.

        The 'templateitemname' property is a string and must be specified as:
          - A string
          - A number that will be converted to a string

        Returns
        -------
        str
        """
        pass


    @property
    def tickcolor(self):
        """
        Sets the color of the border enclosing the slider.

        The 'tickcolor' property is a color and may be specified as:
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
    def ticklen(self):
        """
        Sets the length in pixels of step tick marks

        The 'ticklen' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def tickwidth(self):
        """
        Sets the tick width (in px).

        The 'tickwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def transition(self):
        """
        The 'transition' property is an instance of Transition
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.slider.Transition`
          - A dict of string/value properties that will be passed
            to the Transition constructor

        Returns
        -------
        plotly.graph_objs.layout.slider.Transition
        """
        pass


    @property
    def visible(self):
        """
        Determines whether or not the slider is visible.

        The 'visible' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def x(self):
        """
        Sets the x position (in normalized coordinates) of the slider.

        The 'x' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        pass


    @property
    def xanchor(self):
        """
        Sets the slider's horizontal position anchor. This anchor binds
        the `x` position to the "left", "center" or "right" of the
        range selector.

        The 'xanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'left', 'center', 'right']

        Returns
        -------
        Any
        """
        pass


    @property
    def y(self):
        """
        Sets the y position (in normalized coordinates) of the slider.

        The 'y' property is a number and may be specified as:
          - An int or float in the interval [-2, 3]

        Returns
        -------
        int|float
        """
        pass


    @property
    def yanchor(self):
        """
        Sets the slider's vertical position anchor This anchor binds
        the `y` position to the "top", "middle" or "bottom" of the
        range selector.

        The 'yanchor' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['auto', 'top', 'middle', 'bottom']

        Returns
        -------
        Any
        """
        pass



    def __init__(
        self,
        arg=None,
        active=None,
        activebgcolor=None,
        bgcolor=None,
        bordercolor=None,
        borderwidth=None,
        currentvalue=None,
        font=None,
        len=None,
        lenmode=None,
        minorticklen=None,
        name=None,
        pad=None,
        steps=None,
        stepdefaults=None,
        templateitemname=None,
        tickcolor=None,
        ticklen=None,
        tickwidth=None,
        transition=None,
        visible=None,
        x=None,
        xanchor=None,
        y=None,
        yanchor=None,
        **kwargs,
    ):
        """
        Construct a new Slider object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Slider`
        active
            Determines which button (by index starting from 0) is
            considered active.
        activebgcolor
            Sets the background color of the slider grip while
            dragging.
        bgcolor
            Sets the background color of the slider.
        bordercolor
            Sets the color of the border enclosing the slider.
        borderwidth
            Sets the width (in px) of the border enclosing the
            slider.
        currentvalue
            :class:`plotly.graph_objects.layout.slider.Currentvalue
            ` instance or dict with compatible properties
        font
            Sets the font of the slider step labels.
        len
            Sets the length of the slider This measure excludes the
            padding of both ends. That is, the slider's length is
            this length minus the padding on both ends.
        lenmode
            Determines whether this slider length is set in units
            of plot "fraction" or in *pixels. Use `len` to set the
            value.
        minorticklen
            Sets the length in pixels of minor step tick marks
        name
            When used in a template, named items are created in the
            output figure in addition to any items the figure
            already has in this array. You can modify these items
            in the output figure by making your own item with
            `templateitemname` matching this `name` alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). Has no effect outside of a
            template.
        pad
            Set the padding of the slider component along each
            side.
        steps
            A tuple of
            :class:`plotly.graph_objects.layout.slider.Step`
            instances or dicts with compatible properties
        stepdefaults
            When used in a template (as
            layout.template.layout.slider.stepdefaults), sets the
            default property values to use for elements of
            layout.slider.steps
        templateitemname
            Used to refer to a named item in this array in the
            template. Named items from the template will be created
            even without a matching item in the input figure, but
            you can modify one by making an item with
            `templateitemname` matching its `name`, alongside your
            modifications (including `visible: false` or `enabled:
            false` to hide it). If there is no template or no
            matching item, this item will be hidden unless you
            explicitly show it with `visible: true`.
        tickcolor
            Sets the color of the border enclosing the slider.
        ticklen
            Sets the length in pixels of step tick marks
        tickwidth
            Sets the tick width (in px).
        transition
            :class:`plotly.graph_objects.layout.slider.Transition`
            instance or dict with compatible properties
        visible
            Determines whether or not the slider is visible.
        x
            Sets the x position (in normalized coordinates) of the
            slider.
        xanchor
            Sets the slider's horizontal position anchor. This
            anchor binds the `x` position to the "left", "center"
            or "right" of the range selector.
        y
            Sets the y position (in normalized coordinates) of the
            slider.
        yanchor
            Sets the slider's vertical position anchor This anchor
            binds the `y` position to the "top", "middle" or
            "bottom" of the range selector.

        Returns
        -------
        Slider
        """
        super().__init__("sliders")
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
The first argument to the plotly.graph_objs.layout.Slider
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Slider`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("active", arg, active)
        self._set_property("activebgcolor", arg, activebgcolor)
        self._set_property("bgcolor", arg, bgcolor)
        self._set_property("bordercolor", arg, bordercolor)
        self._set_property("borderwidth", arg, borderwidth)
        self._set_property("currentvalue", arg, currentvalue)
        self._set_property("font", arg, font)
        self._set_property("len", arg, len)
        self._set_property("lenmode", arg, lenmode)
        self._set_property("minorticklen", arg, minorticklen)
        self._set_property("name", arg, name)
        self._set_property("pad", arg, pad)
        self._set_property("steps", arg, steps)
        self._set_property("stepdefaults", arg, stepdefaults)
        self._set_property("templateitemname", arg, templateitemname)
        self._set_property("tickcolor", arg, tickcolor)
        self._set_property("ticklen", arg, ticklen)
        self._set_property("tickwidth", arg, tickwidth)
        self._set_property("transition", arg, transition)
        self._set_property("visible", arg, visible)
        self._set_property("x", arg, x)
        self._set_property("xanchor", arg, xanchor)
        self._set_property("y", arg, y)
        self._set_property("yanchor", arg, yanchor)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
