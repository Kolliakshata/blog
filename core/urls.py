
from django.urls import path
from .views import BlogPostListAPIView, BlogPostCreateAPIView, BlogPostUpdateAPIView

urlpatterns = [
    path('api/posts/', BlogPostListAPIView.as_view(), name='post-list'),
    path('api/posts/create/', BlogPostCreateAPIView.as_view(), name='post-create'),
     path('api/posts/<int:id>/update/', BlogPostUpdateAPIView.as_view(), name='post-update'),
]

