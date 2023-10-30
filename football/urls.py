from django.urls import path
from . import views

app_name = 'football' # to distinguish from other possible apps

urlpatterns = [
	path('', views.home, name='home'), # we have to write a view called home
    path('teams/', views.teams, name='teams'),
    path('teams/manutd', views.manutd, name='manutd'),
    path('teams/<int:teamID>', views.teamPlayers, name='teamPlayers'),
    path('teams/addNew', views.addNewTeam, name = 'addNewTeam'),
    path('teams/addNewPlayer', views.addNewPlayer, name = 'addNewPlayer'),
    path('gcd/', views.gcd, name='gcd'),
    path('chooseTeam/', views.chooseTeam, name='chooseTeam')
]