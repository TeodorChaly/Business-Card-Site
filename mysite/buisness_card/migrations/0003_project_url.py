# Generated by Django 4.1.3 on 2023-02-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness_card', '0002_alter_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
