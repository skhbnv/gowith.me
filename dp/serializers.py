from rest_framework import serializers
from dp.models import *


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['date', 'price', 'title', 'category', 'description', 'location', 'images']


class LocationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = ['latitude', 'longitude']


class CategoriesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class UsersDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class ImagesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ['poster_url', 'carousel_url1',
                  'carousel_url2', 'carousel_url3',
                  'carousel_url4', 'carousel_url5']


class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['id', 'date', 'price', 'title', 'category', 'description', 'location', 'images']
