from django.contrib import admin

# Register your models here.
from .models import Article, Writer

admin.site.register(Article)
admin.site.register(Writer)
