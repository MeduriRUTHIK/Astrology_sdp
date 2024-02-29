from .models import feedback, registration
from django import forms
from django.contrib.auth.forms import UserCreationForm


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ('name', 'email', 'rating', 'body')
