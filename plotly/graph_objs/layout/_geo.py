#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Geo(_BaseLayoutHierarchyType):
    _parent_path_str = "layout"
    _path_str = "layout.geo"
    _valid_props = {
        "bgcolor",
        "center",
        "coastlinecolor",
        "coastlinewidth",
        "countrycolor",
        "countrywidth",
        "domain",
        "fitbounds",
        "framecolor",
        "framewidth",
        "lakecolor",
        "landcolor",
        "lataxis",
        "lonaxis",
        "oceancolor",
        "projection",
        "resolution",
        "rivercolor",
        "riverwidth",
        "scope",
        "showcoastlines",
        "showcountries",
        "showframe",
        "showlakes",
        "showland",
        "showocean",
        "showrivers",
        "showsubunits",
        "subunitcolor",
        "subunitwidth",
        "uirevision",
        "visible",
    }

    @property
    def bgcolor(self):
        """
        Set the background color of the map

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
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Center`
          - A dict of string/value properties that will be passed
            to the Center constructor

        Returns
        -------
        plotly.graph_objs.layout.geo.Center
        """
        pass


    @property
    def coastlinecolor(self):
        """
        Sets the coastline color.

        The 'coastlinecolor' property is a color and may be specified as:
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
    def coastlinewidth(self):
        """
        Sets the coastline stroke width (in px).

        The 'coastlinewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def countrycolor(self):
        """
        Sets line color of the country boundaries.

        The 'countrycolor' property is a color and may be specified as:
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
    def countrywidth(self):
        """
        Sets line width (in px) of the country boundaries.

        The 'countrywidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.geo.Domain
        """
        pass


    @property
    def fitbounds(self):
        """
        Determines if this subplot's view settings are auto-computed to
        fit trace data. On scoped maps, setting `fitbounds` leads to
        `center.lon` and `center.lat` getting auto-filled. On maps with
        a non-clipped projection, setting `fitbounds` leads to
        `center.lon`, `center.lat`, and `projection.rotation.lon`
        getting auto-filled. On maps with a clipped projection, setting
        `fitbounds` leads to `center.lon`, `center.lat`,
        `projection.rotation.lon`, `projection.rotation.lat`,
        `lonaxis.range` and `lataxis.range` getting auto-filled. If
        "locations", only the trace's visible locations are considered
        in the `fitbounds` computations. If "geojson", the entire trace
        input `geojson` (if provided) is considered in the `fitbounds`
        computations, Defaults to False.

        The 'fitbounds' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [False, 'locations', 'geojson']

        Returns
        -------
        Any
        """
        pass


    @property
    def framecolor(self):
        """
        Sets the color the frame.

        The 'framecolor' property is a color and may be specified as:
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
    def framewidth(self):
        """
        Sets the stroke width (in px) of the frame.

        The 'framewidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def lakecolor(self):
        """
        Sets the color of the lakes.

        The 'lakecolor' property is a color and may be specified as:
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
    def landcolor(self):
        """
        Sets the land mass color.

        The 'landcolor' property is a color and may be specified as:
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
    def lataxis(self):
        """
        The 'lataxis' property is an instance of Lataxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Lataxis`
          - A dict of string/value properties that will be passed
            to the Lataxis constructor

        Returns
        -------
        plotly.graph_objs.layout.geo.Lataxis
        """
        pass


    @property
    def lonaxis(self):
        """
        The 'lonaxis' property is an instance of Lonaxis
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Lonaxis`
          - A dict of string/value properties that will be passed
            to the Lonaxis constructor

        Returns
        -------
        plotly.graph_objs.layout.geo.Lonaxis
        """
        pass


    @property
    def oceancolor(self):
        """
        Sets the ocean color

        The 'oceancolor' property is a color and may be specified as:
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
    def projection(self):
        """
        The 'projection' property is an instance of Projection
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.geo.Projection`
          - A dict of string/value properties that will be passed
            to the Projection constructor

        Returns
        -------
        plotly.graph_objs.layout.geo.Projection
        """
        pass


    @property
    def resolution(self):
        """
        Sets the resolution of the base layers. The values have units
        of km/mm e.g. 110 corresponds to a scale ratio of
        1:110,000,000.

        The 'resolution' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                [110, 50]

        Returns
        -------
        Any
        """
        pass


    @property
    def rivercolor(self):
        """
        Sets color of the rivers.

        The 'rivercolor' property is a color and may be specified as:
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
    def riverwidth(self):
        """
        Sets the stroke width (in px) of the rivers.

        The 'riverwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def scope(self):
        """
        Set the scope of the map.

        The 'scope' property is an enumeration that may be specified as:
          - One of the following enumeration values:
                ['africa', 'antarctica', 'asia', 'europe', 'north
                america', 'oceania', 'south america', 'usa', 'world']

        Returns
        -------
        Any
        """
        pass


    @property
    def showcoastlines(self):
        """
        Sets whether or not the coastlines are drawn.

        The 'showcoastlines' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showcountries(self):
        """
        Sets whether or not country boundaries are drawn.

        The 'showcountries' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showframe(self):
        """
        Sets whether or not a frame is drawn around the map.

        The 'showframe' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showlakes(self):
        """
        Sets whether or not lakes are drawn.

        The 'showlakes' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showland(self):
        """
        Sets whether or not land masses are filled in color.

        The 'showland' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showocean(self):
        """
        Sets whether or not oceans are filled in color.

        The 'showocean' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showrivers(self):
        """
        Sets whether or not rivers are drawn.

        The 'showrivers' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def showsubunits(self):
        """
        Sets whether or not boundaries of subunits within countries
        (e.g. states, provinces) are drawn.

        The 'showsubunits' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass


    @property
    def subunitcolor(self):
        """
        Sets the color of the subunits boundaries.

        The 'subunitcolor' property is a color and may be specified as:
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
    def subunitwidth(self):
        """
        Sets the stroke width (in px) of the subunits boundaries.

        The 'subunitwidth' property is a number and may be specified as:
          - An int or float in the interval [0, inf]

        Returns
        -------
        int|float
        """
        pass


    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view
        (projection and center). Defaults to `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def visible(self):
        """
        Sets the default visibility of the base layers.

        The 'visible' property is a boolean and must be specified as:
          - A boolean value: True or False

        Returns
        -------
        bool
        """
        pass



    def __init__(
        self,
        arg=None,
        bgcolor=None,
        center=None,
        coastlinecolor=None,
        coastlinewidth=None,
        countrycolor=None,
        countrywidth=None,
        domain=None,
        fitbounds=None,
        framecolor=None,
        framewidth=None,
        lakecolor=None,
        landcolor=None,
        lataxis=None,
        lonaxis=None,
        oceancolor=None,
        projection=None,
        resolution=None,
        rivercolor=None,
        riverwidth=None,
        scope=None,
        showcoastlines=None,
        showcountries=None,
        showframe=None,
        showlakes=None,
        showland=None,
        showocean=None,
        showrivers=None,
        showsubunits=None,
        subunitcolor=None,
        subunitwidth=None,
        uirevision=None,
        visible=None,
        **kwargs,
    ):
        """
        Construct a new Geo object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Geo`
        bgcolor
            Set the background color of the map
        center
            :class:`plotly.graph_objects.layout.geo.Center`
            instance or dict with compatible properties
        coastlinecolor
            Sets the coastline color.
        coastlinewidth
            Sets the coastline stroke width (in px).
        countrycolor
            Sets line color of the country boundaries.
        countrywidth
            Sets line width (in px) of the country boundaries.
        domain
            :class:`plotly.graph_objects.layout.geo.Domain`
            instance or dict with compatible properties
        fitbounds
            Determines if this subplot's view settings are auto-
            computed to fit trace data. On scoped maps, setting
            `fitbounds` leads to `center.lon` and `center.lat`
            getting auto-filled. On maps with a non-clipped
            projection, setting `fitbounds` leads to `center.lon`,
            `center.lat`, and `projection.rotation.lon` getting
            auto-filled. On maps with a clipped projection, setting
            `fitbounds` leads to `center.lon`, `center.lat`,
            `projection.rotation.lon`, `projection.rotation.lat`,
            `lonaxis.range` and `lataxis.range` getting auto-
            filled. If "locations", only the trace's visible
            locations are considered in the `fitbounds`
            computations. If "geojson", the entire trace input
            `geojson` (if provided) is considered in the
            `fitbounds` computations, Defaults to False.
        framecolor
            Sets the color the frame.
        framewidth
            Sets the stroke width (in px) of the frame.
        lakecolor
            Sets the color of the lakes.
        landcolor
            Sets the land mass color.
        lataxis
            :class:`plotly.graph_objects.layout.geo.Lataxis`
            instance or dict with compatible properties
        lonaxis
            :class:`plotly.graph_objects.layout.geo.Lonaxis`
            instance or dict with compatible properties
        oceancolor
            Sets the ocean color
        projection
            :class:`plotly.graph_objects.layout.geo.Projection`
            instance or dict with compatible properties
        resolution
            Sets the resolution of the base layers. The values have
            units of km/mm e.g. 110 corresponds to a scale ratio of
            1:110,000,000.
        rivercolor
            Sets color of the rivers.
        riverwidth
            Sets the stroke width (in px) of the rivers.
        scope
            Set the scope of the map.
        showcoastlines
            Sets whether or not the coastlines are drawn.
        showcountries
            Sets whether or not country boundaries are drawn.
        showframe
            Sets whether or not a frame is drawn around the map.
        showlakes
            Sets whether or not lakes are drawn.
        showland
            Sets whether or not land masses are filled in color.
        showocean
            Sets whether or not oceans are filled in color.
        showrivers
            Sets whether or not rivers are drawn.
        showsubunits
            Sets whether or not boundaries of subunits within
            countries (e.g. states, provinces) are drawn.
        subunitcolor
            Sets the color of the subunits boundaries.
        subunitwidth
            Sets the stroke width (in px) of the subunits
            boundaries.
        uirevision
            Controls persistence of user-driven changes in the view
            (projection and center). Defaults to
            `layout.uirevision`.
        visible
            Sets the default visibility of the base layers.

        Returns
        -------
        Geo
        """
        super().__init__("geo")
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
The first argument to the plotly.graph_objs.layout.Geo
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Geo`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("bgcolor", arg, bgcolor)
        self._set_property("center", arg, center)
        self._set_property("coastlinecolor", arg, coastlinecolor)
        self._set_property("coastlinewidth", arg, coastlinewidth)
        self._set_property("countrycolor", arg, countrycolor)
        self._set_property("countrywidth", arg, countrywidth)
        self._set_property("domain", arg, domain)
        self._set_property("fitbounds", arg, fitbounds)
        self._set_property("framecolor", arg, framecolor)
        self._set_property("framewidth", arg, framewidth)
        self._set_property("lakecolor", arg, lakecolor)
        self._set_property("landcolor", arg, landcolor)
        self._set_property("lataxis", arg, lataxis)
        self._set_property("lonaxis", arg, lonaxis)
        self._set_property("oceancolor", arg, oceancolor)
        self._set_property("projection", arg, projection)
        self._set_property("resolution", arg, resolution)
        self._set_property("rivercolor", arg, rivercolor)
        self._set_property("riverwidth", arg, riverwidth)
        self._set_property("scope", arg, scope)
        self._set_property("showcoastlines", arg, showcoastlines)
        self._set_property("showcountries", arg, showcountries)
        self._set_property("showframe", arg, showframe)
        self._set_property("showlakes", arg, showlakes)
        self._set_property("showland", arg, showland)
        self._set_property("showocean", arg, showocean)
        self._set_property("showrivers", arg, showrivers)
        self._set_property("showsubunits", arg, showsubunits)
        self._set_property("subunitcolor", arg, subunitcolor)
        self._set_property("subunitwidth", arg, subunitwidth)
        self._set_property("uirevision", arg, uirevision)
        self._set_property("visible", arg, visible)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
