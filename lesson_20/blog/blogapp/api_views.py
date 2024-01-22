from .models import Vacancy, Skills
from .serializers import SkillsSerializer, VacancySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .permissions import ReadOnly, IsAuthor
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication


class SkillsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser | ReadOnly]
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class VacancyViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAdminUser | IsAuthor | ReadOnly]
    #permission_classes = [IsAdminUser | IsAuthor]
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer