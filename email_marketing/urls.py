from django.urls import path
from .views import *
from .postviews import *

urlpatterns = [
    path('sender-list/', allSender),
    path('sender-detail/<int:pk>/', detailSender),
    path('sender-create/', CreateSender),
    path('sender-update/<int:pk>/', UpdateSender),
    path('sender-delete/<int:pk>/', deleteSender),


    path('category-list/', allCategory),
    path('category-detail/<int:pk>/', detailCategory),
    path('category-create/', CreateCategory),
    path('category-update/<int:pk>/', UpdateCategory),
    path('category-delete/<int:pk>/', deleteCategory),

    
    path('receiver-list/', allReceiver),
    path('receiver-detail/<int:pk>/', detailReceiver),
    path('receiver-create/', CreateReceiver),
    path('receiver-update/<int:pk>/', UpdateReceiver),
    path('receiver-delete/<int:pk>/', deleteReceiver),


    path('templete-list/', allTemplate),
    path('templete-detail/<int:pk>/', detailTemplate),
    path('templete-create/', CreateTemplate),
    path('templete-update/<int:pk>/', UpdateTemplate),
    path('templete-delete/<int:pk>/', deleteTemplate),



    path('receiver-category-list/', allReceiverCategory),
    path('receiver-category-detail/<int:pk>/', detailReceiverCategory),
    path('receiver-category-create/', CreateReceiverCategory),
    path('receiver-category-update/<int:pk>/', UpdateReceiverCategory),
    path('receiver-category-delete/<int:pk>/', deleteReceiverCategory),



    
    path('history-list/', allHistory),
    path('History-detail/<int:pk>/', detailHistory),
    path('History-create/', CreateHistory),
    path('History-update/<int:pk>/', UpdateHistory),
    path('History-delete/<int:pk>/', deleteHistory),
    
    
    path('bulk/', createBulkReceiver),

    path('send_email_to_receiver/<int:sender_id>/', sendEmailToReceivers),


    path('single-email/<int:sender_id>/', sendEmailToEmail),
    
    path('search/', searchCategory.as_view()),
]
