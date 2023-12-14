from django.test import TestCase
from .models import Skills, Vacancy
from usersapp.models import BlogUser
from mixer.backend.django import mixer

#Create your tests here.
#class SkillsTestCaseMixer(TestCase):

    # def setUp(self):
    #     self.skills = mixer.blend(Skills)
    #
    #     # category = mixer.blend(Category, name='test_category')
    #     # self.post_str = mixer.blend(Post, name='test_post_str', category=category)
    #     # Короткая запись
    #     self.skills_str = mixer.blend(Vacansy, name='skills_post_str', category__name='test_category')
    #
    # def test_str(self):
    #     self.assertEqual(str(self.skills_str), 'test_skills_str, category: test_category')

class VacancyTestCase(TestCase):

    # def setUp(self):
    #     user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
    #     self.vacancy = Vacancy.objects.create(name='test_vacancy', text='some', user=user, skills=skills)
    #
    #     self.vacancy_str = Vacancy.objects.create(name='test_vacancy_str', text='some', user=user, skills=skills)

    def test_has_image(self):
        user = BlogUser.objects.create_user(username='test_user', email='test@test.com', password='leo1234567')
        vacancy = Vacancy.objects.create(name='test_vacancy', text='some', user=user)
        self.assertFalse(self.vacancy.has_image())

