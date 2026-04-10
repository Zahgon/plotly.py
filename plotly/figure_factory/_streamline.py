import math

from plotly import exceptions, optional_imports
from plotly.figure_factory import utils
from plotly.graph_objs import graph_objs

np = optional_imports.get_module("numpy")


def validate_streamline(x, y):
    """
    Streamline-specific validations

    Specifically, this checks that x and y are both evenly spaced,
    and that the package numpy is available.

    See FigureFactory.create_streamline() for params

    :raises: (ImportError) If numpy is not available.
    :raises: (PlotlyError) If x is not evenly spaced.
    :raises: (PlotlyError) If y is not evenly spaced.
    """
    pass


def create_streamline(
    x, y, u, v, density=1, angle=math.pi / 9, arrow_scale=0.09, **kwargs
):
    """
    Returns data for a streamline plot.

    :param (list|ndarray) x: 1 dimensional, evenly spaced list or array
    :param (list|ndarray) y: 1 dimensional, evenly spaced list or array
    :param (ndarray) u: 2 dimensional array
    :param (ndarray) v: 2 dimensional array
    :param (float|int) density: controls the density of streamlines in
        plot. This is multiplied by 30 to scale similiarly to other
        available streamline functions such as matplotlib.
        Default = 1
    :param (angle in radians) angle: angle of arrowhead. Default = pi/9
    :param (float in [0,1]) arrow_scale: value to scale length of arrowhead
        Default = .09
    :param kwargs: kwargs passed through plotly.graph_objs.Scatter
        for more information on valid kwargs call
        help(plotly.graph_objs.Scatter)

    :rtype (dict): returns a representation of streamline figure.

    Example 1: Plot simple streamline and increase arrow size

    >>> from plotly.figure_factory import create_streamline
    >>> import plotly.graph_objects as go
    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> x = np.linspace(-3, 3, 100)
    >>> y = np.linspace(-3, 3, 100)
    >>> Y, X = np.meshgrid(x, y)
    >>> u = -1 - X**2 + Y
    >>> v = 1 + X - Y**2
    >>> u = u.T  # Transpose
    >>> v = v.T  # Transpose

    >>> # Create streamline
    >>> fig = create_streamline(x, y, u, v, arrow_scale=.1)
    >>> fig.show()

    Example 2: from nbviewer.ipython.org/github/barbagroup/AeroPython

    >>> from plotly.figure_factory import create_streamline
    >>> import numpy as np
    >>> import math

    >>> # Add data
    >>> N = 50
    >>> x_start, x_end = -2.0, 2.0
    >>> y_start, y_end = -1.0, 1.0
    >>> x = np.linspace(x_start, x_end, N)
    >>> y = np.linspace(y_start, y_end, N)
    >>> X, Y = np.meshgrid(x, y)
    >>> ss = 5.0
    >>> x_s, y_s = -1.0, 0.0

    >>> # Compute the velocity field on the mesh grid
    >>> u_s = ss/(2*np.pi) * (X-x_s)/((X-x_s)**2 + (Y-y_s)**2)
    >>> v_s = ss/(2*np.pi) * (Y-y_s)/((X-x_s)**2 + (Y-y_s)**2)

    >>> # Create streamline
    >>> fig = create_streamline(x, y, u_s, v_s, density=2, name='streamline')

    >>> # Add source point
    >>> point = go.Scatter(x=[x_s], y=[y_s], mode='markers',
    ...                    marker_size=14, name='source point')

    >>> fig.add_trace(point) # doctest: +SKIP
    >>> fig.show()
    """
    pass


class _Streamline(object):
    """
    Refer to FigureFactory.create_streamline() for docstring
    """

    def __init__(self, x, y, u, v, density, angle, arrow_scale, **kwargs):
        self.x = np.array(x)
        self.y = np.array(y)
        self.u = np.array(u)
        self.v = np.array(v)
        self.angle = angle
        self.arrow_scale = arrow_scale
        self.density = int(30 * density)  # Scale similarly to other functions
        self.delta_x = self.x[1] - self.x[0]
        self.delta_y = self.y[1] - self.y[0]
        self.val_x = self.x
        self.val_y = self.y

        # Set up spacing
        self.blank = np.zeros((self.density, self.density))
        self.spacing_x = len(self.x) / float(self.density - 1)
        self.spacing_y = len(self.y) / float(self.density - 1)
        self.trajectories = []

        # Rescale speed onto axes-coordinates
        self.u = self.u / (self.x[-1] - self.x[0])
        self.v = self.v / (self.y[-1] - self.y[0])
        self.speed = np.sqrt(self.u**2 + self.v**2)

        # Rescale u and v for integrations.
        self.u *= len(self.x)
        self.v *= len(self.y)
        self.st_x = []
        self.st_y = []
        self.get_streamlines()
        streamline_x, streamline_y = self.sum_streamlines()
        arrows_x, arrows_y = self.get_streamline_arrows()

    def blank_pos(self, xi, yi):
        """
        Set up positions for trajectories to be used with rk4 function.
        """
        pass

    def value_at(self, a, xi, yi):
        """
        Set up for RK4 function, based on Bokeh's streamline code
        """
        if isinstance(xi, np.ndarray):
            self.x = xi.astype(int)
            self.y = yi.astype(int)
        else:
            self.val_x = int(xi)
            self.val_y = int(yi)
        a00 = a[self.val_y, self.val_x]
        a01 = a[self.val_y, self.val_x + 1]
        a10 = a[self.val_y + 1, self.val_x]
        a11 = a[self.val_y + 1, self.val_x + 1]
        xt = xi - self.val_x
        yt = yi - self.val_y
        a0 = a00 * (1 - xt) + a01 * xt
        a1 = a10 * (1 - xt) + a11 * xt
        return a0 * (1 - yt) + a1 * yt

    def rk4_integrate(self, x0, y0):
        """
        RK4 forward and back trajectories from the initial conditions.

        Adapted from Bokeh's streamline -uses Runge-Kutta method to fill
        x and y trajectories then checks length of traj (s in units of axes)
        """
        pass

    def traj(self, xb, yb):
        """
        Integrate trajectories

        :param (int) xb: results of passing xi through self.blank_pos
        :param (int) xy: results of passing yi through self.blank_pos

        Calculate each trajectory based on rk4 integrate method.
        """
        pass

    def get_streamlines(self):
        """
        Get streamlines by building trajectory set.
        """
        pass

    def get_streamline_arrows(self):
        """
        Makes an arrow for each streamline.

        Gets angle of streamline at 1/3 mark and creates arrow coordinates
        based off of user defined angle and arrow_scale.

        :param (array) st_x: x-values for all streamlines
        :param (array) st_y: y-values for all streamlines
        :param (angle in radians) angle: angle of arrowhead. Default = pi/9
        :param (float in [0,1]) arrow_scale: value to scale length of arrowhead
            Default = .09
        :rtype (list, list) arrows_x: x-values to create arrowhead and
            arrows_y: y-values to create arrowhead
        """
        pass

    def sum_streamlines(self):
        """
        Makes all streamlines readable as a single trace.

        :rtype (list, list): streamline_x: all x values for each streamline
            combined into single list and streamline_y: all y values for each
            streamline combined into single list
        """
        pass
