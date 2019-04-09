from django import forms
from .models import SymptomUpload

class PostForm(forms.ModelForm):
    
    class Meta:
        model = SymptomUpload
        fields = '__all__'
