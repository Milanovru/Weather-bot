from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account


class AccountCreationForm(UserCreationForm):

    class Meta(UserCreationForm):

        model = Account
        fields = ('username', 'email', 'phone')


class AccountChangeForm(UserChangeForm):

    class Meta:

        model = Account
        fields = ('username', 'email', 'phone')
