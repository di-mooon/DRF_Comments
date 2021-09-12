from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("article", views.ArticleViewSet, basename="articles")
router.register('comments', views.CommentsListViewSet, basename='comments')
urlpatterns = router.urls

