import textwrap
import pkgutil

import copy
import os
import json
from functools import reduce

try:
    from math import gcd
except ImportError:
    # Python 2
    from fractions import gcd

# Create Lazy sentinal object to indicate that a template should be loaded
# on-demand from package_data
Lazy = object()


# Templates configuration class
# -----------------------------
class TemplatesConfig(object):
    """
    Singleton object containing the current figure templates (aka themes)
    """

    def __init__(self):
        # Initialize properties dict
        self._templates = {}

        # Initialize built-in templates
        default_templates = [
            "ggplot2",
            "seaborn",
            "simple_white",
            "plotly",
            "plotly_white",
            "plotly_dark",
            "presentation",
            "xgridoff",
            "ygridoff",
            "gridon",
            "none",
        ]

        for template_name in default_templates:
            self._templates[template_name] = Lazy

        self._validator = None
        self._default = None

    # ### Magic methods ###
    # Make this act as a dict of templates
    def __len__(self):
        return len(self._templates)

    def __contains__(self, item):
        return item in self._templates

    def __iter__(self):
        return iter(self._templates)

    def __getitem__(self, item):
        if isinstance(item, str):
            template_names = item.split("+")
        else:
            template_names = [item]

        templates = []
        for template_name in template_names:
            template = self._templates[template_name]
            if template is Lazy:
                from plotly.graph_objs.layout import Template

                if template_name == "none":
                    # "none" is a special built-in named template that applied no defaults
                    template = Template(data_scatter=[{}])
                    self._templates[template_name] = template
                else:
                    # Load template from package data
                    path = os.path.join(
                        "package_data", "templates", template_name + ".json"
                    )
                    template_str = pkgutil.get_data("plotly", path).decode("utf-8")
                    template_dict = json.loads(template_str)
                    template = Template(template_dict, _validate=False)

                    self._templates[template_name] = template
            templates.append(self._templates[template_name])

        return self.merge_templates(*templates)

    def __setitem__(self, key, value):
        self._templates[key] = self._validate(value)

    def __delitem__(self, key):
        # Remove template
        del self._templates[key]

        # Check if we need to remove it as the default
        if self._default == key:
            self._default = None


    def keys(self):
        return self._templates.keys()

    def items(self):
        return self._templates.items()

    def update(self, d={}, **kwargs):
        """
        Update one or more templates from a dict or from input keyword
        arguments.

        Parameters
        ----------
        d: dict
            Dictionary from template names to new template values.

        kwargs
            Named argument value pairs where the name is a template name
            and the value is a new template value.
        """
        for k, v in dict(d, **kwargs).items():
            self[k] = v

    # ### Properties ###
    @property
    def default(self):
        """
        The name of the default template, or None if no there is no default

        If not None, the default template is automatically applied to all
        figures during figure construction if no explicit template is
        specified.

        The names of available templates may be retrieved with:

        >>> import plotly.io as pio
        >>> list(pio.templates)

        Returns
        -------
        str
        """
        pass


    def __repr__(self):
        return """\
Templates configuration
-----------------------
    Default template: {default}
    Available templates:
{available}
""".format(default=repr(self.default), available=self._available_templates_str())

    def _available_templates_str(self):
        """
        Return nicely wrapped string representation of all
        available template names
        """
        pass

    def merge_templates(self, *args):
        """
        Merge a collection of templates into a single combined template.
        Templates are process from left to right so if multiple templates
        specify the same propery, the right-most template will take
        precedence.

        Parameters
        ----------
        args: list of Template
            Zero or more template objects (or dicts with compatible properties)

        Returns
        -------
        template:
            A combined template object

        Examples
        --------

        >>> pio.templates.merge_templates(
        ...     go.layout.Template(layout={'font': {'size': 20}}),
        ...     go.layout.Template(data={'scatter': [{'mode': 'markers'}]}),
        ...     go.layout.Template(layout={'font': {'family': 'Courier'}}))
        layout.Template({
            'data': {'scatter': [{'mode': 'markers', 'type': 'scatter'}]},
            'layout': {'font': {'family': 'Courier', 'size': 20}}
        })
        """
        if args:
            return reduce(self._merge_2_templates, args)
        else:
            from plotly.graph_objs.layout import Template

            return Template()

    def _merge_2_templates(self, template1, template2):
        """
        Helper function for merge_templates that merges exactly two templates

        Parameters
        ----------
        template1: Template
        template2: Template

        Returns
        -------
        Template:
            merged template
        """
        pass


# Make config a singleton object
# ------------------------------
templates = TemplatesConfig()
del TemplatesConfig


# Template utilities
# ------------------
def walk_push_to_template(fig_obj, template_obj, skip):
    """
    Move style properties from fig_obj to template_obj.

    Parameters
    ----------
    fig_obj: plotly.basedatatypes.BasePlotlyType
    template_obj: plotly.basedatatypes.BasePlotlyType
    skip: set of str
        Set of names of properties to skip
    """
    pass


def to_templated(fig, skip=("title", "text")):
    """
    Return a copy of a figure where all styling properties have been moved
    into the figure's template.  The template property of the resulting figure
    may then be used to set the default styling of other figures.

    Parameters
    ----------
    fig
        Figure object or dict representing a figure
    skip
        A collection of names of properties to skip when moving properties to
        the template. Defaults to ('title', 'text') so that the text
        of figure titles, axis titles, and annotations does not become part of
        the template

    Examples
    --------
    Imports

    >>> import plotly.graph_objs as go
    >>> import plotly.io as pio

    Construct a figure with large courier text

    >>> fig = go.Figure(layout={'title': 'Figure Title',
    ...                         'font': {'size': 20, 'family': 'Courier'},
    ...                         'template':"none"})
    >>> fig # doctest: +NORMALIZE_WHITESPACE
    Figure({
        'data': [],
        'layout': {'font': {'family': 'Courier', 'size': 20},
                   'template': '...', 'title': {'text': 'Figure Title'}}
    })

    Convert to a figure with a template. Note how the 'font' properties have
    been moved into the template property.

    >>> templated_fig = pio.to_templated(fig)
    >>> templated_fig.layout.template
    layout.Template({
        'layout': {'font': {'family': 'Courier', 'size': 20}}
    })
    >>> templated_fig
    Figure({
        'data': [], 'layout': {'template': '...', 'title': {'text': 'Figure Title'}}
    })


    Next create a new figure with this template

    >>> fig2 = go.Figure(layout={
    ...     'title': 'Figure 2 Title',
    ...     'template': templated_fig.layout.template})
    >>> fig2.layout.template
    layout.Template({
        'layout': {'font': {'family': 'Courier', 'size': 20}}
    })

    The default font in fig2 will now be size 20 Courier.

    Next, register as a named template...

    >>> pio.templates['large_courier'] = templated_fig.layout.template

    and specify this template by name when constructing a figure.

    >>> go.Figure(layout={
    ...     'title': 'Figure 3 Title',
    ...     'template': 'large_courier'}) # doctest: +ELLIPSIS
    Figure(...)

    Finally, set this as the default template to be applied to all new figures

    >>> pio.templates.default = 'large_courier'
    >>> fig = go.Figure(layout={'title': 'Figure 4 Title'})
    >>> fig.layout.template
    layout.Template({
        'layout': {'font': {'family': 'Courier', 'size': 20}}
    })

    Returns
    -------
    go.Figure
    """
    pass
