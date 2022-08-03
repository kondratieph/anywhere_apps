from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'due_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'due_date')

admin.site.register(ToDo, ToDoAdmin)
