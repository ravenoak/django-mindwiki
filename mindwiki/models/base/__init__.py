from django.db import models
from django.urls import reverse
from markdownx.admin import MarkdownxModelAdmin
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify


class WikiItem(models.Model):
    slug = models.SlugField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    _description = MarkdownxField(blank=True, db_column="description")
    tags = models.ManyToManyField('Tag')

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.slug}"

    @property
    def description(self):
        return markdownify(self._description)


class Tag(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)
    _description = MarkdownxField(blank=True)

    def __repr__(self):
        return f'Tag(slug="{self.slug}")'

    def __str__(self):
        return f"{self.slug}"

    @property
    def description(self):
        return markdownify(self._description)

    def get_absolute_url(self):
        return reverse('mindwiki:tag-detail', kwargs={'slug': self.slug})


class TagAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['description__contains',
                     'name__contains',
                     'slug__contains']


class Category(Tag):
    tags = models.ManyToManyField('Tag', related_name='category_tags', )

    def __repr__(self):
        return f'Category(slug="{self.slug}")'

    def get_absolute_url(self):
        return reverse('mindwiki:category-detail', kwargs={'slug': self.slug})


class CategoryAdmin(TagAdmin):
    pass
