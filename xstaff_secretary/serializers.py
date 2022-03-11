from rest_framework import serializers
from .models import Secretary

   
        
        
class SecretarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secretary
        fields = ['doctor']
    

