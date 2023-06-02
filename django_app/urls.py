from django.urls import path, re_path
from django_app import views

urlpatterns = [
    re_path(r'^posts/$', views.posts, name="posts"),
    re_path(r'^posts/(?P<id>\d+)/$', views.posts_one, name="posts_one"),
]