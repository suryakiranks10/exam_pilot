from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from accounts.serializers import TrainerSerializer

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from accounts.models import TrainerProfile
from accounts.serializers import TrainerProfileSerializer
from rest_framework.response import Response

class TrainerSignupView(CreateAPIView):

    serializer_class = TrainerSerializer


class TrainerRetrieveUpdateView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        auth_user = request.user

        qs = TrainerProfile.objects.get(user=auth_user)

        serializer_instance = TrainerProfileSerializer(qs)

        return Response(serializer_instance.data)

    