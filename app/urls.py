from django.urls import path
from .views import home, login, registro, page1, adminT, adminU, crearTrivia, crearUsuario, partida

urlpatterns = [
    path('home/', home, name="home"),
    path('', login, name="login"),
    path('registro/', registro, name="registro"),
    path('page1/', page1, name="page1"),
    path('adminT/', adminT, name="adminT"),
    path('adminU/', adminU, name="adminU"),
    path('crearTrivia/', crearTrivia, name="crearTrivia"),
    path('crearUsuario/', crearUsuario, name="crearUsuario"),
    path('partida/', partida, name="partida"),
]