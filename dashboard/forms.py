from django import forms
from .models import Article
from datetime import datetime


class ArticleForm(forms.Form):

    title = forms.CharField(label="Title", max_length=100, 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label="Content", max_length=100, 
        widget=forms.Textarea(attrs={'class':'form-control'}))
    
    def save(self, written_by):
        print("saving article from ", written_by)
        created_at = datetime.now()
        article = Article(title=self.data["title"], content=self.data["content"], created_at=created_at, written_by=written_by)
        article.save()