# Generated by Django 4.1.3 on 2023-04-07 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buisness_card', '0005_projectimages'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='position',
            field=models.IntegerField(default=0),
        ),
    ]
