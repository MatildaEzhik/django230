# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.forms import PostForm, CommentForm
from blog.models import Post, Category


@login_required
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comment_form': comment_form})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = category.posts.all()
    return render(request, 'blog/category_detail.html', {'category': category, 'posts': posts})

def author_list(request):
    authors = User.objects.all()
    return render(request, 'blog/author_list.html', {'authors': authors})

def author_detail(request, pk):
    author = get_object_or_404(User, pk=pk)
    posts = author.post_set.all()
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})
