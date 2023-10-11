from django.shortcuts import render
from .models import Team
# Create your views here.
def home(request):
    return render(request, 'football/index.html')

def teams(request):

    teams_list = Team.objects.all() # objects is a static attribute. it gives us all the objects/attributes associated with that team (i.e. SELECT * FROM Team)
    context = {'list_of_teams' : teams_list}
    return render(request, 'football/teams.html', context)