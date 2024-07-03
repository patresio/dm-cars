from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from cars.forms import CarModelForm
from cars.models import Car


class CarListView(ListView):
    model = Car
    template_name = "cars.html"
    context_object_name = "cars"

    def get_queryset(self):
        cars = super().get_queryset().order_by("model")
        search = self.request.GET.get("search")
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class NewCarCreateView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = "new_car.html"
    success_url = "/cars/"


class CarDetailView(DetailView):
    model = Car
    template_name = "car_detail.html"


class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = "car_update.html"
    success_url = "/cars/"


class CarDeleteView(DeleteView):
    pass
