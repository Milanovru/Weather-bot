from rest_framework import status, viewsets
from .serializers import SubscriberSerializer
from .models import Subscriber
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response


class SubscribersViewSet(viewsets.ModelViewSet):

    serializer_class = SubscriberSerializer
    queryset = Subscriber.objects.all()
    permission_classes = [AllowAny]

    @action(detail=True, permission_classes=[IsAuthenticated])
    def get_detail_info(self, request, pk=None):
        try:
            subscriber = Subscriber.objects.select_related().get(issubscribed__is_subscribed=True)
            return Response(
                {'id': subscriber.id,
                'name': subscriber.name,
                'data': subscriber.data,
                'status': 'подписка оформлена'
                }
            )
        except:
            subscriber = Subscriber.objects.get(id=pk)
            return Response(
                {'id': subscriber.id,
                 'name': subscriber.name,
                 'data': subscriber.data,
                 'status': 'нет активной подписки' 
                }
            )
