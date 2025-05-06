from django import forms
from .models import HandleNotes, Ticker



class HandleNotesForm(forms.ModelForm):
    class Meta:
        model = HandleNotes             # verweist auf das Model in models
        fields = ['notes']              # ein spezielle Feld oder __all__
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Ticker                  # Model ticker in models.py
        fields = ['ticker']             # only the field ['ticker'] not __all__
        
        
   