from django.contrib import admin
from .models import Project, QuestionsAnswer, Reviews, ProjectImages


admin.site.register(Project)
admin.site.register(QuestionsAnswer)
admin.site.register(Reviews)
admin.site.register(ProjectImages)