from .models import Vacancy, Skills
from .serializers import SkillsSerializer, VacancySerializer
from rest_framework import viewsets


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class VacancyViewSet(viewsets.ModelViewSet):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer