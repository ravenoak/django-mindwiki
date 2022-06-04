from django.test import TestCase

from mindwiki.models.base import Tag


class TagTestCase(TestCase):
    def setUp(self) -> None:
        Tag.objects.create()

    def test_create_empty_vars(self) -> None:
        with self.assertRaises(Exception) as e:
            Tag.objects.create()
        print(e)
