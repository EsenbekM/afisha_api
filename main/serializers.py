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