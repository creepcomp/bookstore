from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthViewSet, BookViewSet, ReviewViewSet

router = DefaultRouter()
router.register('', AuthViewSet, basename='')
router.register('book', BookViewSet)
router.register('review', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls))
]
