"""
tools
=====

Functions that USERS will possibly want access to.

"""

import json
import warnings

import os

from plotly import exceptions, optional_imports
from plotly.files import PLOTLY_DIR

DEFAULT_PLOTLY_COLORS = [
    "rgb(31, 119, 180)",
    "rgb(255, 127, 14)",
    "rgb(44, 160, 44)",
    "rgb(214, 39, 40)",
    "rgb(148, 103, 189)",
    "rgb(140, 86, 75)",
    "rgb(227, 119, 194)",
    "rgb(127, 127, 127)",
    "rgb(188, 189, 34)",
    "rgb(23, 190, 207)",
]


REQUIRED_GANTT_KEYS = ["Task", "Start", "Finish"]
PLOTLY_SCALES = {
    "Greys": ["rgb(0,0,0)", "rgb(255,255,255)"],
    "YlGnBu": ["rgb(8,29,88)", "rgb(255,255,217)"],
    "Greens": ["rgb(0,68,27)", "rgb(247,252,245)"],
    "YlOrRd": ["rgb(128,0,38)", "rgb(255,255,204)"],
    "Bluered": ["rgb(0,0,255)", "rgb(255,0,0)"],
    "RdBu": ["rgb(5,10,172)", "rgb(178,10,28)"],
    "Reds": ["rgb(220,220,220)", "rgb(178,10,28)"],
    "Blues": ["rgb(5,10,172)", "rgb(220,220,220)"],
    "Picnic": ["rgb(0,0,255)", "rgb(255,0,0)"],
    "Rainbow": ["rgb(150,0,90)", "rgb(255,0,0)"],
    "Portland": ["rgb(12,51,131)", "rgb(217,30,30)"],
    "Jet": ["rgb(0,0,131)", "rgb(128,0,0)"],
    "Hot": ["rgb(0,0,0)", "rgb(255,255,255)"],
    "Blackbody": ["rgb(0,0,0)", "rgb(160,200,255)"],
    "Earth": ["rgb(0,0,130)", "rgb(255,255,255)"],
    "Electric": ["rgb(0,0,0)", "rgb(255,250,220)"],
    "Viridis": ["rgb(68,1,84)", "rgb(253,231,37)"],
}

# color constants for violin plot
DEFAULT_FILLCOLOR = "#1f77b4"
DEFAULT_HISTNORM = "probability density"
ALTERNATIVE_HISTNORM = "probability"


### mpl-related tools ###
def mpl_to_plotly(fig, resize=False, strip_style=False, verbose=False):
    """Convert a matplotlib figure to plotly dictionary and send.

    All available information about matplotlib visualizations are stored
    within a matplotlib.figure.Figure object. You can create a plot in python
    using matplotlib, store the figure object, and then pass this object to
    the fig_to_plotly function. In the background, mplexporter is used to
    crawl through the mpl figure object for appropriate information. This
    information is then systematically sent to the PlotlyRenderer which
    creates the JSON structure used to make plotly visualizations. Finally,
    these dictionaries are sent to plotly and your browser should open up a
    new tab for viewing! Optionally, if you're working in IPython, you can
    set notebook=True and the PlotlyRenderer will call plotly.iplot instead
    of plotly.plot to have the graph appear directly in the IPython notebook.

    Note, this function gives the user access to a simple, one-line way to
    render an mpl figure in plotly. If you need to trouble shoot, you can do
    this step manually by NOT running this fuction and entereing the following:

    ===========================================================================
    from plotly.matplotlylib import mplexporter, PlotlyRenderer

    # create an mpl figure and store it under a varialble 'fig'

    renderer = PlotlyRenderer()
    exporter = mplexporter.Exporter(renderer)
    exporter.run(fig)
    ===========================================================================

    You can then inspect the JSON structures by accessing these:

    renderer.layout -- a plotly layout dictionary
    renderer.data -- a list of plotly data dictionaries
    """
    pass


### graph_objs related tools ###


def get_subplots(rows=1, columns=1, print_grid=False, **kwargs):
    """Return a dictionary instance with the subplots set in 'layout'.

    Example 1:
    # stack two subplots vertically
    fig = tools.get_subplots(rows=2)
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x1', yaxis='y1')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 2:
    # print out string showing the subplot grid you've put in the layout
    fig = tools.get_subplots(rows=3, columns=2, print_grid=True)

    Keywords arguments with constant defaults:

    rows (kwarg, int greater than 0, default=1):
        Number of rows, evenly spaced vertically on the figure.

    columns (kwarg, int greater than 0, default=1):
        Number of columns, evenly spaced horizontally on the figure.

    horizontal_spacing (kwarg, float in [0,1], default=0.1):
        Space between subplot columns. Applied to all columns.

    vertical_spacing (kwarg, float in [0,1], default=0.05):
        Space between subplot rows. Applied to all rows.

    print_grid (kwarg, True | False, default=False):
        If True, prints a tab-delimited string representation
        of your plot grid.

    Keyword arguments with variable defaults:

    horizontal_spacing (kwarg, float in [0,1], default=0.2 / columns):
        Space between subplot columns.

    vertical_spacing (kwarg, float in [0,1], default=0.3 / rows):
        Space between subplot rows.

    """
    pass


def make_subplots(
    rows=1,
    cols=1,
    shared_xaxes=False,
    shared_yaxes=False,
    start_cell="top-left",
    print_grid=None,
    **kwargs,
):
    """Return an instance of plotly.graph_objs.Figure
    with the subplots domain set in 'layout'.

    Example 1:
    # stack two subplots vertically
    fig = tools.make_subplots(rows=2)

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]
    [ (2,1) x2,y2 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    # or see Figure.add_trace

    Example 2:
    # subplots with shared x axes
    fig = tools.make_subplots(rows=2, shared_xaxes=True)

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]
    [ (2,1) x1,y2 ]


    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], yaxis='y2')]

    Example 3:
    # irregular subplot layout (more examples below under 'specs')
    fig = tools.make_subplots(rows=2, cols=2,
                              specs=[[{}, {}],
                                     [{'colspan': 2}, None]])

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]  [ (1,2) x2,y2 ]
    [ (2,1) x3,y3           -      ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x3', yaxis='y3')]

    Example 4:
    # insets
    fig = tools.make_subplots(insets=[{'cell': (1,1), 'l': 0.7, 'b': 0.3}])

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]

    With insets:
    [ x2,y2 ] over [ (1,1) x1,y1 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 5:
    # include subplot titles
    fig = tools.make_subplots(rows=2, subplot_titles=('Plot 1','Plot 2'))

    This is the format of your plot grid:
    [ (1,1) x1,y1 ]
    [ (2,1) x2,y2 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Example 6:
    # Include subplot title on one plot (but not all)
    fig = tools.make_subplots(insets=[{'cell': (1,1), 'l': 0.7, 'b': 0.3}],
                              subplot_titles=('','Inset'))

    This is the format of your plot grid!
    [ (1,1) x1,y1 ]

    With insets:
    [ x2,y2 ] over [ (1,1) x1,y1 ]

    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2])]
    fig['data'] += [Scatter(x=[1,2,3], y=[2,1,2], xaxis='x2', yaxis='y2')]

    Keywords arguments with constant defaults:

    rows (kwarg, int greater than 0, default=1):
        Number of rows in the subplot grid.

    cols (kwarg, int greater than 0, default=1):
        Number of columns in the subplot grid.

    shared_xaxes (kwarg, boolean or list, default=False)
        Assign shared x axes.
        If True, subplots in the same grid column have one common
        shared x-axis at the bottom of the gird.

        To assign shared x axes per subplot grid cell (see 'specs'),
        send list (or list of lists, one list per shared x axis)
        of cell index tuples.

    shared_yaxes (kwarg, boolean or list, default=False)
        Assign shared y axes.
        If True, subplots in the same grid row have one common
        shared y-axis on the left-hand side of the gird.

        To assign shared y axes per subplot grid cell (see 'specs'),
        send list (or list of lists, one list per shared y axis)
        of cell index tuples.

    start_cell (kwarg, 'bottom-left' or 'top-left', default='top-left')
        Choose the starting cell in the subplot grid used to set the
        domains of the subplots.

    print_grid (kwarg, boolean, default=True):
        If True, prints a tab-delimited string representation of
        your plot grid.

    Keyword arguments with variable defaults:

    horizontal_spacing (kwarg, float in [0,1], default=0.2 / cols):
        Space between subplot columns.
        Applies to all columns (use 'specs' subplot-dependents spacing)

    vertical_spacing (kwarg, float in [0,1], default=0.3 / rows):
        Space between subplot rows.
        Applies to all rows (use 'specs' subplot-dependents spacing)

    subplot_titles (kwarg, list of strings, default=empty list):
        Title of each subplot.
        "" can be included in the list if no subplot title is desired in
        that space so that the titles are properly indexed.

    specs (kwarg, list of lists of dictionaries):
        Subplot specifications.

        ex1: specs=[[{}, {}], [{'colspan': 2}, None]]

        ex2: specs=[[{'rowspan': 2}, {}], [None, {}]]

        - Indices of the outer list correspond to subplot grid rows
          starting from the bottom. The number of rows in 'specs'
          must be equal to 'rows'.

        - Indices of the inner lists correspond to subplot grid columns
          starting from the left. The number of columns in 'specs'
          must be equal to 'cols'.

        - Each item in the 'specs' list corresponds to one subplot
          in a subplot grid. (N.B. The subplot grid has exactly 'rows'
          times 'cols' cells.)

        - Use None for blank a subplot cell (or to move pass a col/row span).

        - Note that specs[0][0] has the specs of the 'start_cell' subplot.

        - Each item in 'specs' is a dictionary.
            The available keys are:

            * is_3d (boolean, default=False): flag for 3d scenes
            * colspan (int, default=1): number of subplot columns
                for this subplot to span.
            * rowspan (int, default=1): number of subplot rows
                for this subplot to span.
            * l (float, default=0.0): padding left of cell
            * r (float, default=0.0): padding right of cell
            * t (float, default=0.0): padding right of cell
            * b (float, default=0.0): padding bottom of cell

        - Use 'horizontal_spacing' and 'vertical_spacing' to adjust
          the spacing in between the subplots.

    insets (kwarg, list of dictionaries):
        Inset specifications.

        - Each item in 'insets' is a dictionary.
            The available keys are:

            * cell (tuple, default=(1,1)): (row, col) index of the
                subplot cell to overlay inset axes onto.
            * is_3d (boolean, default=False): flag for 3d scenes
            * l (float, default=0.0): padding left of inset
                  in fraction of cell width
            * w (float or 'to_end', default='to_end') inset width
                  in fraction of cell width ('to_end': to cell right edge)
            * b (float, default=0.0): padding bottom of inset
                  in fraction of cell height
            * h (float or 'to_end', default='to_end') inset height
                  in fraction of cell height ('to_end': to cell top edge)

    column_width (kwarg, list of numbers)
        Column_width specifications

        - Functions similarly to `column_width` of `plotly.graph_objs.Table`.
          Specify a list that contains numbers where the amount of numbers in
          the list is equal to `cols`.

        - The numbers in the list indicate the proportions that each column
          domains take across the full horizontal domain excluding padding.

        - For example, if columns_width=[3, 1], horizontal_spacing=0, and
          cols=2, the domains for each column would be [0. 0.75] and [0.75, 1]

    row_width (kwargs, list of numbers)
        Row_width specifications

        - Functions similarly to `column_width`. Specify a list that contains
          numbers where the amount of numbers in the list is equal to `rows`.

        - The numbers in the list indicate the proportions that each row
          domains take along the full vertical domain excluding padding.

        - For example, if row_width=[3, 1], vertical_spacing=0, and
          cols=2, the domains for each row from top to botton would be
          [0. 0.75] and [0.75, 1]
    """
    import plotly.subplots

    warnings.warn(
        "plotly.tools.make_subplots is deprecated, "
        "please use plotly.subplots.make_subplots instead",
        DeprecationWarning,
        stacklevel=1,
    )

    return plotly.subplots.make_subplots(
        rows=rows,
        cols=cols,
        shared_xaxes=shared_xaxes,
        shared_yaxes=shared_yaxes,
        start_cell=start_cell,
        print_grid=print_grid,
        **kwargs,
    )


warnings.filterwarnings(
    "default", r"plotly\.tools\.make_subplots is deprecated", DeprecationWarning
)


def get_graph_obj(obj, obj_type=None):
    """Returns a new graph object.

    OLD FUNCTION: this will *silently* strip out invalid pieces of the object.
    NEW FUNCTION: no striping of invalid pieces anymore - only raises error
        on unrecognized graph_objs
    """
    pass


def _replace_newline(obj):
    """Replaces '\n' with '<br>' for all strings in a collection."""
    pass


def return_figure_from_figure_or_data(figure_or_data, validate_figure):
    from plotly.graph_objs import Figure
    from plotly.basedatatypes import BaseFigure

    validated = False
    if isinstance(figure_or_data, dict):
        figure = figure_or_data
    elif isinstance(figure_or_data, list):
        figure = {"data": figure_or_data}
    elif isinstance(figure_or_data, BaseFigure):
        figure = figure_or_data.to_dict()
        validated = True
    else:
        raise exceptions.PlotlyError(
            "The `figure_or_data` positional "
            "argument must be "
            "`dict`-like, `list`-like, or an instance of plotly.graph_objs.Figure"
        )

    if validate_figure and not validated:
        try:
            figure = Figure(**figure).to_dict()
        except exceptions.PlotlyError as err:
            raise exceptions.PlotlyError(
                "Invalid 'figure_or_data' argument. "
                "Plotly will not be able to properly "
                "parse the resulting JSON. If you "
                "want to send this 'figure_or_data' "
                "to Plotly anyway (not recommended), "
                "you can set 'validate=False' as a "
                "plot option.\nHere's why you're "
                "seeing this error:\n\n{0}"
                "".format(err)
            )
        if not figure["data"]:
            raise exceptions.PlotlyEmptyDataError(
                "Empty data list found. Make sure that you populated the "
                "list of data objects you're sending and try again.\n"
                "Questions? Visit support.plot.ly"
            )

    return figure


# Default colours for finance charts
_DEFAULT_INCREASING_COLOR = "#3D9970"  # http://clrs.cc
_DEFAULT_DECREASING_COLOR = "#FF4136"

DIAG_CHOICES = ["scatter", "histogram", "box"]
VALID_COLORMAP_TYPES = ["cat", "seq"]


# Deprecations
class FigureFactory(object):
















def get_config_plotly_server_url():
    """
    Function to get the .config file's 'plotly_domain' without importing
    the chart_studio package.  This property is needed to compute the default
    value of the plotly.js config plotlyServerURL, so it is independent of
    the chart_studio integration and still needs to live in

    Returns
    -------
    str
    """
    config_file = os.path.join(PLOTLY_DIR, ".config")
    default_server_url = "https://plot.ly"
    if not os.path.exists(config_file):
        return default_server_url
    with open(config_file, "rt") as f:
        try:
            config_dict = json.load(f)
            if not isinstance(config_dict, dict):
                config_dict = {}
        except Exception:
            # TODO: issue a warning and bubble it up
            config_dict = {}

    return config_dict.get("plotly_domain", default_server_url)
