from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Article(models.Model):
    PENDING = 'PD'
    ACCEPTED = 'ACT'
    REJECTED = 'RJT'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
    
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # 0 pending , 1 acepted , 2 rejected
    # status = models.IntegerField(default=0)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default=PENDING)

    written_by = models.CharField(max_length=200)
    edited_by = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f"""id: {self.id} title: {self.title}, written_by: 
        {self.written_by}"""


class Writer(models.Model):
    id_user = models.ForeignKey(
        User, on_delete=models.CASCADE, default=1, null=True)
    is_editor = models.BooleanField()
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"id: {self.id} is_editor: {self.is_editor}, name: {self.name}"