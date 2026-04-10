"""
The `trendline_functions` module contains functions which are called by Plotly Express
when the `trendline` argument is used. Valid values for `trendline` are the names of the
functions in this module, and the value of the `trendline_options` argument to PX
functions is passed in as the first argument to these functions when called.

Note that the functions in this module are not meant to be called directly, and are
exposed as part of the public API for documentation purposes.
"""

__all__ = ["ols", "lowess", "rolling", "ewm", "expanding"]


def ols(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Ordinary Least Squares (OLS) trendline function

    Requires `statsmodels` to be installed.

    This trendline function causes fit results to be stored within the figure,
    accessible via the `plotly.express.get_trendline_results` function. The fit results
    are the output of the `statsmodels.api.OLS` function.

    Valid keys for the `trendline_options` dict are:

    - `add_constant` (`bool`, default `True`): if `False`, the trendline passes through
    the origin but if `True` a y-intercept is fitted.

    - `log_x` and `log_y` (`bool`, default `False`): if `True` the OLS is computed with
    respect to the base 10 logarithm of the input. Note that this means no zeros can
    be present in the input.
    """
    pass


def lowess(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """LOcally WEighted Scatterplot Smoothing (LOWESS) trendline function

    Requires `statsmodels` to be installed.

    Valid keys for the `trendline_options` dict are:

    - `frac` (`float`, default `0.6666666`): the `frac` parameter from the
    `statsmodels.api.nonparametric.lowess` function
    """
    pass




def rolling(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Rolling trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.rolling` function.
    """
    pass


def expanding(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Expanding trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.expanding` function.
    """
    pass


def ewm(trendline_options, x_raw, x, y, x_label, y_label, non_missing):
    """Exponentially Weighted Moment (EWM) trendline function

    The value of the `function` key of the `trendline_options` dict is the function to
    use (defaults to `mean`) and the value of the `function_args` key are taken to be
    its arguments as a dict. The remainder of  the `trendline_options` dict is passed as
    keyword arguments into the `pandas.Series.ewm` function.
    """
    pass
