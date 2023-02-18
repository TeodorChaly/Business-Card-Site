from django.urls import path
from . import views

urlpatterns = [
    path("", views.Project_view.as_view(),)

]