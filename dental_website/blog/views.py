from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm

# Create your views here.
# def home(request):
#     return render(request, 'home_blog.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details_blog.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'
    # fields = '__all__'
    # fields = ('title', 'body')
    