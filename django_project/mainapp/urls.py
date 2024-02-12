from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.MainView.as_view(), name='home'),
    path('index', views.MainView.as_view(), name='home'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('user_account/<slug:slug>', views.UserProfileView.as_view(), name='user_account'),
    path('registration', views.RegistrationView.as_view(), name='registration'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('logout', views.logoutpage, name='logout'),
    path('logout/', views.logoutpage, name='logout')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
