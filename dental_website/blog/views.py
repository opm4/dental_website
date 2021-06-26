from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def home(request):
#     return render(request, 'home_blog.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details_blog.html'
    