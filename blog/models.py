from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Writer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_editor = models.BooleanField(default=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"id: {self.id} is_editor: {self.is_editor}, name: {self.name}"


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
    status = models.CharField(max_length=20, choices=STATUS_CHOICES,
                              default=PENDING)
    written_by = models.ForeignKey(Writer,
                                   on_delete=models.CASCADE,
                                   related_name='written_by')
    edited_by = models.ForeignKey(Writer, on_delete=models.CASCADE, null=True,
                                  related_name='edited_by')

    def __str__(self):
        return f"""id: {self.id} title: {self.title}, written_by:
        {self.written_by}"""
