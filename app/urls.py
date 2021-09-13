from django.urls import path
from .views import home, login, registro, page1

urlpatterns = [
    path('home/', home, name="home"),
    path('', login, name="login"),
    path('registro/', registro, name="registro"),
    path('page1/', page1, name="page1"),
]