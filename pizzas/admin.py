from django.contrib import admin
from .models import Toppings

# Register your models here.

from .models import Pizza

admin.site.register(Pizza)
admin.site.register(Toppings)