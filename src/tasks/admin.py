from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'is_complete', 'created_at',)
    list_display_links = ('id', 'title')
    list_filter = ('user', 'is_complete')
    list_editable = ('is_complete',)
    fields = ('title', 'user', 'is_complete', 'created_at')
    search_fields = ('title', 'user')
