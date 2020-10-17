from django.urls import path, include
from .views import article_list, article_detail
from .views_class import ArticleAPIView, ArticleAPIDetails, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')
router1 = DefaultRouter()
router1.register('article', ArticleGenericViewSet, basename='article')
router2 = DefaultRouter()
router2.register('article', ArticleModelViewSet, basename='article')
urlpatterns = [
    # path("article", article_list),
    # path("detail/<int:pk>", article_detail)
    path("article", ArticleAPIView.as_view()),
    path("detail/<int:pk>", ArticleAPIDetails.as_view()),
    path("generic/article", GenericAPIView.as_view()),
    path("generic/article/<int:pk>", GenericAPIView.as_view()),
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>', include(router.urls)),
    path('genericviewset/', include(router1.urls)),
    path('modelviewset/', include(router2.urls)),
]