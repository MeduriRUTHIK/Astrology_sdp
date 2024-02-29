from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('aboutpage', views.aboutpage, name='aboutpage'),
    path('register', views.register, name='register'),
    path('', views.home, name='home'),
    path('checklogin', views.checklogin, name='checklogin'),
    path('zodiac', views.zodiac, name='zodiac'),
    path('horoscopic', views.horoscope, name='horoscopic'),
    path('feedback', views.feedback, name='feedback'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('updatepassword', views.updatepwd, name='updatepassword'),
    path('checklogin', views.home, name='checklogin'),
    path('contact', views.contact, name='contact'),
    path('help', views.help, name='help'),
]
