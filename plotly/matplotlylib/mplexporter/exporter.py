"""
Matplotlib Exporter
===================
This submodule contains tools for crawling a matplotlib figure and exporting
relevant pieces to a renderer.
"""

import warnings
import io
from . import utils

import matplotlib
from matplotlib import transforms
from matplotlib.backends.backend_agg import FigureCanvasAgg


class Exporter(object):
    """Matplotlib Exporter

    Parameters
    ----------
    renderer : Renderer object
        The renderer object called by the exporter to create a figure
        visualization.  See mplexporter.Renderer for information on the
        methods which should be defined within the renderer.
    close_mpl : bool
        If True (default), close the matplotlib figure as it is rendered. This
        is useful for when the exporter is used within the notebook, or with
        an interactive matplotlib backend.
    """

    def __init__(self, renderer, close_mpl=True):
        self.close_mpl = close_mpl
        self.renderer = renderer

    def run(self, fig):
        """
        Run the exporter on the given figure

        Parmeters
        ---------
        fig : matplotlib.Figure instance
            The figure to export
        """
        pass

    @staticmethod
    def process_transform(
        transform, ax=None, data=None, return_trans=False, force_trans=None
    ):
        """Process the transform and convert data to figure or data coordinates

        Parameters
        ----------
        transform : matplotlib Transform object
            The transform applied to the data
        ax : matplotlib Axes object (optional)
            The axes the data is associated with
        data : ndarray (optional)
            The array of data to be transformed.
        return_trans : bool (optional)
            If true, return the final transform of the data
        force_trans : matplotlib.transform instance (optional)
            If supplied, first force the data to this transform

        Returns
        -------
        code : string
            Code is either "data", "axes", "figure", or "display", indicating
            the type of coordinates output.
        transform : matplotlib transform
            the transform used to map input data to output data.
            Returned only if return_trans is True
        new_data : ndarray
            Data transformed to match the given coordinate code.
            Returned only if data is specified
        """
        pass

    def crawl_fig(self, fig):
        """Crawl the figure and process all axes"""
        pass

    def crawl_ax(self, ax):
        """Crawl the axes and process all elements within"""
        pass

    def crawl_legend(self, ax, legend):
        """
        Recursively look through objects in legend children
        """
        pass

    def draw_line(self, ax, line, force_trans=None):
        """Process a matplotlib line and call renderer.draw_line"""
        pass

    def draw_text(self, ax, text, force_trans=None, text_type=None):
        """Process a matplotlib text object and call renderer.draw_text"""
        pass

    def draw_patch(self, ax, patch, force_trans=None):
        """Process a matplotlib patch object and call renderer.draw_path"""
        pass

    def draw_collection(
        self, ax, collection, force_pathtrans=None, force_offsettrans=None
    ):
        """Process a matplotlib collection and call renderer.draw_collection"""
        pass

    def draw_image(self, ax, image):
        """Process a matplotlib image object and call renderer.draw_image"""
        pass
