from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.Main_Page_view.as_view(), name ="main_page"),
    path("projects/", views.Project_view.as_view(), name="project_list"),
    path("reviews/", views.Reviews_view.as_view(), name="review_list"),
    path("q_a/", views.Question_Answer.as_view(), name="question_answer"),
    path("add-review/", views.Add_review_view.as_view(), name="add_review"),
    path("<slug:slug>/", views.Project_Detail.as_view(), name ="project_detail"),
    path('accounts/login/', LoginView.as_view(), name='login'),
]