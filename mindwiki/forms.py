from django import forms
from mindwiki.models import Page


class PageForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Page
        widgets = {
            'body': forms.Textarea(attrs={'id': 'editor'})
        }
