from django.contrib import admin
from server_api.models import Location, Address, Subscriber, IsSubscribed


class SubscriberAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'locations', 'data')


admin.site.register(Subscriber, SubscriberAdmin)


class LocationAdmin(admin.ModelAdmin):

    list_display = ('id', 'longitude', 'latitude')


admin.site.register(Location, LocationAdmin)


class AddressAdmin(admin.ModelAdmin):

    list_display = ('id', 'locations', 'address')


admin.site.register(Address, AddressAdmin)


class IsSubscribedAdmin(admin.ModelAdmin):

    list_display = ('id', 'is_subscribed')


admin.site.register(IsSubscribed, IsSubscribedAdmin)
