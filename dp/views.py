from dp.serializers import *
from rest_framework import generics
from dp.models import Events


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class LocationCreateView(generics.CreateAPIView):
    serializer_class = LocationDetailSerializer


class CategoriesCreateView(generics.CreateAPIView):
    serializer_class = CategoriesDetailSerializer


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UsersDetailSerializer


class ImagesCreateView(generics.CreateAPIView):
    serializer_class = ImagesDetailSerializer


class CommentsCreateView(generics.CreateAPIView):
    serializer_class = CommentsDetailSerializer


class UsersCreateView(generics.CreateAPIView):
    serializer_class = UsersDetailSerializer


class EventsListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Events.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Events.objects.all()
