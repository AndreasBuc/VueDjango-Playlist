from django.urls import path, include
from songs.api import views as apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('songs', apiviews.SongsViewSet)
router.register('songs-ids', apiviews.SongsIDViewSet)
router.register('playlists', apiviews.PlaylistViewSet)
router.register('playlists-wo-spongs-details',
                apiviews.PlaylistWOSongDetailsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add-remove-song/<int:p_pk>/<int:s_pk>/',
         apiviews.PlaylistAddRemoveAPIView.as_view(), name='add-remove-song'),
]
