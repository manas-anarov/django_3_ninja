from blog import views
from django.urls import path

urlpatterns = [
	path('list/', views.PostListAPIView.as_view(), name='blog-list'),
	path('add/', views.AddPost.as_view(), name='blog-add'),
	path('<id>/', views.ShowPost.as_view(), name='blog-show'),
]