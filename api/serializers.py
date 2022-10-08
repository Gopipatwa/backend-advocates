from rest_framework import serializers
from api import models

class AdvocatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Advocates
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = "__all__"

class SocialSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialLink
        fields = ["platform_name","link"]