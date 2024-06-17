from django.shortcuts import render

from cars.models import Car


# Create your views here.
def car_view(request):
    template = "cars.html"

    cars = Car.objects.all().order_by("brand", "model")
    search = request.GET.get("search")

    if search:
        cars = cars.filter(model__icontains=search)

    context = {
        "cars": cars,
    }
    return render(request, template, context)
