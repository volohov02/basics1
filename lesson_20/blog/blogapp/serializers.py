from django.urls import include, path

from .models import Vacancy, Skills
from rest_framework import routers, serializers, viewsets

class SkillsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class VacancySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Vacancy
        exclude = ['user']