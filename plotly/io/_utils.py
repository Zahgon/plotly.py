from typing import List

import plotly
import plotly.graph_objs as go
from plotly.offline import get_plotlyjs_version


def validate_coerce_fig_to_dict(fig, validate):
    from plotly.basedatatypes import BaseFigure

    if isinstance(fig, BaseFigure):
        fig_dict = fig.to_dict()
    elif isinstance(fig, dict):
        if validate:
            # This will raise an exception if fig is not a valid plotly figure
            fig_dict = plotly.graph_objs.Figure(fig).to_plotly_json()
        else:
            fig_dict = fig
    elif hasattr(fig, "to_plotly_json"):
        fig_dict = fig.to_plotly_json()
    else:
        raise ValueError(
            """
The fig parameter must be a dict or Figure.
    Received value of type {typ}: {v}""".format(typ=type(fig), v=fig)
        )
    return fig_dict




def broadcast_args_to_dicts(**kwargs: dict) -> List[dict]:
    """
    Given one or more keyword arguments which may be either a single value or a list of values,
    return a list of keyword dictionaries by broadcasting the single valuesacross all the dicts.
    If more than one item in the input is a list, all lists must be the same length.

    Parameters
    ----------
    **kwargs: dict
        The keyword arguments

    Returns
    -------
    list of dicts
        A list of dictionaries

    Raises
    ------
    ValueError
        If any of the input lists are not the same length
    """
    pass


def plotly_cdn_url(cdn_ver=get_plotlyjs_version()):
    """Return a valid plotly CDN url."""
    return "https://cdn.plot.ly/plotly-{cdn_ver}.min.js".format(
        cdn_ver=cdn_ver,
    )
