from django import forms
from .models import *

class PizzaCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        labels = {'comment':'Comments'}