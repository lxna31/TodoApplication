from django import forms
from django.core.exceptions import ValidationError
from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'completed']

    def clean_title(self):
        title = self.cleaned_data.get('title', '')
        if not title.strip():
            raise ValidationError('Title cannot be empty or only spaces.')
        return title.strip()