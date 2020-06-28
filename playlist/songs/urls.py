from django.urls import path, include
from songs.api import views as apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', apiviews.SongsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
