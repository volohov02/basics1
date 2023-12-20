from django.test import TestCase
from .models import Skills, Vacancy
from usersapp.models import BlogUser
from mixer.backend.django import mixer


class VacancyTestCase(TestCase):

    def setUp(self):
        user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
        self.vacancy = Vacancy.objects.create(name='test_vacancy', user=user)
        self.vacancy_str = Vacancy.objects.create(name='test_vacancy_str', user=user)

    def test_has_image(self):
        self.assertFalse(self.vacancy.has_image())

    def test_str(self):
        self.assertEqual(str(self.vacancy_str), 'test_vacancy_str')

class SkillsTestCase(TestCase):

    def test_str(self):
        self.skills_str = Skills.objects.create(name='test_skills_str')
        self.assertEqual(str(self.skills_str), 'test_skills_str')

