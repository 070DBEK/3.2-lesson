from django.urls import path
from .views import TagListCreateAPIView, TagDetailAPIView, TagPostsAPIView


app_name = 'tags'


urlpatterns = [
    path('', TagListCreateAPIView.as_view(), name='tag-list-create'),
    path('<int:pk>/', TagDetailAPIView.as_view(), name='tag-detail'),
    path('<int:tag_id>/posts/', TagPostsAPIView.as_view(), name='tag-posts'),
]
