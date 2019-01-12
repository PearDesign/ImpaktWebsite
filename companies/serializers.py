from rest_framework import serializers

from companies.models import Assessment, Company, Metric


class MetricSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ['id']
        model = Metric


class AssessmentSerializer(serializers.ModelSerializer):
    metric = MetricSerializer(read_only=True)

    class Meta:
        exclude = ['id']
        model = Assessment


class CompanySerializer(serializers.ModelSerializer):
    assessment_set = AssessmentSerializer(read_only=True, many=True)

    class Meta:
        exclude = ['id']
        model = Company
