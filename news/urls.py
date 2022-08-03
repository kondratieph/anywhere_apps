from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.get_category, name='category'),
    # TO DELETE BELOW!
    path('test/', views.test, name='test')
]