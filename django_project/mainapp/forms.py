from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from .models import User


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs=
                                                                {'class': 'special', 'placeholder': 'Введите логин'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs=
                                                                {'class': 'special', 'placeholder': 'Введите пароль'}))


class RegForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        help_texts = {
            'username': None
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'special1', 'placeholder': 'Введите ваш логин'}),
            'first_name': forms.TextInput(attrs={'class': 'special1', 'placeholder': 'Введите ваше имя'}),
            'last_name': forms.TextInput(attrs={'class': 'special1', 'placeholder': 'Введите вашу фамилию'}),
            'email': forms.EmailInput(attrs={'class': 'special1', 'placeholder': 'Введите ваш email-адрес'}),
            'password': forms.PasswordInput(attrs={'class': 'special1', 'placeholder': 'Придумайте пароль'})
        }
        labels = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password': ''
            }
        error_messages = {
            'username': {
                'unique': "Такой логин уже существует",
            }
        }

    def save(self, commit=True):
        user = super(RegForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    def clean(self):
        super(RegForm, self).clean()
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            self._errors['password'] = self.error_class([
                'Пароль должен содержать минимум 8 символов'])
        if not any(char.isdigit() for char in password):
            self._errors['password'] = self.error_class([
                'Пароль должен иметь цифры'])
        return self.cleaned_data

