__all__ = ['CategoryViewSet']

from rest_framework import viewsets

from mindwiki.models import Category
from mindwiki.serializers import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'category_slug'
