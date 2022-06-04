from django.test import TestCase

from mindwiki.models.links import WebLink


class WebLinkTestCase(TestCase):
    def setUp(self) -> None:
        WebLink.objects.create()

    def test_create_empty_vars(self) -> None:
        with self.assertRaises(Exception) as e:
            WebLink.objects.create()
        print(e)
