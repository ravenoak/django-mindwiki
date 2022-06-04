from django.contrib import admin
from django.db import models
from django.urls import reverse


class WikiItem(models.Model):
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField('Tag')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.slug}"


class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __repr__(self):
        return f'Tag(slug="{self.slug}")'

    def __str__(self):
        return f"{self.slug}"

    def get_absolute_url(self):
        return reverse('mindwiki:tag-detail', kwargs={'slug': self.slug})


class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']
