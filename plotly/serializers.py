from .basedatatypes import Undefined
from .optional_imports import get_module

np = get_module("numpy")


def _py_to_js(v, widget_manager):
    """
    Python -> Javascript ipywidget serializer

    This function must repalce all objects that the ipywidget library
    can't serialize natively (e.g. numpy arrays) with serializable
    representations

    Parameters
    ----------
    v
        Object to be serialized
    widget_manager
        ipywidget widget_manager (unused)

    Returns
    -------
    any
        Value that the ipywidget library can serialize natively
    """
    pass


def _js_to_py(v, widget_manager):
    """
    Javascript -> Python ipywidget deserializer

    Parameters
    ----------
    v
        Object to be deserialized
    widget_manager
        ipywidget widget_manager (unused)

    Returns
    -------
    any
        Deserialized object for use by the Python side of the library
    """
    pass


# Custom serializer dict for use in ipywidget traitlet definitions
custom_serializers = {"from_json": _js_to_py, "to_json": _py_to_js}
