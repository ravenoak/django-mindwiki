import logging
import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import requests

from .utils import build_url

SNIPPET_RE = r'^\s*\*\{([\w0-9_ -]+)\}\s.*$'

logger = logging.getLogger()


class SnippetExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'base_url': ['/', 'String to append to beginning or URL.'],
            'end_url': ['/', 'String to append to end of URL.'],
            'html_class': ['extlink', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }

        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        snippets = SnippetPreprocessor(self.getConfigs())
        md.preprocessors.register(snippets, 'snippets', 75)


class SnippetPreprocessor(Preprocessor):
    """ Insert Snippet content into the text """

    def __init__(self, config, **kwargs):
        self.config = config
        super().__init__(**kwargs)

    def run(self, lines):
        new_lines = []
        for line in lines:
            m = re.search(SNIPPET_RE, line)
            if not m:
                new_lines.append(line)
            else:
                slug = m.group(1)
                call_url = self.config['build_url'](slug,
                                                    self.config['base_url'],
                                                    self.config['end_url'])
                try:
                    data = requests.get(call_url).json()['data']
                    for sl in data['body'].splitlines():
                        new_lines.append(sl)
                except (KeyError,
                        requests.exceptions.JSONDecodeError,
                        requests.exceptions.HTTPError):
                    pass
        return new_lines


# noinspection PyPep8Naming
def makeExtension(**kwargs):  # pragma: no cover
    return SnippetExtension(**kwargs)
