from django.urls import path

from cars.views import (
    CarDeleteView,
    CarDetailView,
    CarListView,
    CarUpdateView,
    NewCarCreateView,
)

app_name = "car"

urlpatterns = [
    path("", CarListView.as_view(), name="list"),
    path("new/", NewCarCreateView.as_view(), name="new"),
    path("<int:pk>", CarDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", CarUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", CarDeleteView.as_view(), name="delete"),
]
