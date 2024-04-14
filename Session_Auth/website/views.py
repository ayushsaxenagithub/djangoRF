from django.shortcuts import render
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotAuthenticated
from django.contrib.auth import authenticate, login, logout
from rest_framework import status

class WHOAMI(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        if not request.user.is_authenticated:
            content = {
            'message': 'You are not authenticated',
            }
            raise NotAuthenticated("User is not authenticated")
            # return Response(content,status=200)
        # user = request.user
        content = {
            'user': str(request.user),  
            'auth': str(request.auth),  
        }
        return Response(content,status=200)
    

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(APIView):
    def post(self, request):
        if not request.user.is_authenticated:
            content = {
            'message': 'You are not authenticated',
            }
            raise NotAuthenticated("User is not authenticated")
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)
    
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # user.is_staff = True
            # user.is_superuser = True
            # user.save()
            return Response({'message': 'Registration successful'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


