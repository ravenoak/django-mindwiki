from django import template
from django.conf import settings
from django.urls import reverse
from django.template.defaultfilters import stringfilter
import markdown as md
from markdown.extensions.wikilinks import WikiLinkExtension
from plantuml_markdown import PlantUMLMarkdownExtension

from .markdown_ext import ExtLinkExtension, SnippetExtension

register = template.Library()

x = 'http://'
if settings.SSL_ENABLED:
    x = 'https://'
base = f"{x}{settings.SITE_HOSTNAME}:{settings.SITE_PORT}"

MARKDOWN_EXTENSIONS = [
    'codehilite',
    'fenced_code',
    'tables',
    'toc',
    PlantUMLMarkdownExtension(),
    WikiLinkExtension(base_url=reverse('mindwiki:page-index')),
    ExtLinkExtension(
        base_url=base + reverse('mindwiki:weblink-index'),
        end_url='/?json=true'),
    SnippetExtension(
        base_url=base + reverse('mindwiki:snippet-index'),
        end_url='/?json=true')
]


@register.filter()
@stringfilter
def markdown(text):
    return md.markdown(text, extensions=MARKDOWN_EXTENSIONS)
