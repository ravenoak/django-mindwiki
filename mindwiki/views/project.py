__all__ = ['ProjectViewSet']

from rest_framework import viewsets

from mindwiki.models import Project
from mindwiki.serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
    lookup_url_kwarg = 'project_slug'
