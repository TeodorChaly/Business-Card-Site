from django.urls import path
from . import views

urlpatterns = [
    path("", views.Project_view.as_view(),),
    path("<slug:slug>/", views.Project_Detail.as_view(), name = "project_detail")
]