from .serializers import (
	ListSerializer,
	AddSerializer,
)

from rest_framework.generics import (
	ListAPIView,
	CreateAPIView,
)

from blog.models import Post


class PostListAPIView(ListAPIView):
	serializer_class = ListSerializer
	queryset = Post.objects.all()


class AddPost(CreateAPIView):
	serializer_class = AddSerializer
	queryset = Post.objects.all()