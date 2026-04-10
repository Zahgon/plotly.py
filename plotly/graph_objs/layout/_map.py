#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Map(_BaseLayoutHierarchyType):
    _parent_path_str = "layout"
    _path_str = "layout.map"
    _valid_props = {
        "bearing",
        "bounds",
        "center",
        "domain",
        "layerdefaults",
        "layers",
        "pitch",
        "style",
        "uirevision",
        "zoom",
    }

    @property
    def bearing(self):
        """
        Sets the bearing angle of the map in degrees counter-clockwise
        from North (map.bearing).

        The 'bearing' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def bounds(self):
        """
        The 'bounds' property is an instance of Bounds
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.map.Bounds`
          - A dict of string/value properties that will be passed
            to the Bounds constructor

        Returns
        -------
        plotly.graph_objs.layout.map.Bounds
        """
        pass


    @property
    def center(self):
        """
        The 'center' property is an instance of Center
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.map.Center`
          - A dict of string/value properties that will be passed
            to the Center constructor

        Returns
        -------
        plotly.graph_objs.layout.map.Center
        """
        pass


    @property
    def domain(self):
        """
        The 'domain' property is an instance of Domain
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.map.Domain`
          - A dict of string/value properties that will be passed
            to the Domain constructor

        Returns
        -------
        plotly.graph_objs.layout.map.Domain
        """
        pass


    @property
    def layers(self):
        """
        The 'layers' property is a tuple of instances of
        Layer that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.map.Layer
          - A list or tuple of dicts of string/value properties that
            will be passed to the Layer constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.map.Layer]
        """
        pass


    @property
    def layerdefaults(self):
        """
        When used in a template (as
        layout.template.layout.map.layerdefaults), sets the default
        property values to use for elements of layout.map.layers

        The 'layerdefaults' property is an instance of Layer
        that may be specified as:
          - An instance of :class:`plotly.graph_objs.layout.map.Layer`
          - A dict of string/value properties that will be passed
            to the Layer constructor

        Returns
        -------
        plotly.graph_objs.layout.map.Layer
        """
        pass


    @property
    def pitch(self):
        """
        Sets the pitch angle of the map (in degrees, where 0 means
        perpendicular to the surface of the map) (map.pitch).

        The 'pitch' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass


    @property
    def style(self):
        """
        Defines the map layers that are rendered by default below the
        trace layers defined in `data`, which are themselves by default
        rendered below the layers defined in `layout.map.layers`.
        These layers can be defined either explicitly as a Map Style
        object which can contain multiple layer definitions that load
        data from any public or private Tile Map Service (TMS or XYZ)
        or Web Map Service (WMS) or implicitly by using one of the
        built-in style objects which use WMSes or by using a custom
        style URL  Map Style objects are of the form described in the
        MapLibre GL JS documentation available at
        https://maplibre.org/maplibre-style-spec/  The built-in
        plotly.js styles objects are: basic, carto-darkmatter, carto-
        darkmatter-nolabels, carto-positron, carto-positron-nolabels,
        carto-voyager, carto-voyager-nolabels, dark, light, open-
        street-map, outdoors, satellite, satellite-streets, streets,
        white-bg.

        The 'style' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def uirevision(self):
        """
        Controls persistence of user-driven changes in the view:
        `center`, `zoom`, `bearing`, `pitch`. Defaults to
        `layout.uirevision`.

        The 'uirevision' property accepts values of any type

        Returns
        -------
        Any
        """
        pass


    @property
    def zoom(self):
        """
        Sets the zoom level of the map (map.zoom).

        The 'zoom' property is a number and may be specified as:
          - An int or float

        Returns
        -------
        int|float
        """
        pass



    def __init__(
        self,
        arg=None,
        bearing=None,
        bounds=None,
        center=None,
        domain=None,
        layers=None,
        layerdefaults=None,
        pitch=None,
        style=None,
        uirevision=None,
        zoom=None,
        **kwargs,
    ):
        """
        Construct a new Map object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of :class:`plotly.graph_objs.layout.Map`
        bearing
            Sets the bearing angle of the map in degrees counter-
            clockwise from North (map.bearing).
        bounds
            :class:`plotly.graph_objects.layout.map.Bounds`
            instance or dict with compatible properties
        center
            :class:`plotly.graph_objects.layout.map.Center`
            instance or dict with compatible properties
        domain
            :class:`plotly.graph_objects.layout.map.Domain`
            instance or dict with compatible properties
        layers
            A tuple of
            :class:`plotly.graph_objects.layout.map.Layer`
            instances or dicts with compatible properties
        layerdefaults
            When used in a template (as
            layout.template.layout.map.layerdefaults), sets the
            default property values to use for elements of
            layout.map.layers
        pitch
            Sets the pitch angle of the map (in degrees, where 0
            means perpendicular to the surface of the map)
            (map.pitch).
        style
            Defines the map layers that are rendered by default
            below the trace layers defined in `data`, which are
            themselves by default rendered below the layers defined
            in `layout.map.layers`.  These layers can be defined
            either explicitly as a Map Style object which can
            contain multiple layer definitions that load data from
            any public or private Tile Map Service (TMS or XYZ) or
            Web Map Service (WMS) or implicitly by using one of the
            built-in style objects which use WMSes or by using a
            custom style URL  Map Style objects are of the form
            described in the MapLibre GL JS documentation available
            at https://maplibre.org/maplibre-style-spec/  The
            built-in plotly.js styles objects are: basic, carto-
            darkmatter, carto-darkmatter-nolabels, carto-positron,
            carto-positron-nolabels, carto-voyager, carto-voyager-
            nolabels, dark, light, open-street-map, outdoors,
            satellite, satellite-streets, streets, white-bg.
        uirevision
            Controls persistence of user-driven changes in the
            view: `center`, `zoom`, `bearing`, `pitch`. Defaults to
            `layout.uirevision`.
        zoom
            Sets the zoom level of the map (map.zoom).

        Returns
        -------
        Map
        """
        super().__init__("map")
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
The first argument to the plotly.graph_objs.layout.Map
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.Map`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("bearing", arg, bearing)
        self._set_property("bounds", arg, bounds)
        self._set_property("center", arg, center)
        self._set_property("domain", arg, domain)
        self._set_property("layers", arg, layers)
        self._set_property("layerdefaults", arg, layerdefaults)
        self._set_property("pitch", arg, pitch)
        self._set_property("style", arg, style)
        self._set_property("uirevision", arg, uirevision)
        self._set_property("zoom", arg, zoom)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
