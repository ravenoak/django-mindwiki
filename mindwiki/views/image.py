__all__ = ['ImageViewSet']

from rest_framework import viewsets

from mindwiki.models import Image
from mindwiki.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'slug'
