from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import  status
from django.contrib.auth import get_user_model
from .models import PizzaOrder

from django.urls import reverse

# Create your tests here.

class PizzaOrderTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(
            username="testuser1", password="pass",
        )
        testuser1.save()

        testuser2 = get_user_model().objects.create_user(
            username="testuser2", password="pass",
        )
        testuser2.save()

        test_PizzaOrder = PizzaOrder.objects.create(
            size="Small",
            customer=testuser1,
            order_status = "Pending"
        )
        test_PizzaOrder.save()

    def setUp(self):
        self.client.login(username='testuser1', password="pass")


    def test_PizzaOrder_model(self):
        pizzaOrder = PizzaOrder.objects.get(id=1)
        actual_customer = str(pizzaOrder.customer)
        actual_size = str(pizzaOrder.size)
        actual_order_status = str(pizzaOrder.order_status)
        self.assertEqual(actual_customer, "testuser1")
        self.assertEqual(actual_size, "Small")
        self.assertEqual(actual_order_status, "Pending")

    def test_get_PizzaOrder_list(self):
        url = reverse("PizaaOrder_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        pizaaOrder = response.data
        self.assertEqual(len(pizaaOrder), 1)
        
