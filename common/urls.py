from django.urls import path
from . import views

# app_name = 'common'

urlpatterns = [
    path('', views.start, name='start'),
    path('test/', views.test, name='test')
]