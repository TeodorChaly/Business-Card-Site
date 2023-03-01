from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.Demos_view.as_view(), name="demos_list"),
    path('run_scraping/', views.run_scraping, name='run_scraping'),
    path('run_calculator/', views.run_calculator, name='run_calculator'),
]