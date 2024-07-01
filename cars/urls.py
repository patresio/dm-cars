from django.urls import path

from cars.views import CarListView, NewCarCreateView

app_name = "car"

urlpatterns = [
    path("", CarListView.as_view(), name="list"),
    path("new", NewCarCreateView.as_view(), name="new"),
]
