import argparse
import hashlib
import io
import json
import pathlib
import re

from django.core.management.base import BaseCommand

from mindwiki.models import Tag, WebLink

FAILED_FILE = 'bookmarks2weblinks-failed.json'
OUTPUT_DIR = '/tmp/mindwiki'
SLUG_CHARS = re.compile(r'[A-Za-z0-9_-]')


class Command(BaseCommand):
    help = 'Imports bookmarks as weblinks'

    def add_arguments(self, parser):
        parser.add_argument('file', type=argparse.FileType('r'))
        self.output_dir = pathlib.Path(OUTPUT_DIR)

    def handle(self, *args, **options):
        if not self.output_dir.exists():
            self.output_dir.mkdir()

        failed = []
        bms = self._parse_firefox(options['file'])
        self.stdout.write(
            self.style.SUCCESS(f'Found {len(bms)} items in bookmarks file.'))
        for bm in bms:
            descr = f'{bm["title"]}\n{bm["path"]}'
            tags = []
            for part in bm['path'].strip('/').split('/'):
                if part == 'toolbar' or part == 'mobile' or part == 'menu':
                    part = 'unfiled'
                tags.append(part)
            if 'tags' in bm:
                descr += f'\n{bm["tags"]}'
                tags += bm['tags']
            tags = list(dict.fromkeys(tags))
            ident_hash = hashlib.md5()
            ident_hash.update(
                bm['title'].encode('utf-8') + bm['path'].encode('utf-8') + bm[
                    'uri'].encode('utf-8'))
            slug = 'imported-' + ident_hash.hexdigest()
            data = {'url': bm['uri'],
                    'tags': tags,
                    'description': descr,
                    'slug': slug}

            weblink = WebLink.objects.filter(url__exact=bm['uri']).first()
            if weblink is None:
                weblink = WebLink(url=bm['uri'])
                weblink.slug = slug
            weblink.description = descr
            try:
                weblink.save()
                for tag in tags:
                    tag = tag.title()
                    t = Tag.objects.filter(name__exact=tag).first()
                    if t is None:
                        t = Tag(name=tag, slug=tag.replace(' ', ''))
                        t.save()
                    weblink.tags.add(t)
                weblink.save()
            except Exception as e:
                failed.append((data, bm))
                self.stdout.write(self.style.ERROR(f'{e} --> {weblink}'))
        if len(failed) > 0:
            with open('/tmp/mindwiki/bookmarks2weblinks-failed.json',
                      'w') as f:
                json.dump(failed, f)

    def _parse_firefox(self, file: io.FileIO):
        bookmarks = json.load(file)
        self.stdout.write(
            self.style.SUCCESS(f'Loaded Firefox bookmarks from {file.name}.'))
        return self._firefox_bm_walker(bookmarks['children'], '/')[0]

    def _firefox_bm_walker(self, bookmarks: list, path: str):
        bms = []
        for entry in bookmarks:
            if entry['type'] == 'text/x-moz-place-container':
                bms += self._firefox_bm_walker(entry['children'],
                                               f'{path}'
                                               f'{entry["title"]}/')[0]
            elif entry['type'] == 'text/x-moz-place':
                e = {
                    'title': entry['title'],
                    'path': path,
                    'uri': entry['uri'], }
                if 'tags' in entry:
                    e['tags'] = entry['tags'].split(',')
                bms.append(e)
        return bms, path
