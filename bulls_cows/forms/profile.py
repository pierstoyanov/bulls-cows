from django import forms
from django.db.models import fields
from django.db.models.fields import files


from bulls_cows.models import Player

class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['player_name']
        widgets = {
            'player_name': forms.TextInput(attrs={
                'size': 15,
                'title': 'Type new name and press "Change name" to change'})
        }
        labels = {
            'player_name': 'Current PLAYER is'
        }