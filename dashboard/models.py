from django.db import models
# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField()
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=1000)
    status = models.IntegerField(default=0)  # 0 pending , 1 acepted , 2 rejected
    written_by = models.CharField(max_length=200)
    edited_by = models.CharField(max_length=200)
    
    def __str__(self):
        return f"id: {self.id} title: {self.title}, written_by: {self.written_by}"


class Writer(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True)
    is_editor = models.BooleanField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"id: {self.id} is_editor: {self.is_editor}, name: {self.name}"