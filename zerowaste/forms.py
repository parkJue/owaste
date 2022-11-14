from django import forms
from .models import Shop, Oreview

class CommentForm(forms.ModelForm):
    class Meta:
        model = Oreview
        # fields = '__all__'
        exclude = ('article', 'user',)
        