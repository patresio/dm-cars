from django.shortcuts import redirect, render
from django.views import View

from cars.forms import CarModelForm
from cars.models import Car


# Create your views here.
# def car_view(request):
#     template = "cars.html"

#     cars = Car.objects.all().order_by("brand", "model")
#     search = request.GET.get("search")

#     if search:
#         cars = cars.filter(model__icontains=search)

#     context = {
#         "cars": cars,
#     }
#     return render(request, template, context)


class CarView(View):
    def get(self, request):
        cars = Car.objects.all().order_by("brand", "model")
        search = request.GET.get("search")

        if search:
            cars = cars.filter(model__icontains=search)

        context = {
            "cars": cars,
        }
        return render(request, "cars.html", context)

# def new_car_view(request):
#     if request.method == "POST":
#         new_car_form = CarModelForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect("car:list")
#     new_car_form = CarModelForm()
#     context = {
#         "new_car_form": new_car_form,
#     }
#     return render(request, "new_car.html", context)


class NewCarView(View):
    def get(self, request):
        new_car_form = CarModelForm()
        context = {
            "new_car_form": new_car_form,
        }
        return render(request, "new_car.html", context)
    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            
            return redirect("car:list")