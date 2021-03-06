from django import forms
from .models import Article
from datetime import datetime


class ArticleForm(forms.Form):

    title = forms.CharField(label="Title", max_length=200,
                            widget=forms.TextInput(
                                attrs={"class": "form-control"}),
                            )
    content = forms.CharField(
        label="Content",
        max_length=10000,
        widget=forms.Textarea(attrs={"class": "form-control"}),
    )

    def save(self, writer):
        article = Article(
            title=self.data["title"],
            content=self.data["content"],
            written_by=writer,
        )
        article.save()
