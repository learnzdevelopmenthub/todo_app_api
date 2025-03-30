from rest_framework import serializers
from .models import Category, Tag, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        source='category',
        write_only=True,
        required=False,
        allow_null = True
    )

    tag_ids = serializers.PrimaryKeyRelatedField(
        queryset = Tag.objects.all(),
        many=True,
        source='tags',
        required=False,
        allow_null=True
    )

    class Meta:
        model=Task
        fields = ['id', 'title', 'description', 'created_at', 'category', 'category_id', 'tags', 'tag_ids']