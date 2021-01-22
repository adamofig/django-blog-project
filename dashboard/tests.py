from django.test import TestCase
from .models import Writer, Article
from datetime import datetime


class GenericTest(TestCase):

    def test_create_write_default_status(self):
        article = Article.objects.create(title='Big', content="content", created_at = datetime.now())
        self.assertEqual(article.status, 0)

    def test_save_model_writter(self):
        writer = Writer()
        writer.name = "newuser"
        writer.is_editor = True
        writer.id_user = None
        writer.save()

    def test_get_writter(self):

        writer = Writer(name="newuser", is_editor=True, id_user=None)
        writer.save()
        get_writet = Writer.objects.get(pk=1)
        self.assertEqual(writer, get_writet)
        print(get_writet)