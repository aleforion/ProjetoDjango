from django.forms import ModelForm
from core.models.controle import Conta, Categoria


class CategoriaForm(ModelForm):
    class Meta:
        model = Categoria
        exclude =['']


class ContaForm(ModelForm):
    class Meta:
        model = Conta
        exclude = ['']


