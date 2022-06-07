__all__ = ['CategoryDetailView', 'CategoryListView', 'CategorySearchView']

from django.views import generic

from mindwiki.models import Category

TEMPLATE_PATH = 'mindwiki/category/'


class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = TEMPLATE_PATH + 'detail.html'


class CategoryListView(generic.ListView):
    model = Category
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class CategorySearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)

        query_set = Category.objects.all()
        if contains is not None and contains != '':
            query_set = query_set.filter(
                name__contains=contains) | query_set.filter(
                slug__contains=contains) | query_set.filter(
                description__contains=contains)
        return query_set
