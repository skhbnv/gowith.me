from rest_framework import serializers
from dp.models import Events


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id', 'event_id', 'eventArticle', 'eventLocation', 'eventCategory', 'user')


