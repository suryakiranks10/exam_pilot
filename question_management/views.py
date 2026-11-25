from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework.generics import CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import authentication,permissions

from question_management.serializers import QuestionSerializer
from assessment_management.models import Assesment

from question_management.models import Question


class QuestionCreateView(CreateAPIView):

    serializer_class = QuestionSerializer

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):

        assessment_id = self.kwargs.get("pk")

        assessment_object = get_object_or_404(Assesment,id=assessment_id)

        return serializer.save(assessment=assessment_object)


class QuestionRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class = QuestionSerializer

    queryset = Question.objects.all()