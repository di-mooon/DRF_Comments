from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from django.db.models import Prefetch

from .serializers import *


class ArticleViewSet(ModelViewSet):
    """Вывод статей"""
    queryset = Articles.objects\
        .filter(is_published=True)\
        .prefetch_related(Prefetch('comments', queryset=Comments.objects.filter(level=0))) #надо оставить комментарии 0 уровня

    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleListSerializer
        return ArticleDetailSerializer


class CommentsListViewSet(ModelViewSet):
    def get_queryset(self):
        if self.action == 'list':
            return Comments.objects.filter(is_published=True, level=0)
        return Comments.objects.filter(id=self.kwargs.get('pk'))

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CommentsDetailSerializer
        return CommentsListSerializer
