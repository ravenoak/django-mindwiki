__all__ = ['TagViewSet']

from django.views import generic
from rest_framework import viewsets

from mindwiki.models import Tag
from mindwiki.serializers import TagSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'tag_slug'
