from rest_framework.viewsets import ModelViewSet
from .serializers import *


class ArticleViewSet(ModelViewSet):
    """Вывод статей"""
    queryset = Articles.objects.filter(is_published=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer


class CommentsListViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Comments.objects.filter(is_published=True, level=0).prefetch_related(
                'articles',
                'children'
            )
        return Comments.objects.filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        if self.action == 'list':
            return CommentsListSerializer
        return CommentsDetailSerializer


