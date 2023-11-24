from django import forms
from .models import usuario

class usuarioForm(forms.ModelForm):

    class Meta:
        model = usuario
        fields = [
            'nome',
            'idade',
            ]
        widgets = {
            'nome': forms.TextInput(attrs={'autofocus': True}),
        }
        def __init__(self) -> None:
            self.fields['nome'].widget.attrs['onfocus']