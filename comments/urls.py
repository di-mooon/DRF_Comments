from django.urls import path
from . import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='Articles'),
    path('articles/<int:pk>', views.ArticleDetailView.as_view(), name='Article'),
    path('articles-create/', views.ArticleCreateView.as_view()),
    path('comments/', views.CommentView.as_view(), name='Comments'),
    path('comments-list/<int:pk>', views.CommentListView.as_view()),
    path('comments-detail/<int:pk>', views.CommentDetailView.as_view()),
    path('comments-create/', views.CommentCreateView.as_view()),
]
