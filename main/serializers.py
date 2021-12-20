from rest_framework import fields, serializers
from .models import *

class FilmsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = [
            'title',
            'description',
            'cinema',
            'genres',
            ]

class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProductDatailSerializer(serializers.ModelSerializer):
    film = FilmsSerializer()