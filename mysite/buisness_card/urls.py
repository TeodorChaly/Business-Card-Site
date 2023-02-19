from django.urls import path
from . import views

urlpatterns = [
    path("", views.Project_view.as_view(),),
    path("<int:pk>/", views.Project_Detail.as_view())
]