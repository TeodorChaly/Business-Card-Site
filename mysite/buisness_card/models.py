from django.db import models
from datetime import date

from django.urls import reverse


class Project(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField("Text Area")
    date = models.DateField("Project Date", default= date.today)
    image = models.ImageField("Image", upload_to="projects", blank=True, null=True)
    url = models.SlugField(max_length=100, unique=True, null=True)

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={"slug": self.url})

class QuestionsAnswer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField("Text Area")

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=50)
    text = models.TextField("Text Area")