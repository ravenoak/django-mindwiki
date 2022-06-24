__all__ = ['TagDetailView', 'TagListView', 'TagSearchView']

from django.views import generic

from mindwiki.models import Tag

TEMPLATE_PATH = 'mindwiki/tag/'


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = TEMPLATE_PATH + 'detail.html'


class TagListView(generic.ListView):
    model = Tag
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class TagSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)

        query_set = Tag.objects.all()
        if contains is not None and contains != '':
            query_set = query_set.filter(
                name__contains=contains) | query_set.filter(
                slug__contains=contains) | query_set.filter(
                _description__contains=contains)
        return query_set
