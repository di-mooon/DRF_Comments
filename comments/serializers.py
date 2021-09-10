from rest_framework import serializers
from .models import Articles, CommentsMptt


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


class RecursiveSerializer(serializers.Serializer):
    """Рекурсивный вывод комментариев"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CommentBaseSerializer(serializers.ModelSerializer):
    """Вывод комментария"""
    class Meta:
        model = CommentsMptt
        fields = (
            'name', 'text', 'date', 'is_published', 'articles', 'level', 'tree_id', 'parent',
        )


class CommentSerializer(serializers.ModelSerializer):
    """Вывод всех комментариев"""
    childrenmptt = RecursiveSerializer(many=True, read_only=True)

    class Meta:
        model = CommentsMptt
        fields = (
            'name', 'text', 'date', 'is_published', 'articles', 'level', 'tree_id', 'parent',
            'childrenmptt'
        )


class CommentDetailSerializer(CommentSerializer):
    """Комментарии до 3 уровня"""

    articles = serializers.SlugRelatedField(read_only=True, slug_field='title')
    childrenmptt = CommentBaseSerializer(many=True, read_only=True)


class CommentsCreateSerializer(serializers.ModelSerializer):
    """Добавление комментария к статье"""

    class Meta:
        model = CommentsMptt
        fields = "__all__"


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Статья"""

    commentsmptt = CommentBaseSerializer(many=True)

    class Meta:
        model = Articles
        fields = ('title', 'author', 'text', 'date', 'is_published', 'commentsmptt')