from django.contrib import admin
from django.db import models
from django.urls import reverse

from .base import WikiItem


class WebLink(WikiItem):
    url = models.URLField(unique=True, verbose_name='URL')
    description = models.TextField(blank=True)
    last_verified = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return f'WebLink(slug="{self.slug}")'

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
