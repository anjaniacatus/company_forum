from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login


def home_view(request):
    return render(request, "pages/home.html", {})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/")
    form = RegistrationForm()
    return render(
        request=request,
        template_name="registration/register.html",
        context={"form": form},
    )
