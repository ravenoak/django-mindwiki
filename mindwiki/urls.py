from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView

from .views import category, file, image, page, project, snippet, tag, weblink

app_name = 'mindwiki'
urlpatterns = [
    #
    # Root
    #
    path('', RedirectView.as_view(url=reverse_lazy(f'{app_name}:page-index')),
         name='index'),
    ###########################################################################

    #
    # Category
    #
    path('category/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:category-list')),
         name='category-index'),
    path('category/list', category.CategoryListView.as_view(),
         name='category-list'),
    path('category/search', category.CategorySearchView.as_view(),
         name='category-search'),
    path('category/<slug:slug>/', category.CategoryDetailView.as_view(),
         name='category-detail'),
    ###########################################################################

    #
    # File
    #
    path('file/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:file-list')),
         name='file-index'),
    path('file/list', file.FileListView.as_view(),
         name='file-list'),
    path('file/search', file.FileSearchView.as_view(),
         name='file-search'),
    path('file/<slug:slug>/', file.FileDetailView.as_view(),
         name='file-detail'),
    ###########################################################################

    #
    # Image
    #
    path('image/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:image-list')),
         name='image-index'),
    path('image/list', image.ImageListView.as_view(),
         name='image-list'),
    path('image/search', image.ImageSearchView.as_view(),
         name='image-search'),
    path('image/<slug:slug>/', image.ImageDetailView.as_view(),
         name='image-detail'),
    ###########################################################################

    #
    # Page
    #
    path('page/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:page-list')),
         name='page-index'),
    path('page/list', page.PageListView.as_view(), name='page-list'),
    # TODO: Enable once auth is figured out
    # path('page/new', views.PageCreateView.as_view(), name='page-new'),
    path('page/search', page.PageSearchView.as_view(), name='page-search'),
    path('page/<slug:slug>/', page.PageDetailView.as_view(),
         name='page-detail'),
    # TODO: Enable once auth is figured out
    # path('page/<slug:slug>/edit', views.PageUpdateView.as_view(),
    #     name='page-edit'),
    ###########################################################################

    #
    # Project
    #
    path('project/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:project-list')),
         name='project-index'),
    path('project/list', project.ProjectListView.as_view(),
         name='project-list'),
    path('project/search', project.ProjectSearchView.as_view(),
         name='project-search'),
    path('project/<slug:slug>/', project.ProjectDetailView.as_view(),
         name='project-detail'),
    ###########################################################################

    #
    # Snippet
    #
    path('snippet/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:snippet-list')),
         name='snippet-index'),
    path('snippet/list', snippet.SnippetListView.as_view(),
         name='snippet-list'),
    path('snippet/search', snippet.SnippetSearchView.as_view(),
         name='snippet-search'),
    path('snippet/<slug:slug>/', snippet.SnippetDetailView.as_view(),
         name='snippet-detail'),
    ###########################################################################

    #
    # Tag
    #
    path('tag/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:tag-list')),
         name='tag-index'),
    path('tag/list', tag.TagListView.as_view(), name='tag-list'),
    path('tag/search', tag.TagSearchView.as_view(), name='tag-search'),
    path('tag/<slug:slug>/', tag.TagDetailView.as_view(), name='tag-detail'),
    ###########################################################################

    #
    # WebLink
    #
    path('weblink/',
         RedirectView.as_view(url=reverse_lazy(f'{app_name}:weblink-list')),
         name='weblink-index'),
    path('weblink/list', weblink.WebLinkListView.as_view(),
         name='weblink-list'),
    path('weblink/search', weblink.WebLinkSearchView.as_view(),
         name='weblink-search'),
    path('weblink/<slug:slug>/', weblink.WebLinkDetailView.as_view(),
         name='weblink-detail'),
    ###########################################################################
]
