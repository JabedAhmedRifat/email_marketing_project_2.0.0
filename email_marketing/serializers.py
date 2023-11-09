from rest_framework import serializers
from .models import *



class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sender 
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        
        
class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receiver
        fields = "__all__"



class ReceiverCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiverCategory
        fields = "__all__"

        
        
        
class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = "__all__"
        
        
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = "__all__"
    