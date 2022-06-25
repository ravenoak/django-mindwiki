__all__ = ['ProjectDetailView', 'ProjectListView',
           'ProjectSearchView', ]

from django.views import generic

from mindwiki.models import Project

TEMPLATE_PATH = 'mindwiki/project/'


class ProjectListView(generic.ListView):
    model = Project
    ordering = '-date_modified'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = TEMPLATE_PATH + 'detail.html'


class ProjectSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = Project.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                _body__contains=contains) | query_set.filter(
                _description__contains=contains) | query_set.filter(
                name__contains=contains).order_by('-id')
        return query_set
