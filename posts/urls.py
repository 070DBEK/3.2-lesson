from django.urls import path
from .views import PostListCreateAPIView, PostDetailAPIView
from comments.views import PostCommentListCreateAPIView


urlpatterns = [
    path('', PostListCreateAPIView.as_view(), name='post-list-create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('<int:post_id>/comments/', PostCommentListCreateAPIView.as_view(), name='post-comments'),
]
