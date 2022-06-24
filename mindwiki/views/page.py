__all__ = ['PageCreateView', 'PageDetailView', 'PageListView',
           'PageSearchView', 'PageUpdateView']

from django.views import generic

from mindwiki.forms import PageForm
from mindwiki.models import Page

TEMPLATE_PATH = 'mindwiki/page/'


class PageCreateView(generic.CreateView):
    model = Page
    form_class = PageForm
    template_name = TEMPLATE_PATH + 'edit.html'


class PageUpdateView(generic.UpdateView):
    model = Page
    form_class = PageForm
    template_name = TEMPLATE_PATH + 'edit.html'


class PageListView(generic.ListView):
    model = Page
    ordering = '-date_modified'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'list.html'


class PageDetailView(generic.DetailView):
    model = Page
    template_name = TEMPLATE_PATH + 'detail.html'


class PageSearchView(generic.ListView):
    context_object_name = 'search_results'
    paginate_by = 9
    template_name = TEMPLATE_PATH + 'search.html'

    def get_queryset(self):
        contains = self.request.GET.get('contains', None)
        tags = self.request.GET.get('tags', None)

        query_set = Page.objects.all()
        if tags is not None and tags != '':
            for tag in tags.split(','):
                query_set = query_set.filter(tags__name__contains=tag)
        if contains is not None and contains != '':
            query_set = query_set.filter(
                _body__contains=contains) | query_set.filter(
                _description__contains=contains) | query_set.filter(
                title__contains=contains)
        return query_set
