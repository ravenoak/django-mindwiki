from django.contrib import admin

from .models.links import WebLink, WebLinkAdmin
from .models.pages import (
    Page, PageAdmin, Project, ProjectAdmin, Snippet,
    SnippetAdmin)
from .models.files import File, FileAdmin, Image, ImageAdmin
from .models.base import Tag, TagAdmin

admin.site.register(File, FileAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(WebLink, WebLinkAdmin)
