from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Details
from .serializers import ProfileSerializer, DetailsSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

@api_view(['GET','PUT','POST','DELETE','PATCH'])
def PersonList(request):
    if request.method == 'GET':
        persons = Profile.objects.all()
        serializer = ProfileSerializer(persons, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def profilecrud(request, pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profile.delete()
        return Response({'message': 'Profile deleted successfully'}, status=status.HTTP_200_OK)

class DetailsList(APIView):
    def get(self, request):
        details = Details.objects.all()
        serializer = DetailsSerializer(details, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = DetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DetailsCrud(APIView):
    def get(self, request, pk):
        try:
            detail = Details.objects.get(id=pk)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        try:
            detail = Details.objects.get(id=pk)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            detail = Details.objects.get(id=pk)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(detail, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            detail = Details.objects.get(id=pk)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = DetailsSerializer(detail, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            detail = Details.objects.get(id=pk)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        detail.delete()
        return Response({'message': 'Details deleted successfully'}, status=status.HTTP_200_OK)

class FullDetails(APIView):
    def get(self, request, pk):
        try:
            profile = Profile.objects.get(id=pk)
            detail = Details.objects.filter(profile=profile)
        except Profile.DoesNotExist:
            return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
        except Details.DoesNotExist:
            return Response({'message': 'Details not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer_profile = ProfileSerializer(profile)
        serializer_detail = DetailsSerializer(detail, many = True)
        full_detail = {'profile': serializer_profile.data, 'detail': serializer_detail.data}
        return Response(full_detail, status=status.HTTP_200_OK)
