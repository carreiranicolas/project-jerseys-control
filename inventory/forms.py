from django import forms 
from .models import Camisa

class CamisaForm(forms.ModelForm):
    class Meta:
        model = Camisa
        fields = '__all__'
