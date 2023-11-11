from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from knox.auth import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters


from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404

import csv
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
import pandas as pd

from django.core.mail import send_mail
from email_marketing.email_utils import CustomEmailBackend
from django.core.mail.message import EmailMessage 
from django.core.mail import send_mail, BadHeaderError


from celery import shared_task




# Create your views here.



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allSender(request):
    data = Sender.objects.all().order_by('-id')
    serializer = SenderSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailSender(request, pk ):
    data = Sender.objects.get(id=pk)
    serializer = SenderSerializer(data)
    return Response(serializer.data)











@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteSender(request, pk):
    data = Sender.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Sender deleted successfully"
    })


#--------------------------------------------------





@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allCategory(request):
    data = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailCategory(request, pk ):
    data = Category.objects.get(id=pk)
    serializer = CategorySerializer(data)
    return Response(serializer.data)












@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteCategory(request, pk):
    data = Category.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })











#---------------------Receiver Crud---------------------------------




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allReceiver(request):
    data = Receiver.objects.all().order_by('-id')
    serializer = ReceiverSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailReceiver(request, pk ):
    data = Receiver.objects.get(id=pk)
    serializer = ReceiverSerializer(data)
    return Response(serializer.data)












@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteReceiver(request, pk):
    data = Receiver.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })




#----------------------ReceiverCategory Crud-----------------




@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allReceiverCategory(request):
    data = ReceiverCategory.objects.all().order_by('-id')
    serializer = ReceiverCategorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailReceiverCategory(request, pk ):
    data = ReceiverCategory.objects.get(id=pk)
    serializer = ReceiverCategorySerializer(data)
    return Response(serializer.data)












@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteReceiverCategory(request, pk):
    data = ReceiverCategory.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" ReceiverCategory deleted successfully"
    })







#--------------------Template CRUD----------------------------


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allTemplate(request):
    data = Template.objects.all().order_by('-id')
    serializer = TemplateSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailTemplate(request, pk ):
    data = Template.objects.get(id=pk)
    serializer = TemplateSerializer(data)
    return Response(serializer.data)









@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteTemplate(request, pk):
    data = Template.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Template deleted successfully"
    })



#-----------------------History Crud--------------------------



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def allHistory(request):
    data = History.objects.all().order_by('-id')
    serializer = HistorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detailHistory(request, pk ):
    data = History.objects.get(id=pk)
    serializer = HistorySerializer(data)
    return Response(serializer.data)










@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def deleteHistory(request, pk):
    data = History.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" History deleted successfully"
    })

