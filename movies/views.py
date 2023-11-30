from django.shortcuts import render

from rest_framework.views import APIView, status, Request, Response
from .models import Movie
from .serializers import MovieSerializer
from movies_orders.serializers import MovieOrderSerializer
from .permissions import MyCustomPermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [MyCustomPermission]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all().order_by("id")
        result = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)
    
    def post(self, request: Request) -> Response:
        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_move = serializer.save(user=request.user)
        data = MovieSerializer(instance=create_move)
        return Response(data.data, status.HTTP_201_CREATED)
    
class MovieDetailView(APIView):
     
    authentication_classes = [JWTAuthentication]  
    permission_classes = [MyCustomPermission]

    def get(self, req: Request, movie_id: int) -> Response:
        
        found_movie = get_object_or_404(Movie, pk=movie_id)  
        serializer = MovieSerializer(found_movie)
        return Response(serializer.data)
     
    def delete(self, req: Request,  movie_id: int) -> Response:
        
        found_movie = get_object_or_404(Movie, pk= movie_id)
        found_movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated]

    def post(self, request: Request, movie_id: int) -> Response:

        movie = get_object_or_404(Movie, pk= movie_id )

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(movie=movie, order=request.user)  
        return Response(serializer.data, status.HTTP_201_CREATED)