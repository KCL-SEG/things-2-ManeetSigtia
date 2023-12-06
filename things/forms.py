"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):

    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
    
        widgets = {
            'description': forms.Textarea(),   # Display description as a Textarea
            'quantity': forms.NumberInput(),   # Display quantity as a NumberInput
        }
