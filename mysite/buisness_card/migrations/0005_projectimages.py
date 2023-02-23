# Generated by Django 4.1.3 on 2023-02-21 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buisness_card', '0004_project_draft'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='project_picture/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buisness_card.project')),
            ],
        ),
    ]