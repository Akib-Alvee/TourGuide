from django.contrib import admin

# Register your models here.
from .models import Booking, Destination, Contact
admin.site.register(Destination),  
admin.site.register(Contact),
admin.site.register(Booking)  