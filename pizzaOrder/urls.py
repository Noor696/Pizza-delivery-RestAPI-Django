from django.urls import path 
from .views import PizaaOrderListView , PizaaOrderDetailView , CustomerFeedbackListView , CustomerFeedbackDetailView


urlpatterns = [
    path('', PizaaOrderListView.as_view(),name="PizaaOrder_list"),
    path('<int:pk>', PizaaOrderDetailView.as_view(),name='PizaaOrder_detail'),
    path('CustomersFeedback/', CustomerFeedbackListView.as_view(),name='CustomerFeedback_list'),
    path('CustomersFeedback/<int:pk>', CustomerFeedbackDetailView.as_view(),name='CustomerFeedback_detail')
]