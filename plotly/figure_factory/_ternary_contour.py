import plotly.colors as clrs
from plotly.graph_objs import graph_objs as go
from plotly import exceptions
from plotly import optional_imports

from skimage import measure

np = optional_imports.get_module("numpy")
scipy_interp = optional_imports.get_module("scipy.interpolate")

# -------------------------- Layout ------------------------------


def _ternary_layout(
    title="Ternary contour plot", width=550, height=525, pole_labels=["a", "b", "c"]
):
    """
    Layout of ternary contour plot, to be passed to ``go.FigureWidget``
    object.

    Parameters
    ==========
    title : str or None
        Title of ternary plot
    width : int
        Figure width.
    height : int
        Figure height.
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    """
    pass


# ------------- Transformations of coordinates -------------------


def _replace_zero_coords(ternary_data, delta=0.0005):
    """
    Replaces zero ternary coordinates with delta and normalize the new
    triplets (a, b, c).

    Parameters
    ----------

    ternary_data : ndarray of shape (N, 3)

    delta : float
        Small float to regularize logarithm.

    Notes
    -----
    Implements a method
    by J. A. Martin-Fernandez,  C. Barcelo-Vidal, V. Pawlowsky-Glahn,
    Dealing with zeros and missing values in compositional data sets
    using nonparametric imputation, Mathematical Geology 35 (2003),
    pp 253-278.
    """
    pass


def _ilr_transform(barycentric):
    """
    Perform Isometric Log-Ratio on barycentric (compositional) data.

    Parameters
    ----------
    barycentric: ndarray of shape (3, N)
        Barycentric coordinates.

    References
    ----------
    "An algebraic method to compute isometric logratio transformation and
    back transformation of compositional data", Jarauta-Bragulat, E.,
    Buenestado, P.; Hervada-Sala, C., in Proc. of the Annual Conf. of the
    Intl Assoc for Math Geology, 2003, pp 31-30.
    """
    pass


def _ilr_inverse(x):
    """
    Perform inverse Isometric Log-Ratio (ILR) transform to retrieve
    barycentric (compositional) data.

    Parameters
    ----------
    x : array of shape (2, N)
        Coordinates in ILR space.

    References
    ----------
    "An algebraic method to compute isometric logratio transformation and
    back transformation of compositional data", Jarauta-Bragulat, E.,
    Buenestado, P.; Hervada-Sala, C., in Proc. of the Annual Conf. of the
    Intl Assoc for Math Geology, 2003, pp 31-30.
    """
    pass


def _transform_barycentric_cartesian():
    """
    Returns the transformation matrix from barycentric to Cartesian
    coordinates and conversely.
    """
    pass


def _prepare_barycentric_coord(b_coords):
    """
    Check ternary coordinates and return the right barycentric coordinates.
    """
    pass


def _compute_grid(coordinates, values, interp_mode="ilr"):
    """
    Transform data points with Cartesian or ILR mapping, then Compute
    interpolation on a regular grid.

    Parameters
    ==========

    coordinates : array-like
        Barycentric coordinates of data points.
    values : 1-d array-like
        Data points, field to be represented as contours.
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours.
    """
    pass


# ----------------------- Contour traces ----------------------




def _colors(ncontours, colormap=None):
    """
    Return a list of ``ncontours`` colors from the ``colormap`` colorscale.
    """
    pass


def _is_invalid_contour(x, y):
    """
    Utility function for _contour_trace

    Contours with an area of the order as 1 pixel are considered spurious.
    """
    pass


def _extract_contours(im, values, colors):
    """
    Utility function for _contour_trace.

    In ``im`` only one part of the domain has valid values (corresponding
    to a subdomain where barycentric coordinates are well defined). When
    computing contours, we need to assign values outside of this domain.
    We can choose a value either smaller than all the values inside the
    valid domain, or larger. This value must be chose with caution so that
    no spurious contours are added. For example, if the boundary of the valid
    domain has large values and the outer value is set to a small one, all
    intermediate contours will be added at the boundary.

    Therefore, we compute the two sets of contours (with an outer value
    smaller of larger than all values in the valid domain), and choose
    the value resulting in a smaller total number of contours. There might
    be a faster way to do this, but it works...
    """
    pass


def _add_outer_contour(
    all_contours,
    all_values,
    all_areas,
    all_colors,
    values,
    val_outer,
    v_min,
    v_max,
    colors,
    color_min,
    color_max,
):
    """
    Utility function for _contour_trace

    Adds the background color to fill gaps outside of computed contours.

    To compute the background color, the color of the contour with largest
    area (``val_outer``) is used. As background color, we choose the next
    color value in the direction of the extrema of the colormap.

    Then we add information for the outer contour for the different lists
    provided as arguments.

    A discrete colormap with all used colors is also returned (to be used
    by colorscale trace).
    """
    pass


def _contour_trace(
    x,
    y,
    z,
    ncontours=None,
    colorscale="Electric",
    linecolor="rgb(150,150,150)",
    interp_mode="ilr",
    coloring=None,
    v_min=0,
    v_max=1,
):
    """
    Contour trace in Cartesian coordinates.

    Parameters
    ==========

    x, y : array-like
        Cartesian coordinates
    z : array-like
        Field to be represented as contours.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    colorscale : None or str (Plotly colormap)
        colorscale of the contours.
    linecolor : rgb color
        Color used for lines. If ``colorscale`` is not None, line colors are
        determined from ``colorscale`` instead.
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours. If 'irl',
        ILR (Isometric Log-Ratio) of compositional data is performed. If
        'cartesian', contours are determined in Cartesian space.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    vmin, vmax : float
        Bounds of interval of values used for the colorspace

    Notes
    =====
    """
    pass


# -------------------- Figure Factory for ternary contour -------------


def create_ternary_contour(
    coordinates,
    values,
    pole_labels=["a", "b", "c"],
    width=500,
    height=500,
    ncontours=None,
    showscale=False,
    coloring=None,
    colorscale="Bluered",
    linecolor=None,
    title=None,
    interp_mode="ilr",
    showmarkers=False,
):
    """
    Ternary contour plot.

    Parameters
    ----------

    coordinates : list or ndarray
        Barycentric coordinates of shape (2, N) or (3, N) where N is the
        number of data points. The sum of the 3 coordinates is expected
        to be 1 for all data points.
    values : array-like
        Data points of field to be represented as contours.
    pole_labels : str, default ['a', 'b', 'c']
        Names of the three poles of the triangle.
    width : int
        Figure width.
    height : int
        Figure height.
    ncontours : int or None
        Number of contours to display (determined automatically if None).
    showscale : bool, default False
        If True, a colorbar showing the color scale is displayed.
    coloring : None or 'lines'
        How to display contour. Filled contours if None, lines if ``lines``.
    colorscale : None or str (Plotly colormap)
        colorscale of the contours.
    linecolor : None or rgb color
        Color used for lines. ``colorscale`` has to be set to None, otherwise
        line colors are determined from ``colorscale``.
    title : str or None
        Title of ternary plot
    interp_mode : 'ilr' (default) or 'cartesian'
        Defines how data are interpolated to compute contours. If 'irl',
        ILR (Isometric Log-Ratio) of compositional data is performed. If
        'cartesian', contours are determined in Cartesian space.
    showmarkers : bool, default False
        If True, markers corresponding to input compositional points are
        superimposed on contours, using the same colorscale.

    Examples
    ========

    Example 1: ternary contour plot with filled contours

    >>> import plotly.figure_factory as ff
    >>> import numpy as np
    >>> # Define coordinates
    >>> a, b = np.mgrid[0:1:20j, 0:1:20j]
    >>> mask = a + b <= 1
    >>> a = a[mask].ravel()
    >>> b = b[mask].ravel()
    >>> c = 1 - a - b
    >>> # Values to be displayed as contours
    >>> z = a * b * c
    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z)
    >>> fig.show()

    It is also possible to give only two barycentric coordinates for each
    point, since the sum of the three coordinates is one:

    >>> fig = ff.create_ternary_contour(np.stack((a, b)), z)


    Example 2: ternary contour plot with line contours

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, coloring='lines')

    Example 3: customize number of contours

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, ncontours=8)

    Example 4: superimpose contour plot and original data as markers

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z, coloring='lines',
    ...                                 showmarkers=True)

    Example 5: customize title and pole labels

    >>> fig = ff.create_ternary_contour(np.stack((a, b, c)), z,
    ...                                 title='Ternary plot',
    ...                                 pole_labels=['clay', 'quartz', 'fledspar'])
    """
    pass
