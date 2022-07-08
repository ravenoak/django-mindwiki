__all__ = ['FileViewSet']

from rest_framework import viewsets

from mindwiki.models import File
from mindwiki.serializers import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'file_slug'
