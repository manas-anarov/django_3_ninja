from rest_framework.serializers import (
	ModelSerializer,
)
from blog.models import Post


class ListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'text',
		]


class AddSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			'text',
		]