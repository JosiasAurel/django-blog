from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Comment
from .forms import CommentForm


def index(request):
    blog_posts = Post.objects.all().order_by("-date_published")
    blogs_ctx = {
        "posts": blog_posts
    }
    return render(request, "index.html", blogs_ctx)


def blog_specific(request, pk):
    blog_post = Post.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=blog_post
            )
            comment.save()
    comments = Comment.objects.filter(post=blog_post)
    ctx = {
        "post": blog_post,
        "comments": comments,
        "form": form
    }
    return render(request, "blogs.html", ctx)
