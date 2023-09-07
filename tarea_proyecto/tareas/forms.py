from django import forms
from .models import Tarea

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'asignada_a', 'prioridad']

    def __init__(self, *args, **kwargs):
        super(TareaForm, self).__init__(*args, **kwargs)
        # Personaliza los widgets o agrega clases CSS según tus necesidades
        self.fields['titulo'].widget.attrs.update({'class': 'form-control'})
        self.fields['descripcion'].widget.attrs.update({'class': 'form-control', 'rows': '4'})
        self.fields['asignada_a'].widget.attrs.update({'class': 'form-control'})
        self.fields['prioridad'].widget.attrs.update({'class': 'form-control'})
