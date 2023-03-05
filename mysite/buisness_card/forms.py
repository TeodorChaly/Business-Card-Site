from django import forms
from .models import Reviews

class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['email', 'name', 'text']
        widgets = {
            'email': forms.TextInput(attrs={'readonly': 'readonly'}),
            'name': forms.TextInput(attrs={'readonly': 'readonly'})
        }