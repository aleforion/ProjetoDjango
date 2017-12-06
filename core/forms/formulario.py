from django.forms import ModelForm
from core.models.controle import Conta, Categoria
from django import forms


class CategoriaForm(ModelForm):
    nome = forms.CharField(label='Nome ', widget=forms.TextInput(attrs={"class": "form-control"}))
    ativa = forms.BooleanField(label='Ativa ')

    class Meta:
        model = Categoria
        exclude =['']


class ContaForm(ModelForm):
    opcoes = Categoria.objects.all()
    descricao = forms.CharField(label='Descrição: ', widget=forms.TextInput(attrs={"class": "form-control"}))
    categoria = forms.ModelChoiceField(queryset=opcoes, label='Categoria', widget=forms.Select(attrs={"class": "form-control"}))
    valor = forms.DecimalField(label='Valor', widget=forms.NumberInput(attrs={"class": "form-control"}))
    vencimento = forms.CharField(label='Vencimento: ', widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Conta
        exclude = ['']


