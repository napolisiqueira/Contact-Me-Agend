from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone', 'email', 'description', 'category',
        )
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Felipe'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Napoli'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder': '11 22334 5678'
                }
            ),
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                'ABC não é um valor valido.',
                code='invalid'
                )
            )
        return first_name
        