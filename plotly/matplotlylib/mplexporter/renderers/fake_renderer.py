from .base import Renderer


class FakeRenderer(Renderer):
    """
    Fake Renderer

    This is a fake renderer which simply outputs a text tree representing the
    elements found in the plot(s).  This is used in the unit tests for the
    package.

    Below are the methods your renderer must implement. You are free to do
    anything you wish within the renderer (i.e. build an XML or JSON
    representation, call an external API, etc.)  Here the renderer just
    builds a simple string representation for testing purposes.
    """

    def __init__(self):
        self.output = ""











class FullFakeRenderer(FakeRenderer):
    """
    Renderer with the full complement of methods.

    When the following are left undefined, they will be implemented via
    other methods in the class.  They can be defined explicitly for
    more efficient or specialized use within the renderer implementation.
    """



