from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from .forms import LoginUserForm, RegForm
from .models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.contrib import messages
from django.views.generic.detail import DetailView
from django.views.generic import ListView, CreateView
from django.views import View

categories = [{'name': 'Animals', 'url_name': '/categories/Animals'},
              {'name': 'Colors', 'url_name': '/categories/Colors'},
              {'name': 'Technic', 'url_name': '/categories/Technic'}]


class RegistrationView(CreateView):
    form_class = RegForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')


class UserProfileView(DetailView):
    model = User
    template_name = "user_account.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = categories
        return context


class MainView(View):

    def get(self, request):
        return render(request, 'index.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse('user_account', kwargs={'slug': self.request.user.slug})


def logoutpage(request):
    logout(request)
    return redirect('login')



# def loginpage(request):
#     if request.method == 'GET':
#         form = LoginForm()
#         return render(request, 'login.html', context={'form': form})
#     else:
#         data = request.POST
#         form = LoginForm(data)
#         try:
#             user = authenticate(username=form.data['username'],
#                                     password=form.data['password'])
#             if user is None:
#                 return HttpResponse('Пользователя с таким логином или паролем не существует')
#             else:
#                 login(request, user)
#                 return redirect(f'user_account')
#         except Exception as e:
#             return HttpResponse(f'Что-то пошло не так. Ошибка: {e}')


# def registrationpage(request):
#     if request.method == 'GET':
#         form = RegForm()
#         return render(request, 'registration.html', context={'form': form})
#     elif request.method == 'POST':
#         form = RegForm(request.POST)
#         if form.is_valid(): #TODO: написать проверку через try
#             post = form.save(commit=False)
#             post.save()
#             return HttpResponse('Вы успешно зарегистрировались')
#         else:
#             return render(request, 'registration.html', {'form':form})