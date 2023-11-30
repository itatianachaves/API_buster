from django.shortcuts import render

from rest_framework.views import APIView, status, Request, Response

from users.models import User
from users.serializers import UserSerializer
from .permissions import IsUserOwner
from rest_framework_simplejwt.views import TokenObtainPairView

from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LoginView(TokenObtainPairView):
    ...
class UserView(APIView):
    def post(self, request: Request) -> Response:
       
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  
        return Response(serializer.data, status.HTTP_201_CREATED)
    
class UserDetailView(APIView):

    authentication_classes = [JWTAuthentication]  
    permission_classes = [IsAuthenticated, IsUserOwner]
    
    def get(self, req: Request, user_id: int) -> Response:

        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(req, found_user) 
        serializer = UserSerializer(found_user)
        return Response(serializer.data)
    
    def patch(self, request: Request, user_id: int) -> Response:
        found_user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, found_user)
        serializer = UserSerializer(found_user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()  
        return Response(serializer.data)
        
