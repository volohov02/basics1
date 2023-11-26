from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from blogapp.models import Vacancy, Skills
from blogapp.hh_parser import HH_servise, HH_mapper, Writer, Main

class Command(BaseCommand):

    def handle(self, *args, **options):

        # Механизм получения всех страниц с вакансиями был реализован в одном из предыдущих заданий. Поскольку цель донного задания работа с базой данных
        # здесь взята только одна (первая) страница с сотней вакансий. Из тех же соображений цикл ниже обрабатывает только двадцать первых, а не все 100
        for index in range(20):
            new_skills = Main().exec(index)
            Writer().print_skills(new_skills)
            vacancy = Vacancy.objects.create(name='Python developer', areal='Москва', description =f'Вакансия N {index}')
            for item in new_skills:
                try:
                    r = Skills.objects.filter(name=item).get()
                    count = str(int(r.description) +1)
                    print(count)
                    print(type(count))
                    print(f'skill {r} уже есть в базе')

                    skill = Skills.objects.get(name=item)
                    skill.description = count
                    skill.save()
                    vacancy.skills.add(skill)
                    vacancy.save()
                except ObjectDoesNotExist:
                    skill = Skills.objects.create(name=item, description = '1')
                    skill.save()
                    vacancy.skills.add(skill)
                    vacancy.save()



