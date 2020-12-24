from .serializers import (
	ListSerializer,
)

from rest_framework.generics import (
	ListAPIView,
)

from blog.models import Post


class PostListAPIView(ListAPIView):
    serializer_class = ListSerializer
    queryset = Post.objects.all()