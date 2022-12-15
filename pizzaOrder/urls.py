from django.urls import path 
from .views import PizaaOrderListView , PizaaOrderDetailView  


urlpatterns = [
    path('', PizaaOrderListView.as_view(),name="PizaaOrder_list"),
    path('<int:pk>', PizaaOrderDetailView.as_view(),name='PizaaOrder_detail')
]