from django.urls    import path
from .              import views

urlpatterns = [
    path("", views.index),
    path("posts", views.all_posts),
    path("posts/<str:title>", views.post_by_title)
]