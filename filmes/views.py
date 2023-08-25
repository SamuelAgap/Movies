from django.shortcuts import render
from rest_framework import viewsets

from filmes.models import Actor, Movie
from filmes.serializer import ActorSerializer, MovieSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
