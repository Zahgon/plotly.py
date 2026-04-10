#                   --- THIS FILE IS AUTO-GENERATED ---
# Modifications will be overwitten the next time code generation run.

from plotly.basedatatypes import BaseLayoutHierarchyType as _BaseLayoutHierarchyType
import copy as _copy


class Data(_BaseLayoutHierarchyType):
    _parent_path_str = "layout.template"
    _path_str = "layout.template.data"
    _valid_props = {
        "bar",
        "barpolar",
        "box",
        "candlestick",
        "carpet",
        "choropleth",
        "choroplethmap",
        "choroplethmapbox",
        "cone",
        "contour",
        "contourcarpet",
        "densitymap",
        "densitymapbox",
        "funnel",
        "funnelarea",
        "heatmap",
        "histogram",
        "histogram2d",
        "histogram2dcontour",
        "icicle",
        "image",
        "indicator",
        "isosurface",
        "mesh3d",
        "ohlc",
        "parcats",
        "parcoords",
        "pie",
        "sankey",
        "scatter",
        "scatter3d",
        "scattercarpet",
        "scattergeo",
        "scattergl",
        "scattermap",
        "scattermapbox",
        "scatterpolar",
        "scatterpolargl",
        "scattersmith",
        "scatterternary",
        "splom",
        "streamtube",
        "sunburst",
        "surface",
        "table",
        "treemap",
        "violin",
        "volume",
        "waterfall",
    }

    @property
    def barpolar(self):
        """
        The 'barpolar' property is a tuple of instances of
        Barpolar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Barpolar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Barpolar constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Barpolar]
        """
        pass


    @property
    def bar(self):
        """
        The 'bar' property is a tuple of instances of
        Bar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Bar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Bar constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Bar]
        """
        return self["bar"]

    @bar.setter
    def bar(self, val):
        self["bar"] = val

    @property
    def box(self):
        """
        The 'box' property is a tuple of instances of
        Box that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Box
          - A list or tuple of dicts of string/value properties that
            will be passed to the Box constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Box]
        """
        return self["box"]

    @box.setter
    def box(self, val):
        self["box"] = val

    @property
    def candlestick(self):
        """
        The 'candlestick' property is a tuple of instances of
        Candlestick that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Candlestick
          - A list or tuple of dicts of string/value properties that
            will be passed to the Candlestick constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Candlestick]
        """
        pass


    @property
    def carpet(self):
        """
        The 'carpet' property is a tuple of instances of
        Carpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Carpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Carpet constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Carpet]
        """
        pass


    @property
    def choroplethmapbox(self):
        """
        The 'choroplethmapbox' property is a tuple of instances of
        Choroplethmapbox that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Choroplethmapbox
          - A list or tuple of dicts of string/value properties that
            will be passed to the Choroplethmapbox constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Choroplethmapbox]
        """
        pass


    @property
    def choroplethmap(self):
        """
        The 'choroplethmap' property is a tuple of instances of
        Choroplethmap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Choroplethmap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Choroplethmap constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Choroplethmap]
        """
        pass


    @property
    def choropleth(self):
        """
        The 'choropleth' property is a tuple of instances of
        Choropleth that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Choropleth
          - A list or tuple of dicts of string/value properties that
            will be passed to the Choropleth constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Choropleth]
        """
        return self["choropleth"]

    @choropleth.setter
    def choropleth(self, val):
        self["choropleth"] = val

    @property
    def cone(self):
        """
        The 'cone' property is a tuple of instances of
        Cone that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Cone
          - A list or tuple of dicts of string/value properties that
            will be passed to the Cone constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Cone]
        """
        pass


    @property
    def contourcarpet(self):
        """
        The 'contourcarpet' property is a tuple of instances of
        Contourcarpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Contourcarpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Contourcarpet constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Contourcarpet]
        """
        pass


    @property
    def contour(self):
        """
        The 'contour' property is a tuple of instances of
        Contour that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Contour
          - A list or tuple of dicts of string/value properties that
            will be passed to the Contour constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Contour]
        """
        pass


    @property
    def densitymapbox(self):
        """
        The 'densitymapbox' property is a tuple of instances of
        Densitymapbox that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Densitymapbox
          - A list or tuple of dicts of string/value properties that
            will be passed to the Densitymapbox constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Densitymapbox]
        """
        pass


    @property
    def densitymap(self):
        """
        The 'densitymap' property is a tuple of instances of
        Densitymap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Densitymap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Densitymap constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Densitymap]
        """
        pass


    @property
    def funnelarea(self):
        """
        The 'funnelarea' property is a tuple of instances of
        Funnelarea that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Funnelarea
          - A list or tuple of dicts of string/value properties that
            will be passed to the Funnelarea constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Funnelarea]
        """
        pass


    @property
    def funnel(self):
        """
        The 'funnel' property is a tuple of instances of
        Funnel that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Funnel
          - A list or tuple of dicts of string/value properties that
            will be passed to the Funnel constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Funnel]
        """
        return self["funnel"]

    @funnel.setter
    def funnel(self, val):
        self["funnel"] = val

    @property
    def heatmap(self):
        """
        The 'heatmap' property is a tuple of instances of
        Heatmap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Heatmap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Heatmap constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Heatmap]
        """
        pass


    @property
    def histogram2dcontour(self):
        """
        The 'histogram2dcontour' property is a tuple of instances of
        Histogram2dContour that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram2dContour
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram2dContour constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram2dContour]
        """
        pass


    @property
    def histogram2d(self):
        """
        The 'histogram2d' property is a tuple of instances of
        Histogram2d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram2d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram2d constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram2d]
        """
        pass


    @property
    def histogram(self):
        """
        The 'histogram' property is a tuple of instances of
        Histogram that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Histogram
          - A list or tuple of dicts of string/value properties that
            will be passed to the Histogram constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Histogram]
        """
        return self["histogram"]

    @histogram.setter
    def histogram(self, val):
        self["histogram"] = val

    @property
    def icicle(self):
        """
        The 'icicle' property is a tuple of instances of
        Icicle that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Icicle
          - A list or tuple of dicts of string/value properties that
            will be passed to the Icicle constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Icicle]
        """
        pass


    @property
    def image(self):
        """
        The 'image' property is a tuple of instances of
        Image that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Image
          - A list or tuple of dicts of string/value properties that
            will be passed to the Image constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Image]
        """
        pass


    @property
    def indicator(self):
        """
        The 'indicator' property is a tuple of instances of
        Indicator that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Indicator
          - A list or tuple of dicts of string/value properties that
            will be passed to the Indicator constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Indicator]
        """
        pass


    @property
    def isosurface(self):
        """
        The 'isosurface' property is a tuple of instances of
        Isosurface that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Isosurface
          - A list or tuple of dicts of string/value properties that
            will be passed to the Isosurface constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Isosurface]
        """
        pass


    @property
    def mesh3d(self):
        """
        The 'mesh3d' property is a tuple of instances of
        Mesh3d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Mesh3d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Mesh3d constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Mesh3d]
        """
        pass


    @property
    def ohlc(self):
        """
        The 'ohlc' property is a tuple of instances of
        Ohlc that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Ohlc
          - A list or tuple of dicts of string/value properties that
            will be passed to the Ohlc constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Ohlc]
        """
        pass


    @property
    def parcats(self):
        """
        The 'parcats' property is a tuple of instances of
        Parcats that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Parcats
          - A list or tuple of dicts of string/value properties that
            will be passed to the Parcats constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Parcats]
        """
        pass


    @property
    def parcoords(self):
        """
        The 'parcoords' property is a tuple of instances of
        Parcoords that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Parcoords
          - A list or tuple of dicts of string/value properties that
            will be passed to the Parcoords constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Parcoords]
        """
        pass


    @property
    def pie(self):
        """
        The 'pie' property is a tuple of instances of
        Pie that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Pie
          - A list or tuple of dicts of string/value properties that
            will be passed to the Pie constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Pie]
        """
        return self["pie"]

    @pie.setter
    def pie(self, val):
        self["pie"] = val

    @property
    def sankey(self):
        """
        The 'sankey' property is a tuple of instances of
        Sankey that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Sankey
          - A list or tuple of dicts of string/value properties that
            will be passed to the Sankey constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Sankey]
        """
        pass


    @property
    def scatter3d(self):
        """
        The 'scatter3d' property is a tuple of instances of
        Scatter3d that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatter3d
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatter3d constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatter3d]
        """
        pass


    @property
    def scattercarpet(self):
        """
        The 'scattercarpet' property is a tuple of instances of
        Scattercarpet that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattercarpet
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattercarpet constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattercarpet]
        """
        pass


    @property
    def scattergeo(self):
        """
        The 'scattergeo' property is a tuple of instances of
        Scattergeo that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattergeo
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattergeo constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattergeo]
        """
        pass


    @property
    def scattergl(self):
        """
        The 'scattergl' property is a tuple of instances of
        Scattergl that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattergl
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattergl constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattergl]
        """
        pass


    @property
    def scattermapbox(self):
        """
        The 'scattermapbox' property is a tuple of instances of
        Scattermapbox that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattermapbox
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattermapbox constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattermapbox]
        """
        pass


    @property
    def scattermap(self):
        """
        The 'scattermap' property is a tuple of instances of
        Scattermap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattermap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattermap constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattermap]
        """
        pass


    @property
    def scatterpolargl(self):
        """
        The 'scatterpolargl' property is a tuple of instances of
        Scatterpolargl that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterpolargl
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterpolargl constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterpolargl]
        """
        pass


    @property
    def scatterpolar(self):
        """
        The 'scatterpolar' property is a tuple of instances of
        Scatterpolar that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterpolar
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterpolar constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterpolar]
        """
        pass


    @property
    def scatter(self):
        """
        The 'scatter' property is a tuple of instances of
        Scatter that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatter
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatter constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatter]
        """
        return self["scatter"]

    @scatter.setter
    def scatter(self, val):
        self["scatter"] = val

    @property
    def scattersmith(self):
        """
        The 'scattersmith' property is a tuple of instances of
        Scattersmith that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scattersmith
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scattersmith constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scattersmith]
        """
        pass


    @property
    def scatterternary(self):
        """
        The 'scatterternary' property is a tuple of instances of
        Scatterternary that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Scatterternary
          - A list or tuple of dicts of string/value properties that
            will be passed to the Scatterternary constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Scatterternary]
        """
        pass


    @property
    def splom(self):
        """
        The 'splom' property is a tuple of instances of
        Splom that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Splom
          - A list or tuple of dicts of string/value properties that
            will be passed to the Splom constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Splom]
        """
        pass


    @property
    def streamtube(self):
        """
        The 'streamtube' property is a tuple of instances of
        Streamtube that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Streamtube
          - A list or tuple of dicts of string/value properties that
            will be passed to the Streamtube constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Streamtube]
        """
        pass


    @property
    def sunburst(self):
        """
        The 'sunburst' property is a tuple of instances of
        Sunburst that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Sunburst
          - A list or tuple of dicts of string/value properties that
            will be passed to the Sunburst constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Sunburst]
        """
        return self["sunburst"]

    @sunburst.setter
    def sunburst(self, val):
        self["sunburst"] = val

    @property
    def surface(self):
        """
        The 'surface' property is a tuple of instances of
        Surface that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Surface
          - A list or tuple of dicts of string/value properties that
            will be passed to the Surface constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Surface]
        """
        pass


    @property
    def table(self):
        """
        The 'table' property is a tuple of instances of
        Table that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Table
          - A list or tuple of dicts of string/value properties that
            will be passed to the Table constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Table]
        """
        pass


    @property
    def treemap(self):
        """
        The 'treemap' property is a tuple of instances of
        Treemap that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Treemap
          - A list or tuple of dicts of string/value properties that
            will be passed to the Treemap constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Treemap]
        """
        return self["treemap"]

    @treemap.setter
    def treemap(self, val):
        self["treemap"] = val

    @property
    def violin(self):
        """
        The 'violin' property is a tuple of instances of
        Violin that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Violin
          - A list or tuple of dicts of string/value properties that
            will be passed to the Violin constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Violin]
        """
        return self["violin"]

    @violin.setter
    def violin(self, val):
        self["violin"] = val

    @property
    def volume(self):
        """
        The 'volume' property is a tuple of instances of
        Volume that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Volume
          - A list or tuple of dicts of string/value properties that
            will be passed to the Volume constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Volume]
        """
        pass


    @property
    def waterfall(self):
        """
        The 'waterfall' property is a tuple of instances of
        Waterfall that may be specified as:
          - A list or tuple of instances of plotly.graph_objs.layout.template.data.Waterfall
          - A list or tuple of dicts of string/value properties that
            will be passed to the Waterfall constructor

        Returns
        -------
        tuple[plotly.graph_objs.layout.template.data.Waterfall]
        """
        pass



    def __init__(
        self,
        arg=None,
        barpolar=None,
        bar=None,
        box=None,
        candlestick=None,
        carpet=None,
        choroplethmapbox=None,
        choroplethmap=None,
        choropleth=None,
        cone=None,
        contourcarpet=None,
        contour=None,
        densitymapbox=None,
        densitymap=None,
        funnelarea=None,
        funnel=None,
        heatmap=None,
        histogram2dcontour=None,
        histogram2d=None,
        histogram=None,
        icicle=None,
        image=None,
        indicator=None,
        isosurface=None,
        mesh3d=None,
        ohlc=None,
        parcats=None,
        parcoords=None,
        pie=None,
        sankey=None,
        scatter3d=None,
        scattercarpet=None,
        scattergeo=None,
        scattergl=None,
        scattermapbox=None,
        scattermap=None,
        scatterpolargl=None,
        scatterpolar=None,
        scatter=None,
        scattersmith=None,
        scatterternary=None,
        splom=None,
        streamtube=None,
        sunburst=None,
        surface=None,
        table=None,
        treemap=None,
        violin=None,
        volume=None,
        waterfall=None,
        **kwargs,
    ):
        """
        Construct a new Data object

        Parameters
        ----------
        arg
            dict of properties compatible with this constructor or
            an instance of
            :class:`plotly.graph_objs.layout.template.Data`
        barpolar
            A tuple of :class:`plotly.graph_objects.Barpolar`
            instances or dicts with compatible properties
        bar
            A tuple of :class:`plotly.graph_objects.Bar` instances
            or dicts with compatible properties
        box
            A tuple of :class:`plotly.graph_objects.Box` instances
            or dicts with compatible properties
        candlestick
            A tuple of :class:`plotly.graph_objects.Candlestick`
            instances or dicts with compatible properties
        carpet
            A tuple of :class:`plotly.graph_objects.Carpet`
            instances or dicts with compatible properties
        choroplethmapbox
            A tuple of
            :class:`plotly.graph_objects.Choroplethmapbox`
            instances or dicts with compatible properties
        choroplethmap
            A tuple of :class:`plotly.graph_objects.Choroplethmap`
            instances or dicts with compatible properties
        choropleth
            A tuple of :class:`plotly.graph_objects.Choropleth`
            instances or dicts with compatible properties
        cone
            A tuple of :class:`plotly.graph_objects.Cone` instances
            or dicts with compatible properties
        contourcarpet
            A tuple of :class:`plotly.graph_objects.Contourcarpet`
            instances or dicts with compatible properties
        contour
            A tuple of :class:`plotly.graph_objects.Contour`
            instances or dicts with compatible properties
        densitymapbox
            A tuple of :class:`plotly.graph_objects.Densitymapbox`
            instances or dicts with compatible properties
        densitymap
            A tuple of :class:`plotly.graph_objects.Densitymap`
            instances or dicts with compatible properties
        funnelarea
            A tuple of :class:`plotly.graph_objects.Funnelarea`
            instances or dicts with compatible properties
        funnel
            A tuple of :class:`plotly.graph_objects.Funnel`
            instances or dicts with compatible properties
        heatmap
            A tuple of :class:`plotly.graph_objects.Heatmap`
            instances or dicts with compatible properties
        histogram2dcontour
            A tuple of
            :class:`plotly.graph_objects.Histogram2dContour`
            instances or dicts with compatible properties
        histogram2d
            A tuple of :class:`plotly.graph_objects.Histogram2d`
            instances or dicts with compatible properties
        histogram
            A tuple of :class:`plotly.graph_objects.Histogram`
            instances or dicts with compatible properties
        icicle
            A tuple of :class:`plotly.graph_objects.Icicle`
            instances or dicts with compatible properties
        image
            A tuple of :class:`plotly.graph_objects.Image`
            instances or dicts with compatible properties
        indicator
            A tuple of :class:`plotly.graph_objects.Indicator`
            instances or dicts with compatible properties
        isosurface
            A tuple of :class:`plotly.graph_objects.Isosurface`
            instances or dicts with compatible properties
        mesh3d
            A tuple of :class:`plotly.graph_objects.Mesh3d`
            instances or dicts with compatible properties
        ohlc
            A tuple of :class:`plotly.graph_objects.Ohlc` instances
            or dicts with compatible properties
        parcats
            A tuple of :class:`plotly.graph_objects.Parcats`
            instances or dicts with compatible properties
        parcoords
            A tuple of :class:`plotly.graph_objects.Parcoords`
            instances or dicts with compatible properties
        pie
            A tuple of :class:`plotly.graph_objects.Pie` instances
            or dicts with compatible properties
        sankey
            A tuple of :class:`plotly.graph_objects.Sankey`
            instances or dicts with compatible properties
        scatter3d
            A tuple of :class:`plotly.graph_objects.Scatter3d`
            instances or dicts with compatible properties
        scattercarpet
            A tuple of :class:`plotly.graph_objects.Scattercarpet`
            instances or dicts with compatible properties
        scattergeo
            A tuple of :class:`plotly.graph_objects.Scattergeo`
            instances or dicts with compatible properties
        scattergl
            A tuple of :class:`plotly.graph_objects.Scattergl`
            instances or dicts with compatible properties
        scattermapbox
            A tuple of :class:`plotly.graph_objects.Scattermapbox`
            instances or dicts with compatible properties
        scattermap
            A tuple of :class:`plotly.graph_objects.Scattermap`
            instances or dicts with compatible properties
        scatterpolargl
            A tuple of :class:`plotly.graph_objects.Scatterpolargl`
            instances or dicts with compatible properties
        scatterpolar
            A tuple of :class:`plotly.graph_objects.Scatterpolar`
            instances or dicts with compatible properties
        scatter
            A tuple of :class:`plotly.graph_objects.Scatter`
            instances or dicts with compatible properties
        scattersmith
            A tuple of :class:`plotly.graph_objects.Scattersmith`
            instances or dicts with compatible properties
        scatterternary
            A tuple of :class:`plotly.graph_objects.Scatterternary`
            instances or dicts with compatible properties
        splom
            A tuple of :class:`plotly.graph_objects.Splom`
            instances or dicts with compatible properties
        streamtube
            A tuple of :class:`plotly.graph_objects.Streamtube`
            instances or dicts with compatible properties
        sunburst
            A tuple of :class:`plotly.graph_objects.Sunburst`
            instances or dicts with compatible properties
        surface
            A tuple of :class:`plotly.graph_objects.Surface`
            instances or dicts with compatible properties
        table
            A tuple of :class:`plotly.graph_objects.Table`
            instances or dicts with compatible properties
        treemap
            A tuple of :class:`plotly.graph_objects.Treemap`
            instances or dicts with compatible properties
        violin
            A tuple of :class:`plotly.graph_objects.Violin`
            instances or dicts with compatible properties
        volume
            A tuple of :class:`plotly.graph_objects.Volume`
            instances or dicts with compatible properties
        waterfall
            A tuple of :class:`plotly.graph_objects.Waterfall`
            instances or dicts with compatible properties

        Returns
        -------
        Data
        """
        super().__init__("data")
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
The first argument to the plotly.graph_objs.layout.template.Data
constructor must be a dict or
an instance of :class:`plotly.graph_objs.layout.template.Data`""")

        self._skip_invalid = kwargs.pop("skip_invalid", False)
        self._validate = kwargs.pop("_validate", True)

        self._set_property("barpolar", arg, barpolar)
        self._set_property("bar", arg, bar)
        self._set_property("box", arg, box)
        self._set_property("candlestick", arg, candlestick)
        self._set_property("carpet", arg, carpet)
        self._set_property("choroplethmapbox", arg, choroplethmapbox)
        self._set_property("choroplethmap", arg, choroplethmap)
        self._set_property("choropleth", arg, choropleth)
        self._set_property("cone", arg, cone)
        self._set_property("contourcarpet", arg, contourcarpet)
        self._set_property("contour", arg, contour)
        self._set_property("densitymapbox", arg, densitymapbox)
        self._set_property("densitymap", arg, densitymap)
        self._set_property("funnelarea", arg, funnelarea)
        self._set_property("funnel", arg, funnel)
        self._set_property("heatmap", arg, heatmap)
        self._set_property("histogram2dcontour", arg, histogram2dcontour)
        self._set_property("histogram2d", arg, histogram2d)
        self._set_property("histogram", arg, histogram)
        self._set_property("icicle", arg, icicle)
        self._set_property("image", arg, image)
        self._set_property("indicator", arg, indicator)
        self._set_property("isosurface", arg, isosurface)
        self._set_property("mesh3d", arg, mesh3d)
        self._set_property("ohlc", arg, ohlc)
        self._set_property("parcats", arg, parcats)
        self._set_property("parcoords", arg, parcoords)
        self._set_property("pie", arg, pie)
        self._set_property("sankey", arg, sankey)
        self._set_property("scatter3d", arg, scatter3d)
        self._set_property("scattercarpet", arg, scattercarpet)
        self._set_property("scattergeo", arg, scattergeo)
        self._set_property("scattergl", arg, scattergl)
        self._set_property("scattermapbox", arg, scattermapbox)
        self._set_property("scattermap", arg, scattermap)
        self._set_property("scatterpolargl", arg, scatterpolargl)
        self._set_property("scatterpolar", arg, scatterpolar)
        self._set_property("scatter", arg, scatter)
        self._set_property("scattersmith", arg, scattersmith)
        self._set_property("scatterternary", arg, scatterternary)
        self._set_property("splom", arg, splom)
        self._set_property("streamtube", arg, streamtube)
        self._set_property("sunburst", arg, sunburst)
        self._set_property("surface", arg, surface)
        self._set_property("table", arg, table)
        self._set_property("treemap", arg, treemap)
        self._set_property("violin", arg, violin)
        self._set_property("volume", arg, volume)
        self._set_property("waterfall", arg, waterfall)
        self._process_kwargs(**dict(arg, **kwargs))
        self._skip_invalid = False
