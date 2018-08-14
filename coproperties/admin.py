from django.contrib import admin
from .models import *

class PropertyAdmin(admin.ModelAdmin):
    search_fields = ['name']


class CopropertyAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Property, PropertyAdmin)

admin.site.register(Coproperty, CopropertyAdmin)

admin.site.register(PropertyPhones)

