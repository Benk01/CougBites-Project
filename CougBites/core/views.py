from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from .models import Fooditems

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/")
    else:
        form = RegisterForm()
    return render(response, "register.html", {"form":form})

def index(response):
    return render(response, "index.html")

def food_item(response, id):
    id = "FOOD-" + str(id)
    item = Fooditems.objects.filter(food_id__exact=id)
    return render(response, "item.html", {"item":item[0]})