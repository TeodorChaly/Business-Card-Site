from django.contrib import admin
from .models import Project, QuestionsAnswer, Reviews, ProjectImages

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ProjectAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Project
        fields = '__all__'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id","title","date", "url", "draft")
    list_display_links = ("title",)
    list_filter = ("date",)
    search_fields = ("id", "title", "url")
    form = ProjectAdminForm

@admin.register(QuestionsAnswer)
class QuestionsAnswerAdmin(admin.ModelAdmin):
    list_display = ("id","title")
    list_display_links = ("id","title")

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    list_display_links = ("id", "name")
    readonly_fields = ("email",)

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ("id","title", "movie")
    list_display_links = ("id","title", "movie")
    list_filter = ("movie",)

# admin.site.register(Project, CategoryAdmin)
# admin.site.register(QuestionsAnswer)
# admin.site.register(Reviews)
# admin.site.register(ProjectImages)