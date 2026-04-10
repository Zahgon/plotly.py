from collections.abc import Sequence

from plotly import exceptions




def validate_index(index_vals):
    """
    Validates if a list contains all numbers or all strings

    :raises: (PlotlyError) If there are any two items in the list whose
        types differ
    """
    pass


def validate_dataframe(array):
    """
    Validates all strings or numbers in each dataframe column

    :raises: (PlotlyError) If there are any two items in any list whose
        types differ
    """
    pass


def validate_equal_length(*args):
    """
    Validates that data lists or ndarrays are the same length.

    :raises: (PlotlyError) If any data lists are not the same length.
    """
    pass


def validate_positive_scalars(**kwargs):
    """
    Validates that all values given in key/val pairs are positive.

    Accepts kwargs to improve Exception messages.

    :raises: (PlotlyError) If any value is < 0 or raises.
    """
    pass


def flatten(array):
    """
    Uses list comprehension to flatten array

    :param (array): An iterable to flatten
    :raises (PlotlyError): If iterable is not nested.
    :rtype (list): The flattened list.
    """
    pass


def endpts_to_intervals(endpts):
    """
    Returns a list of intervals for categorical colormaps

    Accepts a list or tuple of sequentially increasing numbers and returns
    a list representation of the mathematical intervals with these numbers
    as endpoints. For example, [1, 6] returns [[-inf, 1], [1, 6], [6, inf]]

    :raises: (PlotlyError) If input is not a list or tuple
    :raises: (PlotlyError) If the input contains a string
    :raises: (PlotlyError) If any number does not increase after the
        previous one in the sequence
    """
    pass


def annotation_dict_for_label(
    text,
    lane,
    num_of_lanes,
    subplot_spacing,
    row_col="col",
    flipped=True,
    right_side=True,
    text_color="#0f0f0f",
):
    """
    Returns annotation dict for label of n labels of a 1xn or nx1 subplot.

    :param (str) text: the text for a label.
    :param (int) lane: the label number for text. From 1 to n inclusive.
    :param (int) num_of_lanes: the number 'n' of rows or columns in subplot.
    :param (float) subplot_spacing: the value for the horizontal_spacing and
        vertical_spacing params in your plotly.tools.make_subplots() call.
    :param (str) row_col: choose whether labels are placed along rows or
        columns.
    :param (bool) flipped: flips text by 90 degrees. Text is printed
        horizontally if set to True and row_col='row', or if False and
        row_col='col'.
    :param (bool) right_side: only applicable if row_col is set to 'row'.
    :param (str) text_color: color of the text.
    """
    pass


def list_of_options(iterable, conj="and", period=True):
    """
    Returns an English listing of objects separated by commas ','

    For example, ['foo', 'bar', 'baz'] becomes 'foo, bar and baz'
    if the conjunction 'and' is selected.
    """
    pass
