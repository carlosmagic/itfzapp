# Django
from django import forms
from django.forms import ModelForm, DateInput, RadioSelect, NumberInput, TextInput

# wger
from wger.core.models import UserProfile
from wger.wellness.models import WellnessEntry
from django.contrib.auth.models import User

class NewWellnessEntry(forms.ModelForm):
    class Meta:
        model = WellnessEntry
        fields=('user',
                'wellness_date',
                'wellnes_energy',
                'wellnes_sleep', 
                'wellnes_motivation',
                'wellnes_stress', 
                'wellnes_hungry',
                'wellnes_steps', 
                'wellnes_bath',
                'wellnes_fasting'
                )
        widgets = {
            'user': TextInput(),
            'wellness_date': DateInput(attrs={'type':"date"}),
            'wellnes_energy': RadioSelect(attrs={'type':"radio"}),
            'wellnes_sleep': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            'wellnes_motivation': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            'wellnes_stress': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            'wellnes_hungry': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            'wellnes_steps': NumberInput(attrs={'cols': 80, 'rows': 20}),
            'wellnes_bath': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            'wellnes_fasting': RadioSelect(attrs={'cols': 80, 'rows': 20}),
            

        }
       
    
