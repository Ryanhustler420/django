from datetime import date
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound


posts = [
    { 
        "slug": "mountains",
        "image": "mountains.jpg",
        "author": "Gaurav Gupta",
        "date": date(2026, 10, 1),
        "title": "Mountain Hiking", 
        "excerpt": """There's nothing like the views you get when hiking in the mountains! And i wasn't even prepared for what happend whilst I was enjoying the view.""",
        "content": """Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since 1966, when designers at Letraset and James Mosley, the librarian at St Bride Printing Library in London, took a 1914 Cicero translation and scrambled it to make dummy text for Letraset's Body Type sheets. It has survived not only many decades, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised thanks to these sheets and more recently with desktop publishing software like Aldus PageMaker and Microsoft Word including versions of Lorem Ipsum."""
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


def post_by_title(request, title):
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

