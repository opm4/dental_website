from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, EditForm, CategoryEditForm
from django.urls import reverse_lazy

# Create your views here.
# def home(request):
#     return render(request, 'home_blog.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details_blog.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')
    
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'blog/add_category.html'
    fields = '__all__'
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields = ('title', 'title_tag', 'body')
    
class UpdateCategoryView(UpdateView):
    model = Category
    form_class = CategoryEditForm
    template_name = 'blog/update_category.html'
    # fields = ('title', 'title_tag', 'body')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url =  reverse_lazy('home_blog')
    
def CategoryView(request, category):
    category_posts = Post.objects.filter(category=category.replace('-',' '))
    return render(request, 'blog/categories.html', { 'category' : category.title().replace('-',' ') , 'category_posts' : category_posts})