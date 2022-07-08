__all__ = ['PageViewSet']

from django.views import generic
from rest_framework import viewsets

from mindwiki.models import Page
from mindwiki.serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'page_slug'
