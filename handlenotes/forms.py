from django import forms
from .models import HandleNotes



class HandleNotesForm(forms.ModelForm):
    class Meta:
        model = HandleNotes             # verweist auf das Model in models
        fields = ['notes']              # ein spezielle Feld oder __all__