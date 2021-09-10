from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


class ArticleListView(generics.ListAPIView):
    """Вывод всех статей"""
    queryset = Articles.objects.filter(is_published=True)
    serializer_class = ArticleListSerializer


class ArticleDetailView(generics.RetrieveAPIView):
    """Вывод статьи"""
    queryset = Articles.objects.filter(is_published=True)
    serializer_class = ArticleDetailSerializer


class ArticleCreateView(generics.CreateAPIView):
    """Добавление статьи"""
    serializer_class = ArticleCreateSerializer


class CommentView(generics.ListAPIView):
    """Вывод всех комментариев"""
    queryset = CommentsMptt.objects.filter(is_published=True, level=0).prefetch_related(

        'childrenmptt',
    )
    serializer_class = CommentSerializer


class CommentDetailView(APIView):
    """Вывод комментариев к статье до 3 уровня вложенности"""

    def get(self, request, pk):
        comments = CommentsMptt.objects.filter(articles_id=pk, is_published=True, level=0).prefetch_related(

            'articles',
            'childrenmptt'
        )
        serializer = CommentDetailSerializer(comments, many=True)
        return Response(serializer.data)


class CommentListView(APIView):
    """Вывод комментариев к статье 3 уровня вложенности"""

    def get(self, request, pk):
        comments = CommentsMptt.objects.filter(
            articles_id=pk,
            is_published=True,
            level=2
        ).get_descendants(include_self=True).prefetch_related('childrenmptt',)
        serializer = CommentBaseSerializer(comments, many=True)
        return Response(serializer.data)


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария"""
    serializer_class = CommentsCreateSerializer
