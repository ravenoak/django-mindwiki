from django.urls import include, path, reverse_lazy
from django.views.generic.base import RedirectView
from rest_framework.routers import DefaultRouter

from .views import category, file, image, page, project, snippet, tag, weblink, FrontPageView

app_name = 'mindwiki'

router = DefaultRouter()
router.register(r'category', category.CategoryViewSet, basename='category')
router.register(r'file', file.FileViewSet, basename='file')
router.register(r'image', image.ImageViewSet, basename='image')
router.register(r'page', page.PageViewSet, basename='page')
router.register(r'project', project.ProjectViewSet, basename='project')
router.register(r'snippet', snippet.SnippetViewSet, basename='snippet')
router.register(r'tag', tag.TagViewSet, basename='tag')
router.register(r'weblink', weblink.WebLinkViewSet, basename='weblink')

urlpatterns = [
    #
    # Root
    #
    path('', RedirectView.as_view(url=reverse_lazy(f'{app_name}:main')),
         name='index'),
    ###########################################################################

    #
    # Single-page app
    #
    path('main/', FrontPageView.as_view(), name='main'),

    #
    # API
    #
    path('api/', include(router.urls)),
    ###########################################################################
]
