from django.urls import path, include
from songs.api import views as apiviews
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('users-songs', apiviews.UsersSongsViewSet, basename='user-songs-details')
router.register('songs', apiviews.AllSongsViewSet, basename='all-songs-details')
router.register('users-songs-ids', apiviews.UsersSongsIDViewSet, basename='user-songs-ids')
router.register('users-playlists', apiviews.UsersPlaylistViewSet, basename='user-playlists-details')
router.register('users-playlists-id',
                apiviews.UsersPlaylistIDViewSet, basename='user-playlists-ids')


urlpatterns = [
    path('', include(router.urls)),
    path('users-add-remove-song/<int:p_pk>/<int:s_pk>/',
         apiviews.UsersPlaylistAddRemoveAPIView.as_view(), name='add-remove-song'),
]
