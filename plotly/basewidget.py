from copy import deepcopy
import pathlib
from traitlets import List, Dict, observe, Integer
from plotly.io._renderers import display_jupyter_version_warnings

from .basedatatypes import BaseFigure, BasePlotlyType
from .callbacks import BoxSelector, LassoSelector, InputDeviceState, Points
from .serializers import custom_serializers
import anywidget


class BaseFigureWidget(BaseFigure, anywidget.AnyWidget):
    """
    Base class for FigureWidget. The FigureWidget class is code-generated as a
    subclass
    """

    _esm = pathlib.Path(__file__).parent / "package_data" / "widgetbundle.js"

    # ### _data and _layout ###
    # These properties store the current state of the traces and
    # layout as JSON-style dicts. These dicts do not store any subclasses of
    # `BasePlotlyType`
    #
    # Note: These are only automatically synced with the frontend on full
    # assignment, not on mutation. We use this fact to only directly sync
    # them to the front-end on FigureWidget construction. All other updates
    # are made using mutation, and they are manually synced to the frontend
    # using the relayout/restyle/update/etc. messages.
    _widget_layout = Dict().tag(sync=True, **custom_serializers)
    _widget_data = List().tag(sync=True, **custom_serializers)
    _config = Dict().tag(sync=True, **custom_serializers)

    # ### Python -> JS message properties ###
    # These properties are used to send messages from Python to the
    # frontend. Messages are sent by assigning the message contents to the
    # appropriate _py2js_* property and then immediately assigning None to the
    # property.
    #
    # See JSDoc comments in the FigureModel class in js/src/Figure.js for
    # detailed descriptions of the messages.
    _py2js_addTraces = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_restyle = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_relayout = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_update = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_animate = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    _py2js_deleteTraces = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _py2js_moveTraces = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    _py2js_removeLayoutProps = Dict(allow_none=True).tag(
        sync=True, **custom_serializers
    )
    _py2js_removeTraceProps = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    # ### JS -> Python message properties ###
    # These properties are used to receive messages from the frontend.
    # Messages are received by defining methods that observe changes to these
    # properties. Receive methods are named `_handler_js2py_*` where '*' is
    # the name of the corresponding message property.  Receive methods are
    # responsible for setting the message property to None after retreiving
    # the message data.
    #
    # See JSDoc comments in the FigureModel class in js/src/Figure.js for
    # detailed descriptions of the messages.
    _js2py_traceDeltas = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_layoutDelta = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_restyle = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_relayout = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_update = Dict(allow_none=True).tag(sync=True, **custom_serializers)
    _js2py_pointsCallback = Dict(allow_none=True).tag(sync=True, **custom_serializers)

    # ### Message tracking properties ###
    # The _last_layout_edit_id and _last_trace_edit_id properties are used
    # to keep track of the edit id of the message that most recently
    # requested an update to the Figures layout or traces respectively.
    #
    # We track this information because we don't want to update the Figure's
    # default layout/trace properties (_layout_defaults, _data_defaults)
    # while edits are in process. This can lead to inconsistent property
    # states.
    _last_layout_edit_id = Integer(0).tag(sync=True)
    _last_trace_edit_id = Integer(0).tag(sync=True)

    _set_trace_uid = True
    _allow_disable_validation = False

    # Constructor
    # -----------
    def __init__(
        self, data=None, layout=None, frames=None, skip_invalid=False, **kwargs
    ):
        # Call superclass constructors
        # ----------------------------
        # Note: We rename layout to layout_plotly because to deconflict it
        # with the `layout` constructor parameter of the `widgets.DOMWidget`
        # ipywidgets class
        super(BaseFigureWidget, self).__init__(
            data=data,
            layout_plotly=layout,
            frames=frames,
            skip_invalid=skip_invalid,
            **kwargs,
        )

        # Validate Frames
        # ---------------
        # Frames are not supported by figure widget
        if self._frame_objs:
            BaseFigureWidget._display_frames_error()

        # Message States
        # --------------
        # ### Layout ###

        # _last_layout_edit_id is described above
        self._last_layout_edit_id = 0

        # _layout_edit_in_process is set to True if there are layout edit
        # operations that have been sent to the frontend that haven't
        # completed yet.
        self._layout_edit_in_process = False

        # _waiting_edit_callbacks is a list of callback functions that
        # should be executed as soon as all pending edit operations are
        # completed
        self._waiting_edit_callbacks = []

        # ### Trace ###
        # _last_trace_edit_id: described above
        self._last_trace_edit_id = 0

        # _trace_edit_in_process is set to True if there are trace edit
        # operations that have been sent to the frontend that haven't
        # completed yet.
        self._trace_edit_in_process = False

        # View count
        # ----------
        # ipywidget property that stores the number of active frontend
        # views of this widget
        self._view_count = 0

        # Initialize widget layout and data for third-party widget integration
        # --------------------------------------------------------------------
        self._widget_layout = deepcopy(self._layout_obj._props)
        self._widget_data = deepcopy(self._data)

    def show(self, *args, **kwargs):
        return self

    # Python -> JavaScript Messages
    # -----------------------------
    def _send_relayout_msg(self, layout_data, source_view_id=None):
        """
        Send Plotly.relayout message to the frontend

        Parameters
        ----------
        layout_data : dict
            Plotly.relayout layout data
        source_view_id : str
            UID of view that triggered this relayout operation
            (e.g. By the user clicking 'zoom' in the toolbar). None if the
            operation was not triggered by a frontend view
        """
        pass

    def _send_restyle_msg(self, restyle_data, trace_indexes=None, source_view_id=None):
        """
        Send Plotly.restyle message to the frontend

        Parameters
        ----------
        restyle_data : dict
            Plotly.restyle restyle data
        trace_indexes : list[int]
            List of trace indexes that the restyle operation
            applies to
        source_view_id : str
            UID of view that triggered this restyle operation
            (e.g. By the user clicking the legend to hide a trace).
            None if the operation was not triggered by a frontend view
        """
        pass

    def _send_addTraces_msg(self, new_traces_data):
        """
        Send Plotly.addTraces message to the frontend

        Parameters
        ----------
        new_traces_data : list[dict]
            List of trace data for new traces as accepted by Plotly.addTraces
        """

        # Increment layout/trace edit message IDs
        # ---------------------------------------
        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        # Build message
        # -------------
        add_traces_msg = {
            "trace_data": new_traces_data,
            "trace_edit_id": trace_edit_id,
            "layout_edit_id": layout_edit_id,
        }

        # Send message
        # ------------
        self._py2js_addTraces = add_traces_msg
        self._py2js_addTraces = None

    def _send_moveTraces_msg(self, current_inds, new_inds):
        """
        Send Plotly.moveTraces message to the frontend

        Parameters
        ----------
        current_inds : list[int]
            List of current trace indexes
        new_inds : list[int]
            List of new trace indexes
        """
        pass

    def _send_update_msg(
        self, restyle_data, relayout_data, trace_indexes=None, source_view_id=None
    ):
        """
        Send Plotly.update message to the frontend

        Parameters
        ----------
        restyle_data : dict
            Plotly.update restyle data
        relayout_data : dict
            Plotly.update relayout data
        trace_indexes : list[int]
            List of trace indexes that the update operation applies to
        source_view_id : str
            UID of view that triggered this update operation
            (e.g. By the user clicking a button).
            None if the operation was not triggered by a frontend view
        """

        # Validate / normalize inputs
        # ---------------------------
        trace_indexes = self._normalize_trace_indexes(trace_indexes)

        # Increment layout/trace edit message IDs
        # ---------------------------------------
        trace_edit_id = self._last_trace_edit_id + 1
        self._last_trace_edit_id = trace_edit_id
        self._trace_edit_in_process = True

        layout_edit_id = self._last_layout_edit_id + 1
        self._last_layout_edit_id = layout_edit_id
        self._layout_edit_in_process = True

        # Build message
        # -------------
        update_msg = {
            "style_data": restyle_data,
            "layout_data": relayout_data,
            "style_traces": trace_indexes,
            "trace_edit_id": trace_edit_id,
            "layout_edit_id": layout_edit_id,
            "source_view_id": source_view_id,
        }

        # Send message
        # ------------
        self._py2js_update = update_msg
        self._py2js_update = None

    def _send_animate_msg(
        self, styles_data, relayout_data, trace_indexes, animation_opts
    ):
        """
        Send Plotly.update message to the frontend

        Note: there is no source_view_id parameter because animations
        triggered by the fontend are not currently supported

        Parameters
        ----------
        styles_data : list[dict]
            Plotly.animate styles data
        relayout_data : dict
            Plotly.animate relayout data
        trace_indexes : list[int]
            List of trace indexes that the animate operation applies to
        """
        pass

    def _send_deleteTraces_msg(self, delete_inds):
        """
        Send Plotly.deleteTraces message to the frontend

        Parameters
        ----------
        delete_inds : list[int]
            List of trace indexes of traces to delete
        """
        pass

    # JavaScript -> Python Messages
    # -----------------------------
    @observe("_js2py_traceDeltas")
    def _handler_js2py_traceDeltas(self, change):
        """
        Process trace deltas message from the frontend
        """
        pass

    @observe("_js2py_layoutDelta")
    def _handler_js2py_layoutDelta(self, change):
        """
        Process layout delta message from the frontend
        """
        pass

    @observe("_js2py_restyle")
    def _handler_js2py_restyle(self, change):
        """
        Process Plotly.restyle message from the frontend
        """
        pass

    @observe("_js2py_update")
    def _handler_js2py_update(self, change):
        """
        Process Plotly.update message from the frontend
        """
        pass

    @observe("_js2py_relayout")
    def _handler_js2py_relayout(self, change):
        """
        Process Plotly.relayout message from the frontend
        """
        pass

    @observe("_js2py_pointsCallback")
    def _handler_js2py_pointsCallback(self, change):
        """
        Process points callback message from the frontend
        """
        pass

    # Display
    # -------
    def _repr_html_(self):
        """
        Customize html representation
        """
        raise NotImplementedError  # Prefer _repr_mimebundle_

    def _repr_mimebundle_(self, include=None, exclude=None, validate=True, **kwargs):
        """
        Return mimebundle corresponding to default renderer.
        """
        pass

    def _ipython_display_(self):
        """
        Handle rich display of figures in ipython contexts
        """
        raise NotImplementedError  # Prefer _repr_mimebundle_

    # Callbacks
    # ---------
    def on_edits_completed(self, fn):
        """
        Register a function to be called after all pending trace and layout
        edit operations have completed

        If there are no pending edit operations then function is called
        immediately

        Parameters
        ----------
        fn : callable
            Function of zero arguments to be called when all pending edit
            operations have completed
        """
        pass

    # Validate No Frames
    # ------------------


    @staticmethod
    def _display_frames_error():
        """
        Display an informative error when user attempts to set frames on a
        FigureWidget

        Raises
        ------
        ValueError
            always
        """
        pass

    # Static Helpers
    # --------------
    @staticmethod
    def _remove_overlapping_props(input_data, delta_data, prop_path=()):
        """
        Remove properties in input_data that are also in delta_data, and do so
        recursively.

        Exception: Never remove 'uid' from input_data, this property is used
        to align traces

        Parameters
        ----------
        input_data : dict|list
        delta_data : dict|list

        Returns
        -------
        list[tuple[str|int]]
            List of removed property path tuples
        """
        pass

    @staticmethod
    def _transform_data(to_data, from_data, should_remove=True, relayout_path=()):
        """
        Transform to_data into from_data and return relayout-style
        description of the transformation

        Parameters
        ----------
        to_data : dict|list
        from_data : dict|list

        Returns
        -------
        dict
            relayout-style description of the transformation
        """
        pass
