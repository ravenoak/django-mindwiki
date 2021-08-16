from django import template
from django.urls import reverse
from django.template.defaultfilters import stringfilter

import markdown as md
from markdown.extensions.wikilinks import WikiLinkExtension
from plantuml_markdown import PlantUMLMarkdownExtension

from .markdown_ext.ext_links import ExtLinkExtension

register = template.Library()


@register.filter()
@stringfilter
def markdown(text):
    return md.markdown(
        text,
        extensions=['codehilite',
                    'fenced_code',
                    'tables',
                    'toc',
                    PlantUMLMarkdownExtension(),
                    WikiLinkExtension(base_url=reverse('mindwiki:page-index')),
                    ExtLinkExtension(
                        base_url=reverse('mindwiki:weblink-index'),
                        end_url='/?json=true')
                    ])
