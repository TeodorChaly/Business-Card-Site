from django.urls import path
from . import views

urlpatterns = [
    path("", views.Main_Page_view.as_view(), ),
    path("project/", views.Project_view.as_view(),name="project_list"),
    path("q_a/", views.Question_Answer.as_view(), name="question_answer"),
    path("<slug:slug>/", views.Project_Detail.as_view(), name = "project_detail"),
]