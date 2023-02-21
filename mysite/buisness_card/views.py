from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Project

class Project_view(ListView):
    model = Project
    queryset = Project.objects.filter(draft=False)
    template_name = "posts/projects_list.html"

    # def get(self, request):
    #     projects = Project.objects.all()
    #     return render(request, "posts/projects_list.html", {"project_list":projects})

class Project_Detail(DetailView):
    model = Project
    slug_field = "url"
    template_name =  "posts/project_info.html"
