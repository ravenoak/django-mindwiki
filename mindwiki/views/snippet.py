__all__ = ['SnippetDetailView', 'SnippetListView',
           'SnippetSearchView', ]

from django.http import JsonResponse
from django.views import generic

from mindwiki.models import Snippet

TEMPLATE_PATH = 'mindwiki/snippet/'


class SnippetListView(generic.ListView):
    model = Snippet
    ordering = '-date_modified'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class SnippetDetailView(generic.DetailView):
    model = Snippet
    template_name = TEMPLATE_PATH + 'detail.html'

    def get(self, request, *args, **kwargs):
        json_requested = self.request.GET.get('json', False)
        if json_requested and json_requested.lower() == 'true':
            snippet = self.get_object()
            data = {
                'body': snippet.body,
            }
            return JsonResponse({'data': data})
        return super().get(request, *args, **kwargs)


class SnippetSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = Snippet.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                _body__contains=contains) | query_set.filter(
                _description__contains=contains) | query_set.filter(
                name__contains=contains)
        return query_set
