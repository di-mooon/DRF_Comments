from abc import ABC, ABCMeta

from rest_framework import serializers
from .models import Articles, Comments


class ArticleListSerializer(serializers.ModelSerializer):
    """Список статей"""

    class Meta:
        model = Articles
        fields = ('title',)


class ArticleCreateSerializer(serializers.ModelSerializer):
    """Добавление статьи"""
    class Meta:
        model = Articles
        fields = "__all__"


class FilterCommentsSerializer(serializers.ListSerializer, ABC):
    """Фильтр комментариев"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer, ABC):
    """Рекурсивный вывод комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentListSerializer(serializers.ModelSerializer):
    """Комментарии к статье"""
    children = RecursiveSerializer(many=True)
    articles = serializers.SlugRelatedField(read_only=True, slug_field='title')

    class Meta:

        list_serializer_class = FilterCommentsSerializer
        model = Comments
        fields = ('name', 'text', 'date', 'is_published', 'articles', 'children')


class CommentsCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария к статье"""

    class Meta:
        model = Comments
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Статья"""

    comments = CommentListSerializer(many=True)

    class Meta:

        model = Articles
        fields = ('title', 'author', 'text', 'date', 'is_published', 'comments')
