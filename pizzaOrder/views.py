from django.shortcuts import render
from .serializers  import PizzaOrderSerializer
from .models import PizzaOrder
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView

# Create your views here.
class PizaaOrderListView(ListCreateAPIView):
    # I want to show user the data and can create another data from list
    queryset = PizzaOrder.objects.all() # take all object and give him to serilizer
    serializer_class = PizzaOrderSerializer # afile resposible to convert python code to JSON data/ format


class PizaaOrderDetailView(RetrieveUpdateDestroyAPIView):

    # RetrieveUpdateDestroyAPIView : mean reading , can Updating and delet
    queryset = PizzaOrder.objects.all() 
    serializer_class = PizzaOrderSerializer

