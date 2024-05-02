from django.urls import path, include
from .views import LandingPageView, ArtistView, SongAPIViewSet, AlbumDetailView, ArtistDetailView, AlbumView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("songs", viewset=SongAPIViewSet)


urlpatterns = [
    path('landing/', LandingPageView.as_view(), name='landing'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('artist/<int:id>', ArtistDetailView.as_view(), name='artist-detail'),
    path("", include(router.urls)),
    path('album/', AlbumView.as_view(), name='album'),
    path('album/<int:id>', AlbumDetailView.as_view(), name='album-detail'),

]