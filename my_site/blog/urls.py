from django.urls    import path
from .              import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.all_posts, name="all-posts"),
    path("posts/<slug:title>", views.post_by_title, name="single-post-detail")
]