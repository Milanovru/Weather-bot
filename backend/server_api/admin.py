from django.contrib import admin
from .models import Location, Address, Subscriber, IsSubscribed, Account
from django.contrib.auth.admin import UserAdmin
from .forms import AccountChangeForm, AccountCreationForm


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'locations', 'data')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):

    list_display = ('id', 'longitude', 'latitude')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):

    list_display = ('id', 'locations', 'address')


@admin.register(IsSubscribed)
class IsSubscribedAdmin(admin.ModelAdmin):

    list_display = ('id', 'is_subscribed')


@admin.register(Account)
class AccountAdmin(UserAdmin):
    add_form = AccountCreationForm
    form = AccountChangeForm
    model = Account
    list_display = ('id','username', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)
