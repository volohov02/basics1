from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import ContactForm, PostForm
from django.core.mail import send_mail
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Vacancy
from .models import Skills
from django.views.generic.base import ContextMixin

class VacancyListView(ListView):
    model = Vacancy
    template_name = 'blogapp/index.html'
    context_object_name = 'vacancy'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Vacancy.objects.all()


class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'СКИЛЛ'
        return context

class PostFormMixin(ContextMixin):
    def post(self, request, *args, **kwargs):
        """
        Пришел пост запрос
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return super().post(request, *args, **kwargs)

class SkillsListView(ListView, NameContextMixin):
    model = Skills
    template_name = 'blogapp/skills_list.html'
    context_object_name = 'skills'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        return Skills.objects.all()

class SkillsDetailView(DetailView, NameContextMixin):
    model = Skills
    template_name = 'blogapp/skill_detail.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.skill_id = kwargs['pk']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Skills, pk=self.skill_id)

class SkillsCreateView(CreateView, NameContextMixin, PostFormMixin):
    # form_class =
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('blog:skills_list')
    template_name = 'blogapp/skill_create.html'

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        return super().form_valid(form)


class SkillsUpdataView(UpdateView):
    fields = '__all__'
    model = Skills
    success_url = reverse_lazy('blog:skills_list')
    template_name = 'blogapp/skill_create.html'

class SkillsDeleteView(DeleteView):
    template_name = 'blogapp/skill_delete.html'
    model = Skills
    success_url = reverse_lazy('blog:skills_list')


class ContactCreateView:

    def contact_view(self, request):
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                # Получить данные из форы
                name = form.cleaned_data['name']
                message = form.cleaned_data['message']
                email = form.cleaned_data['email']

                send_mail(
                    'Contact message',
                    f'Ваш сообщение {message} принято',
                    'volohov@aaanet.ru',
                    ['volohov@aaanet.ru'],
                    fail_silently=True,
                )

                return HttpResponseRedirect(reverse('blog:index'))
        else:
            form = ContactForm()
            return render(request, 'blogapp/contact.html', context={'form': form})


class VacancyCreateView(CreateView, NameContextMixin, PostFormMixin):
    # form_class =
    fields = '__all__'
    model = Vacancy
    success_url = reverse_lazy('blog:index')
    template_name = 'blogapp/create.html'

    def form_valid(self, form):
        """
        Метод срабатывает после того как форма валидна
        :param form:
        :return:
        """
        form.instance.user = self.request.user
        return super().form_valid(form)



class VacancyDetailView(DetailView, NameContextMixin):
    model = Vacancy
    template_name = 'blogapp/post.html'

    def get(self, request, *args, **kwargs):
        """
        Метод обработки get запроса
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        self.vacancy_id = kwargs['id']
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        """
        Получение этого объекта
        :param queryset:
        :return:
        """
        return get_object_or_404(Vacancy, id=self.vacancy_id)