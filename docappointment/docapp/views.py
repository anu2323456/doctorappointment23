from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404
from .models import *
from .serializer import *

@api_view(['POST'])

def add_doctors(request):
    try:
        data=request.data
        serializer=DocSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response('Data added sucessfully')
        
    except Exception as e:
        return Response({"status": "failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR) 


@api_view(['GET'])
def getdoctors(request):
    try:
        q=Doctors.objects.all()
        serializer=DocSerializer(q,many=True)
        return Response({'message':'data retrieved sucesssfully','data':serializer.data})
    
    except Exception as e:
        return Response({"status": "failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def getdocdetail(request,id):
    try:
        id=id
        q=Doctors.objects.filter(id=id).first()
        serializer=DocSerializer(q,many=False)
        return Response({'message':'data retrieved sucesssfully','data':serializer.data})
    
    except Exception as e:
        return Response({"status": "failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])

def checkdocavailability(request,id):
    try:
        id=id
        q=Doctors.objects.filter(id=id).first()
        availability=q.availability
       
        return Response({'message':'data retrieved sucesssfully','data':availability})
    
    except Exception as e:
        return Response({"status": "failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

@api_view(['POST'])
def Bookappointment(request):
    try: 
        doctor_id = request.data.get('id') 
        print(doctor_id) 
        doctor = Doctors.objects.filter(id=doctor_id).first()
        
        if doctor:
            print(doctor)
            data = request.data.copy()
            data['doctor'] = doctor.id 
            serializer = DocappontmentSerializer(data=data)
        
            
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Booked successfully'})
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Doctor not found'}, status=status.HTTP_404_NOT_FOUND)
    
    except Exception as e:
        return Response({"status": "failed", "error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
