from django.contrib import admin

# Register your models here.
from .models import Products,ContactUs,OrderUpdate,abc
admin.site.register(Products)
admin.site.register(ContactUs)
admin.site.register(OrderUpdate)
admin.site.register(abc)

