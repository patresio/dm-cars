from django.urls import path

from cars.views import CarView, NewCarView

app_name = "car"

urlpatterns = [
    path("", CarView.as_view(), name="list"),
    path("new", NewCarView.as_view(), name="new"),
]
