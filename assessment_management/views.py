from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from assessment_management.serializers import AssesmentSerializer
from rest_framework import authentication,permissions
from accounts.permissions import IsOwner
from assessment_management.models import Assesment

from datetime import datetime,timedelta

class AssessmentListCreateView(ListCreateAPIView):

    serializer_class=AssesmentSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[permissions.IsAuthenticated]


    def get_queryset(self):

        return Assesment.objects.filter(trainer=self.request.user)

    def perform_create(self, serializer):

        exam_date = serializer.validated_data["exam_date"]

        start_time=serializer.validated_data['start_time']
        
        duration=serializer.validated_data['duration']

        end_date_time=datetime.combine(exam_date,start_time)+timedelta(hours=duration)

        end_time=end_date_time.time()

        serializer.save(trainer=self.request.user,end_time=end_time)


class AssessmentRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    serializer_class=AssesmentSerializer

    authentication_classes=[authentication.TokenAuthentication]

    permission_classes=[IsOwner]


    def get_queryset(self):

        return Assesment.objects.filter(trainer=self.request.user)

    def perform_update(self,serializer):

        instance=serializer.instance

        start_time=serializer.validated_data.get('start_time',instance.start_time)

        exam_date=serializer.validated_data.get('exam_date',instance.exam_date)

        duration=serializer.validated_data.get('duration',instance.duration)

        end_date_time=datetime.combine(exam_date,start_time)+timedelta(hours=duration)

        end_time=end_date_time.time()
        
        serializer.save(end_time=end_time)
