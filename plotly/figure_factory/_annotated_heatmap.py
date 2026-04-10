import plotly.colors as clrs
from plotly import exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs
from plotly.validator_cache import ValidatorCache

# Optional imports, may be None for users that only use our core functionality.
np = optional_imports.get_module("numpy")


def validate_annotated_heatmap(z, x, y, annotation_text):
    """
    Annotated-heatmap-specific validations

    Check that if a text matrix is supplied, it has the same
    dimensions as the z matrix.

    See FigureFactory.create_annotated_heatmap() for params

    :raises: (PlotlyError) If z and text matrices do not  have the same
        dimensions.
    """
    pass


def create_annotated_heatmap(
    z,
    x=None,
    y=None,
    annotation_text=None,
    colorscale="Plasma",
    font_colors=None,
    showscale=False,
    reversescale=False,
    **kwargs,
):
    """
    **deprecated**, use instead
    :func:`plotly.express.imshow`.

    Function that creates annotated heatmaps

    This function adds annotations to each cell of the heatmap.

    :param (list[list]|ndarray) z: z matrix to create heatmap.
    :param (list) x: x axis labels.
    :param (list) y: y axis labels.
    :param (list[list]|ndarray) annotation_text: Text strings for
        annotations. Should have the same dimensions as the z matrix. If no
        text is added, the values of the z matrix are annotated. Default =
        z matrix values.
    :param (list|str) colorscale: heatmap colorscale.
    :param (list) font_colors: List of two color strings: [min_text_color,
        max_text_color] where min_text_color is applied to annotations for
        heatmap values < (max_value - min_value)/2. If font_colors is not
        defined, the colors are defined logically as black or white
        depending on the heatmap's colorscale.
    :param (bool) showscale: Display colorscale. Default = False
    :param (bool) reversescale: Reverse colorscale. Default = False
    :param kwargs: kwargs passed through plotly.graph_objs.Heatmap.
        These kwargs describe other attributes about the annotated Heatmap
        trace such as the colorscale. For more information on valid kwargs
        call help(plotly.graph_objs.Heatmap)

    Example 1: Simple annotated heatmap with default configuration

    >>> import plotly.figure_factory as ff

    >>> z = [[0.300000, 0.00000, 0.65, 0.300000],
    ...      [1, 0.100005, 0.45, 0.4300],
    ...      [0.300000, 0.00000, 0.65, 0.300000],
    ...      [1, 0.100005, 0.45, 0.00000]]

    >>> fig = ff.create_annotated_heatmap(z)
    >>> fig.show()
    """
    pass






class _AnnotatedHeatmap(object):
    """
    Refer to TraceFactory.create_annotated_heatmap() for docstring
    """

    def __init__(
        self, z, x, y, annotation_text, colorscale, font_colors, reversescale, **kwargs
    ):
        self.z = z
        if x:
            self.x = x
        else:
            self.x = range(len(z[0]))
        if y:
            self.y = y
        else:
            self.y = range(len(z))
        if annotation_text is not None:
            self.annotation_text = annotation_text
        else:
            self.annotation_text = self.z
        self.colorscale = colorscale
        self.reversescale = reversescale
        self.font_colors = font_colors

        if np and isinstance(self.z, np.ndarray):
            self.zmin = np.amin(self.z)
            self.zmax = np.amax(self.z)
        else:
            self.zmin = min([v for row in self.z for v in row])
            self.zmax = max([v for row in self.z for v in row])

        if kwargs.get("zmin", None) is not None:
            self.zmin = kwargs["zmin"]
        if kwargs.get("zmax", None) is not None:
            self.zmax = kwargs["zmax"]

        self.zmid = (self.zmax + self.zmin) / 2

        if kwargs.get("zmid", None) is not None:
            self.zmid = kwargs["zmid"]

    def get_text_color(self):
        """
        Get font color for annotations.

        The annotated heatmap can feature two text colors: min_text_color and
        max_text_color. The min_text_color is applied to annotations for
        heatmap values < (max_value - min_value)/2. The user can define these
        two colors. Otherwise the colors are defined logically as black or
        white depending on the heatmap's colorscale.

        :rtype (string, string) min_text_color, max_text_color: text
            color for annotations for heatmap values <
            (max_value - min_value)/2 and text color for annotations for
            heatmap values >= (max_value - min_value)/2
        """
        pass

    def make_annotations(self):
        """
        Get annotations for each cell of the heatmap with graph_objs.Annotation

        :rtype (list[dict]) annotations: list of annotations for each cell of
            the heatmap
        """
        pass
