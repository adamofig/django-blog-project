# Generated by Django 3.1.2 on 2021-01-21 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateField()),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('status', models.IntegerField(default=0)),
                ('written_by', models.CharField(max_length=200)),
                ('edited_by', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_editor', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
            ],
        ),
    ]
