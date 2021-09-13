from rest_framework import serializers
from .models import Articles, Comments


class CommentsListSerializer(serializers.ModelSerializer):
    """Вывод всех комментариев"""

    url = serializers.HyperlinkedIdentityField(view_name='comments-detail')

    class Meta:
        model = Comments
        fields = (
            'id', 'name', 'text', 'date', 'is_published', 'articles', 'level', 'tree_id', 'parent','url'
        )


class CommentsDetailSerializer(CommentsListSerializer):
    """Комментарий и ответы на него"""

    children = serializers.SerializerMethodField()

    def get_children(self, obj: Comments):
        return CommentsListSerializer(obj.get_descendants(), context=self.context, many=True).data

    class Meta:
        model = Comments
        fields = ('id', 'name', 'text', 'date', 'is_published', 'articles', 'tree_id', 'parent', 'url', 'children',)


class ArticleDetailSerializer(serializers.ModelSerializer):
    """Статья"""
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        return [CommentsListSerializer(comment, context=self.context).data for comment in obj.comments.all()]

    class Meta:
        model = Articles
        fields = ('title', 'author', 'text', 'date', 'is_published', 'comments')


class ArticleListSerializer(serializers.ModelSerializer):
    """Список статей"""
    url = serializers.HyperlinkedIdentityField(view_name='articles-detail')

    class Meta:
        model = Articles
        fields = ('title', 'author', 'text', 'is_published', 'url')
