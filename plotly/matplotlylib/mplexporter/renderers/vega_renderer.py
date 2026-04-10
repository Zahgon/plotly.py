import warnings
import json
import random
from .base import Renderer
from ..exporter import Exporter


class VegaRenderer(Renderer):






class VegaHTML(object):
    def __init__(self, renderer):
        self.specification = dict(
            width=renderer.figwidth,
            height=renderer.figheight,
            data=renderer.data,
            scales=renderer.scales,
            axes=renderer.axes,
            marks=renderer.marks,
        )

    def html(self):
        """Build the HTML representation for IPython."""
        pass



def fig_to_vega(fig, notebook=False):
    """Convert a matplotlib figure to vega dictionary

    if notebook=True, then return an object which will display in a notebook
    otherwise, return an HTML string.
    """
    pass


VEGA_TEMPLATE = """
( function() {
  var _do_plot = function() {
    if ( (typeof vg == 'undefined') && (typeof IPython != 'undefined')) {
      $([IPython.events]).on("vega_loaded.vincent", _do_plot);
      return;
    }
    vg.parse.spec(%s, function(chart) {
      chart({el: "#vis%d"}).update();
    });
  };
  _do_plot();
})();
"""
