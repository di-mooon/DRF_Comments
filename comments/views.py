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


class CommentListView(generics.ListAPIView):
    """Вывод всех комментариев"""
    queryset = Comments.objects.filter(is_published=True)
    serializer_class = CommentListSerializer


class CommentDetailView(APIView):
    """Вывод комментариев к статье"""
    def get(self, request, pk):
        comments = Comments.objects.filter(articles_id=pk)
        serializer = CommentListSerializer(comments, many=True)
        return Response(serializer.data)


class CommentCreateView(generics.CreateAPIView):
    """Добавление комментария"""
    serializer_class = CommentsCreateSerializer
