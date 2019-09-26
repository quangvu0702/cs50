from django.contrib import admin
from .models import Pasta, Salad, DinnerPlatter, Topping, SubExtra, Sub, PizzaOrder

# Register your models here.
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
admin.site.register(Topping)
admin.site.register(SubExtra)
admin.site.register(Sub)
admin.site.register(PizzaOrder)