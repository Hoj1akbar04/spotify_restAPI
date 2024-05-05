from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Song, Artist, Album
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class LandingPageView(APIView):
    def get(self, request):
        return Response(data={'get api': 'Hello music lovers !'})

    def post(self, request):
        return Response(data={'post api': 'Hello music'})


class ArtistAPIViewSet(ModelViewSet):
    queryset =Artist.objects.all()
    serializer_class = ArtistSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class AlbumAPIViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


class SongAPIViewSet(ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
