from .serializers import (
	ListSerializer,
	AddSerializer,
	ShowSerializer,
)

from rest_framework.generics import (
	ListAPIView,
	CreateAPIView,
	RetrieveAPIView,
)

from blog.models import Post


class PostListAPIView(ListAPIView):
	serializer_class = ListSerializer
	queryset = Post.objects.all()


class AddPost(CreateAPIView):
	serializer_class = AddSerializer
	queryset = Post.objects.all()


class ShowPost(RetrieveAPIView):
	queryset = Post.objects.all()
	serializer_class = ShowSerializer
	lookup_field = 'id'