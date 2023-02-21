from django.shortcuts import render
from django.views.generic.base import View
from .models import Project

class Project_view(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "posts/projects_list.html", {"project_list":projects})

class Project_Detail(View):
    def get(self, request, slug):
        project = Project.objects.get(url=slug)
        return render(request, "posts/project_info.html", {"project":project})
