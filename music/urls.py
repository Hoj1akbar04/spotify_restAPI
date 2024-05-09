from django.urls import path, include
from .views import LandingPageView, SongAPIViewSet, AlbumAPIViewSet, ArtistAPIViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework import viewsets
from django.contrib import admin


router = DefaultRouter()
router.register("songs", viewset=SongAPIViewSet)
router.register("artists", viewset=ArtistAPIViewSet)
router.register("albums", viewset=AlbumAPIViewSet)


urlpatterns = [
    path('landing/', LandingPageView.as_view(), name='landing'),
    path("", include(router.urls)),
    path('auth/', views.obtain_auth_token)
]
