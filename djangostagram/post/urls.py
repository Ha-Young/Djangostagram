from django.urls import path
from .views import DetailPost

urlpatterns = [
    path('<int:pk>/', DetailPost.as_view(), name="post")
]