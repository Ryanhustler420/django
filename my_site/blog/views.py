from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


posts = [
    { 
        "slug": "my-first-blog",
        "title": "My First Blog", 
        "body": "He there this is my first every blog on the internet", 
        "createdAt": "2026-10-01T12:00" 
    },
    { 
        "slug": "my-second-blog",
        "title": "My Second Blog", 
        "body": "He there this is my second every blog on the internet", 
        "createdAt": "2026-10-01T13:00" 
    },
]


def index(request):
    return render(request, "blog/index.html", {
        "posts": posts
    })


def all_posts(request):
    print("working")
    return render(request, "blog/posts.html", {
        "posts": posts
    })


def post_by_title(request, title: str):
    post = None
    for p in posts:
        if p.get("slug") == title:
            post = p
            break

    if post is None:
        return HttpResponseNotFound("This post is not available or maybe deleted")

    return render(request, "blog/post.html", {
        "title": title,
        "post": post
    })

