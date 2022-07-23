from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<int:pk>', views.delete_todo, name='delete_todo'),
    path('add_todo/', views.add_todo, name='add_todo'),
    path('status/<int:pk>', views.change_status, name='change_status'),
    path('edit/<int:pk>', views.edit_todo, name='edit_todo'),
]