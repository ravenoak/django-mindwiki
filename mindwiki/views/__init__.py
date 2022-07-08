from django.views.generic import TemplateView

from .category import CategoryViewSet
from .file import FileViewSet
from .image import ImageViewSet
from .page import PageViewSet
from .project import ProjectViewSet
from .snippet import SnippetViewSet
from .tag import TagViewSet
from .weblink import WebLinkViewSet


# View for single-page app
class FrontPageView(TemplateView):
    template_name = 'mindwiki/frontpage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

