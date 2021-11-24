from django.urls import path
from .views import home, login, registro, page1, adminT, adminU, crearTrivia, crearUsuario, partida, ruleta,ranking,loginParticipante,iniciarPartida,recuperarClave,score,lobbyP,lobbyAdm,configPartida,avatarP
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
    path('ruleta/', ruleta, name="ruleta"),
    path('ranking/', ranking, name="ranking"),
    path('loginParticipante/', loginParticipante, name="loginParticipante"),
    path('iniciarPartida/', iniciarPartida, name="iniciarPartida"),
    path('recuperarClave/', recuperarClave, name="recuperarClave"),
    path('score/', score, name="score"),
    path('lobbyP/', lobbyP, name="lobbyP"),
    path('lobbyAdm/', lobbyAdm, name="lobbyAdm"),
    path('configPartida/', configPartida, name="configPartida"),
    path('avatarP/', avatarP, name="avatarP"),
]