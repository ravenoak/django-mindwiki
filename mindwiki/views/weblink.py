__all__ = ['WebLinkDetailView', 'WebLinkListView', 'WebLinkSearchView']

from django.http import JsonResponse
from django.views import generic

from mindwiki.models import WebLink

TEMPLATE_PATH = 'mindwiki/weblink/'


class WebLinkDetailView(generic.DetailView):
    model = WebLink
    template_name = TEMPLATE_PATH + 'detail.html'

    def get(self, request, *args, **kwargs):
        json_requested = self.request.GET.get('json', False)
        if json_requested and json_requested.lower() == 'true':
            weblink = self.get_object()
            data = {
                'description': weblink.description,
                'url': weblink.url,
            }
            return JsonResponse({'data': data})
        return super().get(request, *args, **kwargs)


class WebLinkListView(generic.ListView):
    model = WebLink
    ordering = '-last_verified'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class WebLinkSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = WebLink.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                slug__contains=contains) | query_set.filter(
                _description__contains=contains) | query_set.filter(
                url__contains=contains)
        return query_set
