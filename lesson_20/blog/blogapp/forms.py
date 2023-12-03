from django import forms
from .models import Vacancy
from .models import Skills



class ContactForm(forms.Form):
    name = forms.CharField(label='Название')
    email = forms.EmailField(label='email')
    message = forms.CharField(label='Сообщение')


class PostForm(forms.ModelForm):
    name = forms.CharField(label='Название',
                           widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))

    # Чекбоксы
    skills = forms.ModelMultipleChoiceField(queryset=Skills.objects.all(),
                                          widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Vacancy
        fields = '__all__'
        # fields = ('name', 'category')
        # exclude = ('tags',)