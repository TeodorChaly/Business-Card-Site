# Generated by Django 4.1.3 on 2023-02-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness_card', '0003_project_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]