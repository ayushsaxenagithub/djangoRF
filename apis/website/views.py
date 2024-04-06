from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.



@api_view(['GET','PUT','POST','DELETE','PATCH',])
def PersonList(request):
    if request.method == 'GET':
        persons = Profile.objects.all()
        serializer = ProfileSerializer(persons, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfileSerializer(data=request.data)
        if(serializer.is_valid()):
            # print(serializer.data)
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.data, status=400)
    return Response(request.data, status=200)

#  send a POST request:
    # {
    #     "name": "Sahil",
    #     "age": 22,
    #     "description": "Hello, This side Sahil Saxena"
    # }

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def profilecrud(request,pk):
    try:
        profile = Profile.objects.get(id=pk)
    except Profile.DoesNotExist:
        return Response({'message': 'Profile not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProfileSerializer(profile)
        return Response(serializer.data, status=200)

    elif request.method == 'PUT':
        serializer = ProfileSerializer(profile,data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(status = 500)
    elif request.method == 'PATCH':
        serializer = ProfileSerializer(profile, data = request.data, partial = True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(status = 500)
    elif request.method == 'DELETE':
        serializer = ProfileSerializer(profile)
        if(serializer.is_valid()):
            serializer.delete()
            return Response({'message':'Profile deleted successfully'})


    


