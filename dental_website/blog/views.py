from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm, EditForm
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
    
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/update_post.html'
    # fields = ('title', 'title_tag', 'body')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url =  reverse_lazy('home_blog')