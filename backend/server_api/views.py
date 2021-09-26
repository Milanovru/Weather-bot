from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import RegistrationSerializer, SubscriberSerializer
from django.contrib.auth.models import User
from .models import Subscriber
from rest_framework.permissions import IsAdminUser



class RegistrationViewSet(viewsets.ModelViewSet):

    serializer_class = RegistrationSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UsersViewSet(viewsets.ModelViewSet):

    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = [IsAdminUser]
