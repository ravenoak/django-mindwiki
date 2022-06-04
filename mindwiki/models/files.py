from django.contrib import admin
from django.db import models
from django.urls import reverse

from .base import WikiItem


class File(WikiItem):
    name = models.CharField(max_length=64)
    data = models.FileField(upload_to='files')
    description = models.TextField(blank=True)

    def __repr__(self):
        return f'File(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:file-detail', kwargs={'slug': self.slug})


class FileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']


class Image(WikiItem):
    name = models.CharField(max_length=64)
    data = models.ImageField(upload_to='images')
    description = models.TextField(blank=True)

    def __repr__(self):
        return f'Image(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:image-detail', kwargs={'slug': self.slug})


class ImageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']
