from rest_framework import serializers
from assessment_management.models import Assesment

class AssesmentSerializer(serializers.ModelSerializer):

    class Meta:

        model = Assesment

        fields = "__all__"

        read_only_fields=['id','trainer','end_time','created_at','updated_at']