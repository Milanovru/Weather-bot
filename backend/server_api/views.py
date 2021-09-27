from rest_framework import status, viewsets
from rest_framework.response import Response
from .serializers import SubscriberSerializer
from .models import Subscriber
from rest_framework.permissions import IsAdminUser, AllowAny


class SubscribersViewSet(viewsets.ModelViewSet):

    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = [AllowAny]
