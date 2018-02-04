from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from .models import Map, User, Legislation

class MapAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
# Register your models here.
admin.site.register(Map)
admin.site.register(User)
admin.site.register(Legislation)
admin.site.register(MapAdmin)