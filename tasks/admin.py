from .models import Task

from django.contrib import admin


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',
                    'deadline', 'date_created',
                    'date_modified', 'done']
    list_editable = ['deadline', 'done', 'title']
    list_filter = ['deadline']
    search_fields = ['title']