from collections import OrderedDict

from plotly import exceptions, optional_imports
from plotly.graph_objs import graph_objs

# Optional imports, may be None for users that only use our core functionality.
np = optional_imports.get_module("numpy")
scp = optional_imports.get_module("scipy")
sch = optional_imports.get_module("scipy.cluster.hierarchy")
scs = optional_imports.get_module("scipy.spatial")


def create_dendrogram(
    X,
    orientation="bottom",
    labels=None,
    colorscale=None,
    distfun=None,
    linkagefun=lambda x: sch.linkage(x, "complete"),
    hovertext=None,
    color_threshold=None,
):
    """
    Function that returns a dendrogram Plotly figure object. This is a thin
    wrapper around scipy.cluster.hierarchy.dendrogram.

    See also https://dash.plot.ly/dash-bio/clustergram.

    :param (ndarray) X: Matrix of observations as array of arrays
    :param (str) orientation: 'top', 'right', 'bottom', or 'left'
    :param (list) labels: List of axis category labels(observation labels)
    :param (list) colorscale: Optional colorscale for the dendrogram tree.
                              Requires 8 colors to be specified, the 7th of
                              which is ignored.  With scipy>=1.5.0, the 2nd, 3rd
                              and 6th are used twice as often as the others.
                              Given a shorter list, the missing values are
                              replaced with defaults and with a longer list the
                              extra values are ignored.
    :param (function) distfun: Function to compute the pairwise distance from
                               the observations
    :param (function) linkagefun: Function to compute the linkage matrix from
                               the pairwise distances
    :param (list[list]) hovertext: List of hovertext for constituent traces of dendrogram
                               clusters
    :param (double) color_threshold: Value at which the separation of clusters will be made

    Example 1: Simple bottom oriented dendrogram

    >>> from plotly.figure_factory import create_dendrogram

    >>> import numpy as np

    >>> X = np.random.rand(10,10)
    >>> fig = create_dendrogram(X)
    >>> fig.show()

    Example 2: Dendrogram to put on the left of the heatmap

    >>> from plotly.figure_factory import create_dendrogram

    >>> import numpy as np

    >>> X = np.random.rand(5,5)
    >>> names = ['Jack', 'Oxana', 'John', 'Chelsea', 'Mark']
    >>> dendro = create_dendrogram(X, orientation='right', labels=names)
    >>> dendro.update_layout({'width':700, 'height':500}) # doctest: +SKIP
    >>> dendro.show()

    Example 3: Dendrogram with Pandas

    >>> from plotly.figure_factory import create_dendrogram

    >>> import numpy as np
    >>> import pandas as pd

    >>> Index= ['A','B','C','D','E','F','G','H','I','J']
    >>> df = pd.DataFrame(abs(np.random.randn(10, 10)), index=Index)
    >>> fig = create_dendrogram(df, labels=Index)
    >>> fig.show()
    """
    pass


class _Dendrogram(object):
    """Refer to FigureFactory.create_dendrogram() for docstring."""

    def __init__(
        self,
        X,
        orientation="bottom",
        labels=None,
        colorscale=None,
        width=np.inf,
        height=np.inf,
        xaxis="xaxis",
        yaxis="yaxis",
        distfun=None,
        linkagefun=lambda x: sch.linkage(x, "complete"),
        hovertext=None,
        color_threshold=None,
    ):
        self.orientation = orientation
        self.labels = labels
        self.xaxis = xaxis
        self.yaxis = yaxis
        self.data = []
        self.leaves = []
        self.sign = {self.xaxis: 1, self.yaxis: 1}
        self.layout = {self.xaxis: {}, self.yaxis: {}}

        if self.orientation in ["left", "bottom"]:
            self.sign[self.xaxis] = 1
        else:
            self.sign[self.xaxis] = -1

        if self.orientation in ["right", "bottom"]:
            self.sign[self.yaxis] = 1
        else:
            self.sign[self.yaxis] = -1

        if distfun is None:
            distfun = scs.distance.pdist

        (dd_traces, xvals, yvals, ordered_labels, leaves) = self.get_dendrogram_traces(
            X, colorscale, distfun, linkagefun, hovertext, color_threshold
        )

        self.labels = ordered_labels
        self.leaves = leaves
        yvals_flat = yvals.flatten()
        xvals_flat = xvals.flatten()

        self.zero_vals = []

        for i in range(len(yvals_flat)):
            if yvals_flat[i] == 0.0 and xvals_flat[i] not in self.zero_vals:
                self.zero_vals.append(xvals_flat[i])

        if len(self.zero_vals) > len(yvals) + 1:
            # If the length of zero_vals is larger than the length of yvals,
            # it means that there are wrong vals because of the identicial samples.
            # Three and more identicial samples will make the yvals of spliting
            # center into 0 and it will accidentally take it as leaves.
            l_border = int(min(self.zero_vals))
            r_border = int(max(self.zero_vals))
            correct_leaves_pos = range(
                l_border, r_border + 1, int((r_border - l_border) / len(yvals))
            )
            # Regenerating the leaves pos from the self.zero_vals with equally intervals.
            self.zero_vals = [v for v in correct_leaves_pos]

        self.zero_vals.sort()
        self.layout = self.set_figure_layout(width, height)
        self.data = dd_traces

    def get_color_dict(self, colorscale):
        """
        Returns colorscale used for dendrogram tree clusters.

        :param (list) colorscale: Colors to use for the plot in rgb format.
        :rtype (dict): A dict of default colors mapped to the user colorscale.

        """
        pass

    def set_axis_layout(self, axis_key):
        """
        Sets and returns default axis object for dendrogram figure.

        :param (str) axis_key: E.g., 'xaxis', 'xaxis1', 'yaxis', yaxis1', etc.
        :rtype (dict): An axis_key dictionary with set parameters.

        """
        pass

    def set_figure_layout(self, width, height):
        """
        Sets and returns default layout object for dendrogram figure.

        """
        pass

    def get_dendrogram_traces(
        self, X, colorscale, distfun, linkagefun, hovertext, color_threshold
    ):
        """
        Calculates all the elements needed for plotting a dendrogram.

        :param (ndarray) X: Matrix of observations as array of arrays
        :param (list) colorscale: Color scale for dendrogram tree clusters
        :param (function) distfun: Function to compute the pairwise distance
                                   from the observations
        :param (function) linkagefun: Function to compute the linkage matrix
                                      from the pairwise distances
        :param (list) hovertext: List of hovertext for constituent traces of dendrogram
        :rtype (tuple): Contains all the traces in the following order:
            (a) trace_list: List of Plotly trace objects for dendrogram tree
            (b) icoord: All X points of the dendrogram tree as array of arrays
                with length 4
            (c) dcoord: All Y points of the dendrogram tree as array of arrays
                with length 4
            (d) ordered_labels: leaf labels in the order they are going to
                appear on the plot
            (e) P['leaves']: left-to-right traversal of the leaves

        """
        pass
