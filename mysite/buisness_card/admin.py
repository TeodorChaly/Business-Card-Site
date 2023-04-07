from django.contrib import admin
from .models import Project, QuestionsAnswer, Reviews, ProjectImages

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProjectAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


class QuestionAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = QuestionsAnswer
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "date", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("date",)
    search_fields = ("id", "title", "url")
    form = ProjectAdminForm


@admin.register(QuestionsAnswer)
class QuestionsAnswerAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    form = QuestionAdminForm


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    list_display_links = ("id", "name")
    readonly_fields = ("email",)


@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_project_title")
    list_display_links = ("id", "title", "get_project_title")
    list_filter = ("movie",)

    def get_project_title(self, obj):
        return obj.movie.title

    get_project_title.short_description = 'Project Titles'
