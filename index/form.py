from django import forms

from .models import Choice, Question

class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = ('choice_text', 'text',)
