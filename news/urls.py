from django.urls import path
from . import views
from news.views import HomeNews, NewsByCategory, ViewNews, CreateNews

app_name = 'news'

urlpatterns = [
    # path('', views.index, name='index'),
    path('', HomeNews.as_view(), name='home'),
    # path('category/<int:category_id>/', views.get_category, name='category'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('<int:news_id>/', views.view_news, name='view_news'),
    path('<int:pk>/', ViewNews.as_view(), name='view_news'),
    # path('add-news/', views.add_news, name="add_news"),
    path('add-news/', CreateNews.as_view(), name="add_news"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),



    # TO DELETE BELOW!
    path('test/', views.test, name='test')
]