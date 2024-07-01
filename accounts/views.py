from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def register_view(request):
    user_form = UserCreationForm()
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("accounts:login")

    context = {
        "user_form": user_form,
    }
    return render(request, "register.html", context)


def login_view(request):
    login_form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("car:list")

    context = {
        "login_form": login_form,
    }
    return render(request, "login.html", context)


def logout_view(request):
    print("usuario: ", request.user)
    logout(request)
    print("logout")
    return redirect("accounts:login")
