# Pizza-delivery-RestAPI-Django

## LAB-26

## Project: Pizza-delivery-RestAPI-Django

**Author: Noor Alkhateeb**

* admin : _noor_  / pass: _noornoor_
* stuff: _bara_  / pass: barabara

* **AllowAny** : I use it in customer feedback , 
* **IsAuthenticatedOrReadOnly** : I use it to show pizza order to any one , but just the Authenticated user can make edit or create or delete on the list.

* **the App. have Two models**
1. PizzaOrder
2. CustomerFeedback

**URLS:**
> http://127.0.0.1:8011/api/v1/pizzaOrder/CustomersFeedback/1

**Run:**

> python3 manage.py runserver


**update the database:**

> python manage.py makemigrations
> python manage.py migrate

**> docker-compose up**
when run this command:
* my image will be build
* my container will be build
* take all the project and put it inside the container
* then run the server inside the container.


**Dockerfile** : to build docker image, the data inside it same for all django application.

**docker-compose.yml** : responsible to create the container