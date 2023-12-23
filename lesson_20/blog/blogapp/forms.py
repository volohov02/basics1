from django import forms
from blogapp.models import Vacancy
from blogapp.models import Skills



class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        exclude = ['user']

    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    # Чекбоксы
    skills = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())

    # class Meta:
    #     model = Vacancy
    #     fields = ('name',)

