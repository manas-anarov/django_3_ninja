from blog import views
from django.urls import path

urlpatterns = [
	path('list/', views.PostListAPIView.as_view(), name='blog-list'),
]