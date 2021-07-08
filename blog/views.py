from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post, Comment
from .forms import PostForm, EditForm, CategoryEditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.
# def home(request):
#     return render(request, 'home_blog.html', {})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home_blog.html'
    ordering = ['-post_date']
    # ordering = ['-id']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_details_blog.html'
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args, **kwargs)
        
        stuff =  get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
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
    category_posts = Post.objects.filter(category__iexact=category.replace('-',' '))
    return render(request, 'blog/categories.html', { 'category' : category.title().replace('-',' ') , 'category_posts' : category_posts})

def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', { 'cat_menu_list' : cat_menu_list})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article_detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'
    # ordering = ['-date_added']
    # fields = '__all__'
    # fields = ('name', 'body')
    
    # success_url =  reverse_lazy('home_blog')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post_pk = self.kwargs['pk']
        stuff =  get_object_or_404(Post, id=self.kwargs['pk'])
        post_title = stuff.title
        context["post_title"] = post_title
        context["post_pk"] = post_pk
        return context