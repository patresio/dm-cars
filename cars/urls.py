from django.urls import path

from cars.views import car_view

urlpatterns = [
    path("", car_view, name="cars_list"),
]
