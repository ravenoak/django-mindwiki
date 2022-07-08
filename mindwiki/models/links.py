from django.db import models
from django.urls import reverse
from markdownx.admin import MarkdownxModelAdmin

from .base import WikiItem


class WebLink(WikiItem):
    url = models.URLField(unique=True, verbose_name='URL')
    last_verified = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return f'WebLink(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:weblink-detail', kwargs={'slug': self.slug})


class WebLinkAdmin(MarkdownxModelAdmin):
    autocomplete_fields = ['tags']
    list_display = ('slug', 'url', 'last_verified')
    list_filter = ('last_verified', 'tags')
    search_fields = ['_description__contains',
                     'slug__contains',
                     'url__contains',
                     'tags__name__contains']
