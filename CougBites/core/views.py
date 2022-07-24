from distutils.command.install import INSTALL_SCHEMES
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
    items = Fooditems.objects.all().order_by('food_id').values()
    print(items[0])
    print(list(items[0:9]))
    return render(response, "index.html", {"items":list(items[0:9])})

def food_item(response, id):
    item = Fooditems.objects.filter(food_id__exact=id)
    return render(response, "item.html", {"item":item[0]})