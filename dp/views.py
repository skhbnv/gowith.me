from dp.serializers import *
from rest_framework import generics
from dp.models import Events


class EventCreateView(generics.CreateAPIView):
    serializer_class = EventDetailSerializer


class EventsListView(generics.ListAPIView):
    serializer_class = EventListSerializer
    queryset = Events.objects.all()


class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EventDetailSerializer
    queryset = Events.objects.all()
