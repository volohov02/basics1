from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Vacancy
from .forms import ContactForm
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.
def main_view(request):
    vacancy = Vacancy.objects.all()
    #print(vacancy)
    return render(request, 'blogapp/index.html', context={'vacancy': vacancy})

def create_post(request):
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
        return render(request, 'blogapp/create.html', context={'form': form})



def post(request, id):
    vacancy = Vacancy.objects.get(id=id)
    return render(request, 'blogapp/post.html', context={'vacancy': vacancy})
