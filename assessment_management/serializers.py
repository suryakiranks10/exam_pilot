from rest_framework import serializers
from assessment_management.models import Assesment

from question_management.models import Question

class AssesmentSerializer(serializers.ModelSerializer):

    question_count = serializers.SerializerMethodField(read_only=True)

    class Meta:

        model = Assesment

        fields = "__all__"

        read_only_fields=['id','trainer','end_time','created_at','updated_at']

    def get_question_count(self,obj):

        return Question.objects.filter(assesment=obj).count()