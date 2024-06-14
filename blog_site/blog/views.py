import random
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from django.contrib import messages
from .forms import BlogPostForm, BlogUpdateForm, CommentForm

@login_required(login_url='home/signin')
def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    return render(request, 'blog/new_form.html',{'form':form})

def allpost_view(request):
    allblog = Post.objects.all()[:18]
    context = {'allblog': allblog}
    return render(request, 'blog/allblog.html', context)

@login_required(login_url='home/signin')
def post_detail(request,slug):
    context = {}
    post = Post.objects.get(slug=slug)
    context = {'post':post}
    return render(request, 'blog/post_detail.html', context)
   
@login_required(login_url='home/signin')
def edit_post(request,s_no):
    post = Post.objects.get(s_no=s_no)
    if request.method != 'POST':
        form = BlogUpdateForm(instance=post)
    else:
        form = BlogUpdateForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            post.author = request.user
            messages.success(request, 'Post Updated Successfully!')
            return redirect('/')
    context={'post':post, 'form':form}
    return render(request, 'blog/post_update_form.html', context)

@login_required(login_url='home/signin')
def delete_post(request, s_no):
    post = get_object_or_404(Post,s_no=s_no)
    post.delete()
    messages.success(request, 'Post Deleted Successfully!')
    return redirect('/')

def post_comment(request):
    if request.method != 'Post':
        form = CommentForm()
    else:
        form = CommentForm(request.Post)
        if form.is_valid():
            form.save()
            return redirect()
    context = {'form':form}
    return render(request, 'blog/post_detail.html', context)



@login_required(login_url='home/signin')  
def blog_about(request):
    return render(request, 'blog/about.html')