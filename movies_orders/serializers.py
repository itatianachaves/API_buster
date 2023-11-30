from rest_framework import serializers
from .models import MovieOrder

class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True, source="movie.title")
    purchased_by = serializers.CharField(read_only=True, source="order.email")
    purchased_at = serializers.DateTimeField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)


    def create(self, validated_data):
        return MovieOrder.objects.create(**validated_data)