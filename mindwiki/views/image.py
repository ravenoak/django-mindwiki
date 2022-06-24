__all__ = ['ImageDetailView', 'ImageListView', 'ImageSearchView']

from django.http import JsonResponse
from django.views import generic

from mindwiki.models import Image

TEMPLATE_PATH = 'mindwiki/image/'


class ImageDetailView(generic.DetailView):
    model = Image
    template_name = TEMPLATE_PATH + 'detail.html'

    def get(self, request, *args, **kwargs):
        json_requested = self.request.GET.get('json', False)
        if json_requested and json_requested.lower() == 'true':
            image = self.get_object()
            data = {
                'description': image.description,
                'data': image.data,
            }
            return JsonResponse({'data': data})
        return super().get(request, *args, **kwargs)


class ImageListView(generic.ListView):
    model = Image
    ordering = '-date_modified'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class ImageSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = Image.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                slug__contains=contains) | query_set.filter(
                _description__contains=contains) | query_set.filter(
                url__contains=contains)
        return query_set
