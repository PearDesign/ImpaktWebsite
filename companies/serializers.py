from rest_framework import serializers

from companies.models import Assessment, Company, Metric


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['positive_image', 'negative_image', 'text']
        model = Metric


class AssessmentSerializer(serializers.ModelSerializer):
    metric = MetricSerializer(read_only=True)

    class Meta:
        fields = '__all__'
        model = Assessment


class CompanySerializer(serializers.ModelSerializer):
    assessment_set = AssessmentSerializer(read_only=True, many=True)

    class Meta:
        exclude = ['id']
        model = Company
