from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput


class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['parent_name'].label = 'Отчество'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['position'].label = 'Должность'
        self.fields['TB_center'].label = 'Место работы'
        self.fields['consilium'].label = 'Координация'
        self.fields['city'].label = 'Город'
        self.fields['whatsup'].label = "WhatsApp"
        self.fields['telegram'].label = 'Telegram'
        self.fields['viber'].label = 'Viber'

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'parent_name', 'password1', 'password2', 'position',
                  'TB_center', 'consilium', 'city', 'whatsup', 'telegram', 'viber']

        widgets = {
            'username': TextInput(attrs={'placeholder': 'логин'}),
            'first_name': TextInput(attrs={'placeholder': 'имя'}),
            'last_name': TextInput(attrs={'placeholder': 'фамилия'}),
            'parent_name': TextInput(attrs={'placeholder': 'отчество'}),
            'password1': TextInput(attrs={'placeholder': 'Пароль'}),
            'password2': TextInput(attrs={'placeholder': 'Повторите пароль'}),
            # 'position': TextInput(attrs={'placeholder': 'Выберете должность'}),
            # 'TB_center': TextInput(attrs={'placeholder': 'Выберете место работы'}),
            # 'consilium': TextInput(attrs={'placeholder': 'Координация'}),
            # 'city': TextInput(attrs={'placeholder': 'Укажите город'}),
            'whatsup': TextInput(attrs={'placeholder': 'Укажите WhatsApp'}),
            'telegram': TextInput(attrs={'placeholder': 'Укажите telegram'}),
            'viber': TextInput(attrs={'placeholder': 'Укажите viber'}),
        }