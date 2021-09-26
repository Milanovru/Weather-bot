from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Subscriber

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')


class SubscriberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscriber
        fields = ('id','name', 'data')
