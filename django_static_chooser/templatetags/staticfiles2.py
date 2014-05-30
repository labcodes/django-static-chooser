from django import template
from django.templatetags.static import StaticNode
from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings

register = template.Library()


def static(path):
    return staticfiles_storage.url(path)


class StaticFilesNode(StaticNode):

    @classmethod
    def handle_token(cls, parser, token):
        """
        Class method to parse prefix node and return a Node.
        """
        bits = token.split_contents()

        if len(bits) < 2:
            raise template.TemplateSyntaxError(
                "'%s' takes at least one argument (path to file)" % bits[0])

        path = parser.compile_filter(bits[1])

        if len(bits) == 3 and bits[-1] != 'as':
            if not settings.DEBUG:
                path = bits[-1]

        if len(bits) >= 2 and bits[-2] == 'as':
            varname = bits[3]
        else:
            varname = None

        return cls(varname, path)

    def url(self, context):
        if hasattr(self.path, 'resolve'):
            return static(self.path.resolve(context))
        else:
            return self.path


@register.tag('static')
def do_static(parser, token):
    """
    A template tag that returns the URL to a file
    using staticfiles' storage backend

    Usage::

        {% static path [remote_path] [as varname] %}

    Examples::

        {% static "myapp/css/base.css" "http://remote.url/css/base.css" %}

    """
    return StaticFilesNode.handle_token(parser, token)
