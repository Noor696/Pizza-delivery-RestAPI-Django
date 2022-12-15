from rest_framework import serializers
from .models import PizzaOrder , CustomerFeedback

class PizzaOrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model= PizzaOrder
        fields=['order_status', 'size', 'quantity','flavour']
        # fields='__all__'

class CustomerFeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model= CustomerFeedback
        fields='__all__'