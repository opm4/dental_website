from django.urls import path
from django.views.generic.edit import UpdateView
# from . import views
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, UpdateCategoryView, CategoryView

urlpatterns = [
    # path('', views.home, name="home_blog"),
    path('', HomeView.as_view(), name="home_blog"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article_detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('category/edit/<int:pk>', UpdateCategoryView.as_view(), name="update_category"),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:category>', CategoryView, name="category")
]