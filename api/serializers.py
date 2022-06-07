from wsgiref import validate
from rest_framework import serializers
from .models import Customers

class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        exclude = ('user',)
        extra_kwargs = {
            'user':{'read_only':True}
        }
    
    def validate(self, attrs):
        attrs['user_id'] = self.context['request'].user.id
        return attrs