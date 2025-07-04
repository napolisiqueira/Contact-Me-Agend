from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    # def __init__(self, **args, **kwargs):
    #     super().__init__(*args, **kwargs)
    
    #     self.fields['first_name'].widget.attrs.update({
    #         'class': "class-a class-b",
    #         'placeholder': "João da Silva",
            
    #     })
    
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
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

    def clean(self):
        # cleaned_data = self.cleaned_data
        self.add_error(
            'first_name',
            ValidationError(
                'O campo é obrigatorio.',
                code='invalid'
            )
        )
        self.add_error(
            'first_name',
            ValidationError(
                'Apenas o primeiro nome.',
                code='invalid'
            )
        )
        return super().clean()
            
