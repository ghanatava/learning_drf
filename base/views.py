from django.shortcuts import render,redirect
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from .models import Advocate,Company
from .serializers import *
from django.db.models import Q 
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

@api_view(['GET'])
def endpoints(request):
    data=['advocates','advocates/:username','company']
    return Response(data)

# @api_view(['GET','POST'])
# def advocates(request):

#     if request.method == 'GET':
#         query = request.GET.get('query')
        
#         if query == None:
#             query = ''   
#         advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
#         serializer=AdvocateSerializers(advocates,many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         advocate=Advocate.objects.create(
#             username=request.data['username'],
#             bio=request.data['bio']
#         )
#         serializer=AdvocateSerializers(advocate,many=False)
#         return redirect('advocates')

# Rewriting the above view as a class based view


class AdvocateList(APIView):
    
    def get(self, request): 
        query = request.GET.get('query')
        
        if query == None:
            query = ''   
        advocates = Advocate.objects.filter(Q(username__icontains=query) | Q(bio__icontains=query))
        serializer=AdvocateSerializers(advocates,many=True)
        return Response(serializer.data)
        
    def post(self, request,):
        advocate=Advocate.objects.create(
            username=request.data['username'],
            bio=request.data['bio'],
            company=request.data['company']
        )
        serializer=AdvocateSerializers(advocate,many=False)
        return redirect('advocates')



@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def advocate_detail(request, username):
    advocate = Advocate.objects.get(username=username)
    if request.method == 'GET':
        serializer=AdvocateSerializers(advocate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        advocate.username=request.data['username']
        advocate.bio=request.data['bio']
        advocate.save()
        serializer=AdvocateSerializers(advocate)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        advocate.delete()
        return Response('user was deleted')


@api_view(['GET','POST'])
def company(request):
    
    if request.method == 'GET':

        query=request.GET.get('query')
        if query == None:
            query = ''
            
        company = Company.objects.filter(Q(name__icontains=query) | Q(bio__icontains=query))
        serializer = CompanySerializer(company, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        
        company = Company.objects.create(
            name=request.data['name'],
            bio=request.data['bio']
        )
        serializer = CompanySerializer(company, many=True)
        return redirect('company')
