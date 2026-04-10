from plotly.express._core import build_dataframe
from plotly.express._doc import make_docstring
from plotly.express._chart_types import choropleth_map, scatter_map
import narwhals.stable.v1 as nw
import numpy as np
import warnings


def _project_latlon_to_wgs84(lat, lon):
    """
    Projects lat and lon to WGS84, used to get regular hexagons on a mapbox map
    """
    pass


def _project_wgs84_to_latlon(x, y):
    """
    Projects WGS84 to lat and lon, used to get regular hexagons on a mapbox map
    """
    pass


def _getBoundsZoomLevel(lon_min, lon_max, lat_min, lat_max, mapDim):
    """
    Get the mapbox zoom level given bounds and a figure dimension
    Source: https://stackoverflow.com/questions/6048975/google-maps-v3-how-to-calculate-the-zoom-level-for-a-given-bounds
    """
    pass


def _compute_hexbin(x, y, x_range, y_range, color, nx, agg_func, min_count):
    """
    Computes the aggregation at hexagonal bin level.
    Also defines the coordinates of the hexagons for plotting.
    The binning is inspired by matplotlib's implementation.

    Parameters
    ----------
    x : np.ndarray
        Array of x values (shape N)
    y : np.ndarray
        Array of y values (shape N)
    x_range : np.ndarray
        Min and max x (shape 2)
    y_range : np.ndarray
        Min and max y (shape 2)
    color : np.ndarray
        Metric to aggregate at hexagon level (shape N)
    nx : int
        Number of hexagons horizontally
    agg_func : function
        Numpy compatible aggregator, this function must take a one-dimensional
        np.ndarray as input and output a scalar
    min_count : int
        Minimum number of points in the hexagon for the hexagon to be displayed

    Returns
    -------
    np.ndarray
        X coordinates of each hexagon (shape M x 6)
    np.ndarray
        Y coordinates of each hexagon (shape M x 6)
    np.ndarray
        Centers of the hexagons (shape M x 2)
    np.ndarray
        Aggregated value in each hexagon (shape M)

    """
    pass


def _compute_wgs84_hexbin(
    lat=None,
    lon=None,
    lat_range=None,
    lon_range=None,
    color=None,
    nx=None,
    agg_func=None,
    min_count=None,
    native_namespace=None,
):
    """
    Computes the lat-lon aggregation at hexagonal bin level.
    Latitude and longitude need to be projected to WGS84 before aggregating
    in order to display regular hexagons on the map.

    Parameters
    ----------
    lat : np.ndarray
        Array of latitudes (shape N)
    lon : np.ndarray
        Array of longitudes (shape N)
    lat_range : np.ndarray
        Min and max latitudes (shape 2)
    lon_range : np.ndarray
        Min and max longitudes (shape 2)
    color : np.ndarray
        Metric to aggregate at hexagon level (shape N)
    nx : int
        Number of hexagons horizontally
    agg_func : function
        Numpy compatible aggregator, this function must take a one-dimensional
        np.ndarray as input and output a scalar
    min_count : int
        Minimum number of points in the hexagon for the hexagon to be displayed

    Returns
    -------
    np.ndarray
        Lat coordinates of each hexagon (shape M x 6)
    np.ndarray
        Lon coordinates of each hexagon (shape M x 6)
    nw.Series
        Unique id for each hexagon, to be used in the geojson data (shape M)
    np.ndarray
        Aggregated value in each hexagon (shape M)

    """
    pass


def _hexagons_to_geojson(hexagons_lats, hexagons_lons, ids=None):
    """
    Creates a geojson of hexagonal features based on the outputs of
    _compute_wgs84_hexbin
    """
    pass


def create_hexbin_map(
    data_frame=None,
    lat=None,
    lon=None,
    color=None,
    nx_hexagon=5,
    agg_func=None,
    animation_frame=None,
    color_discrete_sequence=None,
    color_discrete_map={},
    labels={},
    color_continuous_scale=None,
    range_color=None,
    color_continuous_midpoint=None,
    opacity=None,
    zoom=None,
    center=None,
    map_style=None,
    title=None,
    template=None,
    width=None,
    height=None,
    min_count=None,
    show_original_data=False,
    original_data_marker=None,
):
    """
    Returns a figure aggregating scattered points into connected hexagons
    """
    pass


create_hexbin_map.__doc__ = make_docstring(
    create_hexbin_map,
    override_dict=dict(
        nx_hexagon=["int", "Number of hexagons (horizontally) to be created"],
        agg_func=[
            "function",
            "Numpy array aggregator, it must take as input a 1D array",
            "and output a scalar value.",
        ],
        min_count=[
            "int",
            "Minimum number of points in a hexagon for it to be displayed.",
            "If None and color is not set, display all hexagons.",
            "If None and color is set, only display hexagons that contain points.",
        ],
        show_original_data=[
            "bool",
            "Whether to show the original data on top of the hexbin aggregation.",
        ],
        original_data_marker=["dict", "Scattermap marker options."],
    ),
)


