from django.urls import path
from django.views.generic.edit import UpdateView
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView

urlpatterns = [
    # path('', views.home, name="home_blog"),
    path('', HomeView.as_view(), name="home_blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
]