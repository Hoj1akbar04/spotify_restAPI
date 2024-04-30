from django.urls import path
from .views import LandingPageView, ArtistView, AlbumView, SongView


urlpatterns = [
    path('landing/', LandingPageView.as_view(), name='landing'),
    path('artist/', ArtistView.as_view(), name='artist'),
    path('album/', AlbumView.as_view(), name='album'),
    path('song/', SongView.as_view(), name='song'),

]