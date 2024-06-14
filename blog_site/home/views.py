from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post


def BlogHome(request):
    posts = Post.objects.filter().order_by("-timeStamp")[:6]
    # print(posts)
    context = {"posts": posts}
    return render(request, "home/blog_home.html", context)
