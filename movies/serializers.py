from rest_framework import serializers
from .models import RatingMovie
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    added_by = serializers.CharField(read_only=True, source="user.email")
    title = serializers.CharField(max_length=127,)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField( choices=RatingMovie.choices, default=RatingMovie.G)
    synopsis = serializers.CharField(max_length=255, default="")


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
