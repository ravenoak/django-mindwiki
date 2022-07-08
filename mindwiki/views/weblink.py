__all__ = ['WebLinkViewSet']

from rest_framework import viewsets

from mindwiki.models import WebLink
from mindwiki.serializers import WebLinkSerializer


class WebLinkViewSet(viewsets.ModelViewSet):
    queryset = WebLink.objects.all()
    serializer_class = WebLinkSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'weblink_slug'
