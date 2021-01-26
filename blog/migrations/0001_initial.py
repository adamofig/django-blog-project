# Generated by Django 3.1.5 on 2021-01-26 02:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=10000)),
                ('status', models.IntegerField(default=0)),
                ('written_by', models.CharField(max_length=200)),
                ('edited_by', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_editor', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
                ('id_user', models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]