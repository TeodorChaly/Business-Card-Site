from django.contrib import admin
from .models import Project, QuestionsAnswer, Reviews, ProjectImages

@admin.register(Project)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","title","date", "url", "draft")
    list_display_links = ("title",)

@admin.register(QuestionsAnswer)
class QuestionsAnswerAdmin(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ("id",)

@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("id",)
    list_display_links = ("id",)

@admin.register(ProjectImages)
class ProjectImagesAdmin(admin.ModelAdmin):
    list_display = ("id","title", "movie")
    list_display_links = ("id","title", "movie")

# admin.site.register(Project, CategoryAdmin)
# admin.site.register(QuestionsAnswer)
# admin.site.register(Reviews)
# admin.site.register(ProjectImages)