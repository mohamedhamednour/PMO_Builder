from django.contrib import admin 
from .models import Project , FilesProject
from django.contrib import admin
from django.contrib.admin import TabularInline


# Register your models here.

class FilesProjectInline(TabularInline):
    model = FilesProject
    extra = 0

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')
    inlines = [FilesProjectInline]
