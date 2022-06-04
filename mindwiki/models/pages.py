from django.contrib import admin
from django.db import models
from django.urls import reverse

from .base import WikiItem


class Page(WikiItem):
    title = models.CharField(max_length=64)
    body = models.TextField()

    def __repr__(self):
        return f'Page(slug="{self.slug}" title="{self.title}")'

    def get_absolute_url(self):
        return reverse('mindwiki:page-detail', kwargs={'slug': self.slug})


class PageAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tags']
    list_display = ('slug', 'date_created', 'date_modified')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains']


class Project(Page):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = 'NS', 'Not Started'
        IN_PROGRESS = 'IP', 'In Progress'
        BLOCKED = 'B', 'Blocked'
        COMPLETED = 'C', 'Closed'

    description = models.TextField(blank=True)
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
    search_fields = ['body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains',
                     'description__contains',
                     'status__contains']


class Snippet(Page):
    description = models.TextField(blank=True)

    def __repr__(self):
        return f'Snippet(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:snippet-detail', kwargs={'slug': self.slug})


class SnippetAdmin(PageAdmin):
    search_fields = ['body__contains',
                     'slug__contains',
                     'title__contains',
                     'tags__name__contains',
                     'description__contains']
