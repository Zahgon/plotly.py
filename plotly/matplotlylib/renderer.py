"""
Renderer Module

This module defines the PlotlyRenderer class and a single function,
fig_to_plotly, which is intended to be the main way that user's will interact
with the matplotlylib package.

"""

import warnings

import plotly.graph_objs as go
from plotly.matplotlylib.mplexporter import Renderer
from plotly.matplotlylib import mpltools


class PlotlyRenderer(Renderer):
    """A renderer class inheriting from base for rendering mpl plots in plotly.

    A renderer class to be used with an exporter for rendering matplotlib
    plots in Plotly. This module defines the PlotlyRenderer class which handles
    the creation of the JSON structures that get sent to plotly.

    All class attributes available are defined in __init__().

    Basic Usage:

    # (mpl code) #
    fig = gcf()
    renderer = PlotlyRenderer(fig)
    exporter = Exporter(renderer)
    exporter.run(fig)  # ... et voila

    """

    def __init__(self):
        """Initialize PlotlyRenderer obj.

        PlotlyRenderer obj is called on by an Exporter object to draw
        matplotlib objects like figures, axes, text, etc.

        All class attributes are listed here in the __init__ method.

        """
        self.plotly_fig = go.Figure()
        self.mpl_fig = None
        self.current_mpl_ax = None
        self.bar_containers = None
        self.current_bars = []
        self.axis_ct = 0
        self.x_is_mpl_date = False
        self.mpl_x_bounds = (0, 1)
        self.mpl_y_bounds = (0, 1)
        self.msg = "Initialized PlotlyRenderer\n"
        self._processing_legend = False
        self._legend_visible = False

    def open_figure(self, fig, props):
        """Creates a new figure by beginning to fill out layout dict.

        The 'autosize' key is set to false so that the figure will mirror
        sizes set by mpl. The 'hovermode' key controls what shows up when you
        mouse around a figure in plotly, it's set to show the 'closest' point.

        Positional agurments:
        fig -- a matplotlib.figure.Figure object.
        props.keys(): [
            'figwidth',
            'figheight',
            'dpi'
            ]

        """
        pass

    def close_figure(self, fig):
        """Closes figure by cleaning up data and layout dictionaries.

        The PlotlyRenderer's job is to create an appropriate set of data and
        layout dictionaries. When the figure is closed, some cleanup and
        repair is necessary. This method removes inappropriate dictionary
        entries, freeing up Plotly to use defaults and best judgements to
        complete the entries. This method is called by an Exporter object.

        Positional arguments:
        fig -- a matplotlib.figure.Figure object.

        """
        pass

    def open_axes(self, ax, props):
        """Setup a new axes object (subplot in plotly).

        Plotly stores information about subplots in different 'xaxis' and
        'yaxis' objects which are numbered. These are just dictionaries
        included in the layout dictionary. This function takes information
        from the Exporter, fills in appropriate dictionary entries,
        and updates the layout dictionary. PlotlyRenderer keeps track of the
        number of plots by incrementing the axis_ct attribute.

        Setting the proper plot domain in plotly is a bit tricky. Refer to
        the documentation for mpltools.convert_x_domain and
        mpltools.convert_y_domain.

        Positional arguments:
        ax -- an mpl axes object. This will become a subplot in plotly.
        props.keys() -- [
            'axesbg',           (background color for axes obj)
            'axesbgalpha',      (alpha, or opacity for background)
            'bounds',           ((x0, y0, width, height) for axes)
            'dynamic',          (zoom/pan-able?)
            'axes',             (list: [xaxis, yaxis])
            'xscale',           (log, linear, or date)
            'yscale',
            'xlim',             (range limits for x)
            'ylim',
            'xdomain'           (xdomain=xlim, unless it's a date)
            'ydomain'
            ]

        """
        pass

    def close_axes(self, ax):
        """Close the axes object and clean up.

        Bars from bar charts are given to PlotlyRenderer one-by-one,
        thus they need to be taken care of at the close of each axes object.
        The self.current_bars variable should be empty unless a bar
        chart has been created.

        Positional arguments:
        ax -- an mpl axes object, not required at this time.

        """
        pass

    def open_legend(self, legend, props):
        """Enable Plotly's native legend when matplotlib legend is detected.

        This method is called when a matplotlib legend is found. It enables
        Plotly's showlegend only if the matplotlib legend is visible.

        Positional arguments:
        legend -- matplotlib.legend.Legend object
        props -- legend properties dictionary
        """
        pass

    def close_legend(self, legend):
        """Finalize legend processing.

        Positional arguments:
        legend -- matplotlib.legend.Legend object
        """
        pass


    def draw_bar(self, coll):
        """Draw a collection of similar patches as a bar chart.

        After bars are sorted, an appropriate data dictionary must be created
        to tell plotly about this data. Just like draw_line or draw_markers,
        draw_bar translates patch/path information into something plotly
        understands.

        Positional arguments:
        patch_coll -- a collection of patches to be drawn as a bar chart.

        """
        pass

    def draw_marked_line(self, **props):
        """Create a data dict for a line obj.

        This will draw 'lines', 'markers', or 'lines+markers'. For legend elements,
        this will use layout.shapes, so they can be positioned with paper refs.

        props.keys() -- [
        'coordinates',  ('data', 'axes', 'figure', or 'display')
        'data',         (a list of xy pairs)
        'mplobj',       (the matplotlib.lines.Line2D obj being rendered)
        'label',        (the name of the Line2D obj being rendered)
        'linestyle',    (linestyle dict, can be None, see below)
        'markerstyle',  (markerstyle dict, can be None, see below)
        ]

        props['linestyle'].keys() -- [
        'alpha',        (opacity of Line2D obj)
        'color',        (color of the line if it exists, not the marker)
        'linewidth',
        'dasharray',    (code for linestyle, see DASH_MAP in mpltools.py)
        'zorder',       (viewing precedence when stacked with other objects)
        ]

        props['markerstyle'].keys() -- [
        'alpha',        (opacity of Line2D obj)
        'marker',       (the mpl marker symbol, see SYMBOL_MAP in mpltools.py)
        'facecolor',    (color of the marker face)
        'edgecolor',    (color of the marker edge)
        'edgewidth',    (width of marker edge)
        'markerpath',   (an SVG path for drawing the specified marker)
        'zorder',       (viewing precedence when stacked with other objects)
        ]

        """
        pass

    def draw_image(self, **props):
        """Draw image.

        Not implemented yet!

        """
        pass

    def draw_path_collection(self, **props):
        """Add a path collection to data list as a scatter plot.

        Current implementation defaults such collections as scatter plots.
        Matplotlib supports collections that have many of the same parameters
        in common like color, size, path, etc. However, they needn't all be
        the same. Plotly does not currently support such functionality and
        therefore, the style for the first object is taken and used to define
        the remaining paths in the collection.

        props.keys() -- [
        'paths',                (structure: [vertices, path_code])
        'path_coordinates',     ('data', 'axes', 'figure', or 'display')
        'path_transforms',      (mpl transform, including Affine2D matrix)
        'offsets',              (offset from axes, helpful if in 'data')
        'offset_coordinates',   ('data', 'axes', 'figure', or 'display')
        'offset_order',
        'styles',               (style dict, see below)
        'mplobj'                (the collection obj being drawn)
        ]

        props['styles'].keys() -- [
        'linewidth',            (one or more linewidths)
        'facecolor',            (one or more facecolors for path)
        'edgecolor',            (one or more edgecolors for path)
        'alpha',                (one or more opacites for path)
        'zorder',               (precedence when stacked)
        ]

        """
        pass

    def draw_path(self, **props):
        """Draw path, currently only attempts to draw bar charts.

        This function attempts to sort a given path into a collection of
        horizontal or vertical bar charts. Most of the actual code takes
        place in functions from mpltools.py.

        props.keys() -- [
        'data',         (a list of vertices for the path)
        'coordinates',  ('data', 'axes', 'figure', or 'display')
        'pathcodes',    (code for the path, structure: ['M', 'L', 'Z', etc.])
        'style',        (style dict, see below)
        'mplobj'        (the mpl path object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of path obj)
        'edgecolor',
        'facecolor',
        'edgewidth',
        'dasharray',    (style for path's enclosing line)
        'zorder'        (precedence of obj when stacked)
        ]

        """
        pass

    def draw_text(self, **props):
        """Create an annotation dict for a text obj.

        Currently, plotly uses either 'page' or 'data' to reference
        annotation locations. These refer to 'display' and 'data',
        respectively for the 'coordinates' key used in the Exporter.
        Appropriate measures are taken to transform text locations to
        reference one of these two options.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        pass

    def draw_title(self, **props):
        """Add a title to the current subplot in layout dictionary.

        If there exists more than a single plot in the figure, titles revert
        to 'page'-referenced annotations.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        pass

    def draw_xlabel(self, **props):
        """Add an xaxis label to the current subplot in layout dictionary.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        pass

    def draw_ylabel(self, **props):
        """Add a yaxis label to the current subplot in layout dictionary.

        props.keys() -- [
        'text',         (actual content string, not the text obj)
        'position',     (an x, y pair, not an mpl Bbox)
        'coordinates',  ('data', 'axes', 'figure', 'display')
        'text_type',    ('title', 'xlabel', or 'ylabel')
        'style',        (style dict, see below)
        'mplobj'        (actual mpl text object)
        ]

        props['style'].keys() -- [
        'alpha',        (opacity of text)
        'fontsize',     (size in points of text)
        'color',        (hex color)
        'halign',       (horizontal alignment, 'left', 'center', or 'right')
        'valign',       (vertical alignment, 'baseline', 'center', or 'top')
        'rotation',
        'zorder',       (precedence of text when stacked with other objs)
        ]

        """
        pass

    def resize(self):
        """Revert figure layout to allow plotly to resize.

        By default, PlotlyRenderer tries its hardest to precisely mimic an
        mpl figure. However, plotly is pretty good with aesthetics. By
        running PlotlyRenderer.resize(), layout parameters are deleted. This
        lets plotly choose them instead of mpl.

        """
        pass

