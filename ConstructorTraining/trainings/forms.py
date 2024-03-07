
from django import forms
from .models import Training


class TrainingEditForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = ['title']