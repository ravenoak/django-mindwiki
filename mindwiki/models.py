__all__ = [
    'Page', 'PageAdmin',
    'Project', 'ProjectAdmin',
    'Tag', 'TagAdmin',
    'WebLink', 'WebLinkAdmin',
]

from django.contrib import admin
from django.db import models
from django.urls import reverse


class Page(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    tags = models.ManyToManyField('Tag')

    def __repr__(self):
        return f'Page(slug="{self.slug}" title="{self.title}")'

    def __str__(self):
        return f"{self.slug}"

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


class Project(models.Model):
    class ProjectStatus(models.TextChoices):
        NOT_STARTED = 'NS', 'Not Started'
        IN_PROGRESS = 'IP', 'In Progress'
        BLOCKED = 'B', 'Blocked'
        COMPLETED = 'C', 'Closed'

    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(
        choices=ProjectStatus.choices,
        default=ProjectStatus.NOT_STARTED,
        max_length=3, )
    #status_line = models.CharField(max_length=256)
    pages = models.ManyToManyField('Page')
    tags = models.ManyToManyField('Tag')
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'Project(slug="{self.slug}")'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mindwiki:project-detail', kwargs={'slug': self.slug})


class ProjectAdmin(admin.ModelAdmin):
    autocomplete_fields = ['pages', 'tags']
    list_display = ('name', 'status')
    list_filter = ('status', 'tags')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains',
                     'status__contains',
                     'tags__name__contains']


class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __repr__(self):
        return f'Tag(slug="{self.slug}")'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('mindwiki:tag-detail', kwargs={'slug': self.slug})


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']


class WebLink(models.Model):
    slug = models.SlugField(unique=True)
    url = models.URLField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True)
    tags = models.ManyToManyField('Tag')
    last_verified = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return f'WebLink(slug="{self.slug}")'

    def __str__(self):
        return self.url

    def get_absolute_url(self):
        return reverse('mindwiki:weblink-detail', kwargs={'slug': self.slug})


class WebLinkAdmin(admin.ModelAdmin):
    autocomplete_fields = ['tags']
    list_display = ('slug', 'url', 'last_verified')
    list_filter = ('last_verified', 'tags')
    search_fields = ['description__contains',
                     'slug__contains',
                     'url__contains',
                     'tags__name__contains']
