from django.http import HttpResponse
from django.shortcuts import render
from .models import Pasta, Salad, DinnerPlatter, Sub, PizzaOrder
# Create your views here.
def index(request):
    context = {
        "pastas": Pasta.objects.all(),
        "salads": Salad.objects.all(),
        "dinner_platters": DinnerPlatter.objects.all(),
        "subs": Sub.objects.all(),
        "pizzas": PizzaOrder.objects.all()
    }
    return render(request, "orders/index.html", context)
