__all__ = ['SnippetViewSet']

from rest_framework import viewsets

from mindwiki.models import Snippet
from mindwiki.serializers import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'snippet_slug'
