from django.urls import path
from .views import AuthorListCreateAPIView, AuthorDetailAPIView


urlpatterns = [
    path('', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),
]