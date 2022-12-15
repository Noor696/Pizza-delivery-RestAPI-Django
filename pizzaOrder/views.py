from django.shortcuts import render
from .serializers  import PizzaOrderSerializer , CustomerFeedbackSerializer
from .models import PizzaOrder , CustomerFeedback
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny , IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
# Create your views here.
class PizaaOrderListView(ListCreateAPIView):
    # I want to show user the data and can create another data from list
    queryset = PizzaOrder.objects.all() # take all object and give him to serilizer
    serializer_class = PizzaOrderSerializer # afile resposible to convert python code to JSON data/ format
    permission_classes = [IsAuthenticatedOrReadOnly]

class PizaaOrderDetailView(RetrieveUpdateDestroyAPIView):

    # RetrieveUpdateDestroyAPIView : mean reading , can Updating and delet
    queryset = PizzaOrder.objects.all() 
    serializer_class = PizzaOrderSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CustomerFeedbackListView(ListCreateAPIView): # I want to make feedbac show to any user without permission
    queryset = CustomerFeedback.objects.all() 
    serializer_class = CustomerFeedbackSerializer
    permission_classes = [AllowAny]

class CustomerFeedbackDetailView(RetrieveUpdateDestroyAPIView):

    # RetrieveUpdateDestroyAPIView : mean reading , can Updating and delet
    queryset = CustomerFeedback.objects.all() 
    serializer_class = CustomerFeedbackSerializer
    permission_classes = [AllowAny]


