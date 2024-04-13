from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Profile, Details
from .serializers import ProfileSerializer, DetailsSerializer
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


    
class DetailsList(APIView):
    def get(self, request):
        detail = Details.objects.all()
        serializer = DetailsSerializer(detail, many = True)
        return Response(serializer.data,status = 200)
    def post(self,request): # put pk after request
        data = request.data
        serializer = DetailsSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status = 200)
        else:
            return Response(status=500)
        

class DetailsCrud(APIView):
    def get(self, request, pk):
        detail = Details.objects.get(id = pk)
        serializer = DetailsSerializer(detail)
        return Response(serializer.data,status = 200)
    def post(self, request, pk):
        data = request.data
        detail = Details.objects.get(id = pk)
        serializer = DetailsSerializer(detail,data = data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status = 200)
        else:
            return Response(serializer.data, status = 400)
    def put(self,request, pk):
        data = request.data
        detail = Details.objects.get(id = pk)
        serializer = DetailsSerializer(detail, data = data)
        if(serializer.is_valid()):
            serializer.save()
        else:
            return Response(serializer.data, status = 400)
    def patch(self, request, pk):
        data = request.data
        detail = Details.objects.get(id = pk)
        serializer = DetailsSerializer(detail, data = data, partial = True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status = 200)
        else:
            return Response(serializer.data, status =400)
    def delete(self, request, pk):
        detail = Details.objects.get(id = pk)
        serializer = DetailsSerializer(detail)
        if(serializer.is_valid()):
            serializer.delete()
            return Response({'message':'Profile deleted successfully'})
        else:
            return Response({'message':'Something went wrong'})


        