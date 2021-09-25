from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegistrationSerializer
from django.contrib.auth.models import User

class RegistrationAPIView(APIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        user = RegistrationSerializer.create_user(username=request.data.get['username'], password=request.data.get['password'])
        user.save()
        
        return Response({"status": "success", "response": "User Successfully Created"}, status=status.HTTP_201_CREATED)
