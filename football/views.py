from django.shortcuts import render
from .models import Team
# Create your views here.
def home(request):
    return render(request, 'football/index.html')

def teams(request):

    teams_list = Team.objects.all() # objects is a static attribute. it gives us all the objects/attributes associated with that team (i.e. SELECT * FROM Team)
    context = {'list_of_teams' : teams_list}
    return render(request, 'football/teams.html', context)

def manutd(request):
    team_object = Team.objects.get(name = 'Chelsea')
    players_list = team_object.player_set.all()
    context = {'list_of_players': players_list, 'team': team_object}
    return render(request, 'football/showplayers.html', context)

def teamPlayers(request, teamID):
    team_object = Team.objects.get(id = teamID)
    players_list = team_object.player_set.all()
    context = {'list_of_players': players_list, 'team': team_object.name}
    return render(request, 'football/showplayers.html', context)

def gcd(request):
    # read user input: first and second number
    number1 = int(request.POST.get('first'))
    number2 = int(request.POST.get('second'))

    # compute the GCD
    result = calc_gcd(number1, number2)

    # put the result in the context
    context = {"first" : number1, "second": number2, "result": result}

    return render(request, 'football/show_gcd.html', context)

def calc_gcd(a, b):
    if(b == 0):
        return a
    else:
        return calc_gcd(b, a % b)

