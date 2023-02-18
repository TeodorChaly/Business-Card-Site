from django.shortcuts import render
from django.views.generic.base import View
from .models import Project

class Project_view(View):
    def get(self, request):
        project = Project.objects.all()
        return render(request, "posts/project_list.html", {"project_list":project})
