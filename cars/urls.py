from django.urls import path

from cars.views import car_view, new_car_view

app_name = "car"

urlpatterns = [
    path("", car_view, name="list"),
    path("new", new_car_view, name="new"),
]
