from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
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
def allSender(request):
    data = Sender.objects.all().order_by('-id')
    serializer = SenderSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailSender(request, pk ):
    data = Sender.objects.get(id=pk)
    serializer = SenderSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateSender(request):
    data = request.data 
    serializer = SenderSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateSender(request, pk):
    data = Sender.objects.get(id = pk)
    serializer = SenderSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteSender(request, pk):
    data = Sender.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Sender deleted successfully"
    })


#--------------------------------------------------





@api_view(['GET'])
def allCategory(request):
    data = Category.objects.all().order_by('-id')
    serializer = CategorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailCategory(request, pk ):
    data = Category.objects.get(id=pk)
    serializer = CategorySerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateCategory(request):
    data = request.data 
    serializer = CategorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateCategory(request, pk):
    data = Category.objects.get(id = pk)
    serializer = CategorySerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteCategory(request, pk):
    data = Category.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })




#--------------------upload bulk mail and save this into receiver-----------------------------



@api_view(['POST'])
def createBulkReceiver(request):
    if 'file' in request.FILES:
        csv_file = request.FILES['file']
        try:
            df = pd.read_csv(csv_file)

            receivers_data = []
            for _, row in df.iterrows():
                receiver_data = {
                    'email': row['gmail'],
                }

                if 'name' in row and not pd.isna(row['name']):
                    receiver_data['name'] = row['name']
                if 'phone' in row and not pd.isna(row['phone']):
                    receiver_data['phone'] = row['phone']
                if 'address' in row and not pd.isna(row['address']):
                    receiver_data['address'] = row['address']

                receivers_data.append(receiver_data)

            receivers = Receiver.objects.bulk_create([Receiver(**data) for data in receivers_data])

            serializer = ReceiverSerializer(receivers, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'error': 'Error processing the CSV file'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        data = request.data
        serializer = ReceiverSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








#---------------------Receiver Crud---------------------------------




@api_view(['GET'])
def allReceiver(request):
    data = Receiver.objects.all().order_by('-id')
    serializer = ReceiverSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailReceiver(request, pk ):
    data = Receiver.objects.get(id=pk)
    serializer = ReceiverSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateReceiver(request):
    data = request.data 
    serializer = ReceiverSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateReceiver(request, pk):
    data = Receiver.objects.get(id = pk)
    serializer = ReceiverSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteReceiver(request, pk):
    data = Receiver.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Category deleted successfully"
    })


#--------------------Template CRUD----------------------------


@api_view(['GET'])
def allTemplate(request):
    data = Template.objects.all().order_by('-id')
    serializer = TemplateSerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailTemplate(request, pk ):
    data = Template.objects.get(id=pk)
    serializer = TemplateSerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateTemplate(request):
    data = request.data 
    serializer = TemplateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateTemplate(request, pk):
    data = Template.objects.get(id = pk)
    serializer = TemplateSerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteTemplate(request, pk):
    data = Template.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" Template deleted successfully"
    })



#-----------------------History Crud--------------------------



@api_view(['GET'])
def allHistory(request):
    data = History.objects.all().order_by('-id')
    serializer = HistorySerializer(data, many=True)
    return Response(serializer.data)
    
    
    
    
    
    
@api_view(['GET'])
def detailHistory(request, pk ):
    data = History.objects.get(id=pk)
    serializer = HistorySerializer(data)
    return Response(serializer.data)






@api_view(['POST'])
def CreateHistory(request):
    data = request.data 
    serializer = HistorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['POST'])
def UpdateHistory(request, pk):
    data = History.objects.get(id = pk)
    serializer = HistorySerializer(instance=data, data=request.data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)






@api_view(['DELETE'])
def deleteHistory(request, pk):
    data = History.objects.get(id=pk)
    data.delete()
    return Response({
        "message":" History deleted successfully"
    })




#--------------------Single Email Send--------------------------------------------





@api_view(['POST'])
def sendEmailToEmail(request, sender_id):
    try:
        sender = Sender.objects.get(id=sender_id)

        subject = request.data.get('subject', "Default Subject")
        message = request.data.get('message', "Default Message")

        recipient_email = request.data.get('recipient_email', '')

        if not recipient_email:
            return Response({'error': 'Recipient email is required'}, status=status.HTTP_400_BAD_REQUEST)

        # List to store the email sending results
        email_results = []

        from_email = sender.EMAIL_HOST_USER

        custom_email_backend = CustomEmailBackend(sender)

        # Send the email to the recipient's email address
        try:
            recipient_list = [recipient_email]
            email = EmailMessage(subject, message, from_email, recipient_list, connection=custom_email_backend)

            print("before")
            email.send()
            print("after")

            history = History(sender=sender.EMAIL_HOST_USER, receiver=recipient_email, subject=subject, message=message)
            history.save()

            email_results.append({'recipient_email': recipient_email, 'status': 'Email sent'})
        except BadHeaderError:
            email_results.append({'recipient_email': recipient_email, 'status': 'Invalid header found'})
        except Exception as e:
            print(f"Error sending email to recipient {recipient_email}: {str(e)}")
            email_results.append({'recipient_email': recipient_email, 'status': 'Error sending the email'})

        return Response(email_results, status=status.HTTP_200_OK)
    except Sender.DoesNotExist:
        return Response({'error': 'Sender not found'}, status=status.HTTP_404_NOT_FOUND)




#-------------------------Using Celery for sending Multiple email to Receivers----------------------------------




@shared_task
def send_email_task(sender_id, subject, message, receiver_ids):
    try:
        sender = Sender.objects.get(id=sender_id)
        from_email = sender.EMAIL_HOST_USER
        custom_email_backend = CustomEmailBackend(sender)

        email_results = []

        for receiver_id in receiver_ids:
            try:
                receiver = Receiver.objects.get(id=receiver_id)
                recipient_list = [receiver.email]

                email = EmailMessage(subject, message, from_email, recipient_list, connection=custom_email_backend)
                email.send()

                receiver.email_sent = True
                receiver.save()

                history = History(sender=sender.EMAIL_HOST_USER, receiver=receiver.email, subject=subject, message=message)
                history.save()

                email_results.append({'receiver_id': receiver_id, 'status': 'Email sent'})
            except Receiver.DoesNotExist:
                email_results.append({'receiver_id': receiver_id, 'status': 'Receiver not found'})
            except Exception as e:
                print(f"Error sending email to receiver {receiver_id}: {str(e)}")
                email_results.append({'receiver_id': receiver_id, 'status': 'Error sending the email'})
            finally:
                custom_email_backend.close() 

        return email_results
    except Sender.DoesNotExist:
        return [{'error': 'Sender not found'}]





@api_view(['POST'])
def sendEmailToReceivers(request, sender_id):
    try:
        sender = Sender.objects.get(id=sender_id)  # Assuming Sender is a model in yourapp

        subject = request.data.get('subject', "Default Subject")
        message = request.data.get('message', "Default Message")
        receiver_ids = request.data.get('receiver_ids', [])

        email_results = send_email_task.delay(sender_id, subject, message, receiver_ids)

        return Response({'task_id': email_results.id}, status=status.HTTP_202_ACCEPTED)

    except Sender.DoesNotExist: 
        return Response({'error': 'Sender not found'}, status=status.HTTP_404_NOT_FOUND)