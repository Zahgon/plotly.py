import textwrap
from pprint import PrettyPrinter

from _plotly_utils.utils import NotEncodable, PlotlyJSONEncoder, get_module  # noqa: F401
from _plotly_utils.data_utils import image_array_to_data_uri  # noqa: F401


# Pretty printing
def _list_repr_elided(v, threshold=200, edgeitems=3, indent=0, width=80):
    """
    Return a string representation for of a list where list is elided if
    it has more than n elements

    Parameters
    ----------
    v : list
        Input list
    threshold :
        Maximum number of elements to display

    Returns
    -------
    str
    """
    pass


class ElidedWrapper(object):
    """
    Helper class that wraps values of certain types and produces a custom
    __repr__() that may be elided and is suitable for use during pretty
    printing
    """

    def __init__(self, v, threshold, indent):
        self.v = v
        self.indent = indent
        self.threshold = threshold


    def __repr__(self):
        numpy = get_module("numpy")
        if isinstance(self.v, (list, tuple)):
            # Handle lists/tuples
            res = _list_repr_elided(
                self.v, threshold=self.threshold, indent=self.indent
            )
            return res
        elif numpy and isinstance(self.v, numpy.ndarray):
            # Handle numpy arrays

            # Get original print opts
            orig_opts = numpy.get_printoptions()

            # Set threshold to self.max_list_elements
            numpy.set_printoptions(
                **dict(orig_opts, threshold=self.threshold, edgeitems=3, linewidth=80)
            )

            res = self.v.__repr__()

            # Add indent to all but the first line
            res_lines = res.split("\n")
            res = ("\n" + " " * self.indent).join(res_lines)

            # Restore print opts
            numpy.set_printoptions(**orig_opts)
            return res
        elif isinstance(self.v, str):
            # Handle strings
            if len(self.v) > 80:
                return "(" + repr(self.v[:30]) + " ... " + repr(self.v[-30:]) + ")"
            else:
                return self.v.__repr__()
        else:
            return self.v.__repr__()


class ElidedPrettyPrinter(PrettyPrinter):
    """
    PrettyPrinter subclass that elides long lists/arrays/strings
    """

    def __init__(self, *args, **kwargs):
        self.threshold = kwargs.pop("threshold", 200)
        PrettyPrinter.__init__(self, *args, **kwargs)



def node_generator(node, path=()):
    """
    General, node-yielding generator.

    Yields (node, path) tuples when it finds values that are dict
    instances.

    A path is a sequence of hashable values that can be used as either keys to
    a mapping (dict) or indices to a sequence (list). A path is always wrt to
    some object. Given an object, a path explains how to get from the top level
    of that object to a nested value in the object.

    :param (dict) node: Part of a dict to be traversed.
    :param (tuple[str]) path: Defines the path of the current node.
    :return: (Generator)

    Example:

        >>> for node, path in node_generator({'a': {'b': 5}}):
        ...     print(node, path)
        {'a': {'b': 5}} ()
        {'b': 5} ('a',)

    """
    pass


def get_by_path(obj, path):
    """
    Iteratively get on obj for each key in path.

    :param (list|dict) obj: The top-level object.
    :param (tuple[str]|tuple[int]) path: Keys to access parts of obj.

    :return: (*)

    Example:

        >>> figure = {'data': [{'x': [5]}]}
        >>> path = ('data', 0, 'x')
        >>> get_by_path(figure, path)
        [5]
    """
    pass


