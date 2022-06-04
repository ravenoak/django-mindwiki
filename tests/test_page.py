from django.test import TestCase

from mindwiki.models.pages import Page


class PageTestCase(TestCase):
    def setUp(self) -> None:
        Page.objects.create()

    def test_create_empty_vars(self) -> None:
        with self.assertRaises(Exception) as e:
            Page.objects.create()
        print(e)
