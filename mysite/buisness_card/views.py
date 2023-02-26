from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Project, QuestionsAnswer, Reviews
from .forms import AddReviewForm

class Project_view(ListView):
    model = Project
    queryset = Project.objects.filter(draft=False).order_by("-id")
    template_name = "posts/projects_list.html"

    # def get(self, request):
    #     projects = Project.objects.all()
    #     return render(request, "posts/projects_list.html", {"project_list":projects})

class Project_Detail(DetailView):
    model = Project
    slug_field = "url"
    template_name =  "posts/project_info.html"

class Question_Answer(View):
    def get(self, request):
        quest_answr = QuestionsAnswer.objects.all()
        return render(request, "posts/question_answer.html", {"question_answer":quest_answr})

class Reviews_view(View):
    def get(self, request):
        reviews = Reviews.objects.all()
        return render(request, "posts/reviews.html", {"reviews":reviews})

class Add_review_view(View):
    def get(self, request):
        form = AddReviewForm()
        return render(request, "posts/form_add_review.html", {"form":form})

    def post(self, request):
        form = AddReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')
        return render(request, "posts/form_add_review.html", {"form":form})

class Main_Page_view(View):
    def get(self, request):
        content_one = Project.objects.order_by("-id")[:2]
        content_two = QuestionsAnswer.objects.order_by("-id")[:3]
        content_three = Reviews.objects.order_by("-id")[:3]
        return render(request, "posts/main_page.html", {"content_one":content_one,"content_two":content_two,"content_three":content_three })


