from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('profile/', views.profile, name='profile'),  # Личный кабинет
    path('affirmations/', views.affirmations, name='affirmations'),  # Мои аффирмации
    path('tests/', views.tests, name='tests'),  # Тесты
]
