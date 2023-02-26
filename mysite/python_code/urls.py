from django.urls import path
from . import views

urlpatterns = [
    path('run_scraping/', views.run_scraping, name='run_scraping'),
]