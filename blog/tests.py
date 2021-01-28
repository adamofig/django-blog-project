from django.test import TestCase
from django.contrib.auth import get_user_model


from .models import Writer, Article


User = get_user_model()


class GenericTest(TestCase):

    def setUp(self):
        User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')

    def test_create_user(self):
        User.objects.create_user(username='adamo',
                                 email='adamo@yo.com',
                                 password='glass onion')

    def test_save_model_writer(self):
        writer = Writer()
        writer.name = "johnas"
        writer.is_editor = True
        writer.user = User.objects.get(username="john")
        writer.save()

    def test_full_article_process(self):
        user = User.objects.get(username="john")
        writer = Writer.objects.create(name='john writer', user=user)
        article = Article.objects.create(
            title='Big', content="content", written_by=writer)
        self.assertEqual(article.status, Article.PENDING)

    def test_get_writter(self):
        user = User.objects.get(username="john")
        writer = Writer(name="newuser", is_editor=True, user=user)
        writer.save()
        writer_obj = Writer.objects.get(pk=writer.id)
        self.assertEqual(writer, writer_obj)
