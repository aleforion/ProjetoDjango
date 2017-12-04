from django.forms import  ModelForm
from django import forms
from core.models.controle import Conta, Categoria


class CategoriaForm(ModelForm):
    model = Categoria


class ContaForm(ModelForm):
    model = Conta


