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


class FilterCommentsSerializer(serializers.ListSerializer):
    """Фильтр комментариев"""

    def to_representation(self, data):
        data = data.filter(parent__isnull=True)
        return super().to_representation(data)


class FilterTreeCommentSerializer(serializers.ListSerializer):
    """Фильтр комментариев до 3 уровня"""

    def to_representation(self, data):
        data = data.filter(parent__parent__isnull=False, parent__parent__parent__isnull=True)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Рекурсивный вывод комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentBaseSerializer(serializers.ModelSerializer):
    # children = serializers.SlugRelatedField(read_only=True, many=True,slug_field='name')
    class Meta:
        model = Comments
        fields = ('name', 'text', 'date', 'is_published', 'articles','children','parent')



class CommentSerializer(serializers.ModelSerializer):
    """Рекурсивный вывод комментариев"""
    children = RecursiveSerializer(many=True)


    class Meta:
        list_serializer_class = FilterCommentsSerializer
        model = Comments
        fields = ('name', 'text', 'date', 'is_published', 'articles', 'children')


class CommentDetailSerializer(CommentSerializer):
    """Комментарии до 3 уровня"""

    articles = serializers.SlugRelatedField(read_only=True, slug_field='title')
    children = CommentBaseSerializer(many=True)


class CommentListSerializer(CommentSerializer):
    """Комментарии 3 уровня"""

    class Meta:
        list_serializer_class = FilterTreeCommentSerializer
        model = Comments
        fields = ('name', 'text', 'date', 'is_published', 'articles', 'children')


class CommentsCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария к статье"""

    class Meta:
        model = Comments
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Статья"""

    comments = CommentDetailSerializer(many=True)

    class Meta:
        model = Articles
        fields = ('title', 'author', 'text', 'date', 'is_published', 'comments')
