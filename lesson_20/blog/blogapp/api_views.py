from .models import Vacancy, Skills
from .serializers import SkillsSerializer #, PostSerializer
from rest_framework import viewsets


class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer