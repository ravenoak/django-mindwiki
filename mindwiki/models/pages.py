from django.db import models
from django.urls import reverse
from markdownx.admin import MarkdownxModelAdmin
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify

from .base import WikiItem


class Page(WikiItem):
    title = models.CharField(max_length=64)
    _body = MarkdownxField(db_column="body",
                           verbose_name="Body",
                           help_text="Main rendered text of the item")

    def __repr__(self):
        return f'Page(slug="{self.slug}" title="{self.title}")'

    @property
    def body(self):
        return markdownify(str(self._body))

    def get_absolute_url(self):
        return reverse('mindwiki:page-detail', kwargs={'slug': self.slug})


class PageAdmin(MarkdownxModelAdmin):
    autocomplete_fields = ['tags']
    list_display = ('slug', 'date_created', 'date_modified')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['_body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains']


class Project(Page):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = 'NS', 'Not Started'
        IN_PROGRESS = 'IP', 'In Progress'
        BLOCKED = 'B', 'Blocked'
        COMPLETED = 'C', 'Closed'

    status = models.CharField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.NOT_STARTED,
        max_length=3, )
    status_line = models.CharField(max_length=256, blank=True)
    pages = models.ManyToManyField('Page',
                                   related_name='project_pages',
                                   blank=True)

    def __repr__(self):
        return f'Project(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:project-detail', kwargs={'slug': self.slug})


class ProjectAdmin(PageAdmin):
    autocomplete_fields = ['pages', 'tags']
    list_display = ('slug', 'date_created', 'date_modified', 'status')
    list_filter = ('status', 'tags')
    search_fields = ['_body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains',
                     '_description__contains',
                     'status__contains']


class Snippet(Page):

    def __repr__(self):
        return f'Snippet(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:snippet-detail', kwargs={'slug': self.slug})


class SnippetAdmin(PageAdmin):
    search_fields = ['_body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains',
                     '_description__contains']
