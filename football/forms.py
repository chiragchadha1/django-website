from django import forms
from .models import Team, Player

class TeamForm(forms.ModelForm):
    class Meta: # metadata
        model = Team
        fields = ['name', 'city'] # must match name name of the team in the models
        labels: {'name': 'Team Name', 'City': 'City of the team'}

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'team']
        labels: {'first_name': 'First Name', 'last_name': 'Last Name', 'team': 'Team Name'}