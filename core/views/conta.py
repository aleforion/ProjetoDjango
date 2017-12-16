from django.shortcuts import render, redirect
from core.models.controle import Conta, Categoria
from core.forms.formulario import ContaForm
from django.db.models import Sum


def inicio (request):
    soma = 0
    dados = {}
    dados['form'] = ContaForm()
    dados['lista_conta'] = Conta.objects.all()
    dados['soma'] = Conta.objects.all().aggregate(Sum('valor'))
    dados['categorias'] = Categoria.objects.all()
    return render(request, 'core/lista_conta.html', dados)


def inserir_conta(request):
    dados = {}
    dados['form'] = ContaForm()
    dados['lista_conta'] = Conta.objects.all()
    conta = ContaForm(request.POST)
    if conta.is_valid():
        conta.save()
        return redirect('inicio')
    return render(request, 'core/inserir_conta.html', dados)


def atualizar_conta(request, pk):
    dados = {}
    conta = Conta.objects.get(id=pk)
    dados['form'] = ContaForm(instance=conta)
    dados['pk'] = pk
    return render(request, 'core/atualizar_conta.html', dados)


def conta_atualizada(request):
    conta = Conta.objects.get(pk=request.POST['id_conta'])
    form = ContaForm(request.POST or None, instance=conta)
    if form.is_valid:
        form.save()
        return redirect('inicio')


def delete(request):
    id = request.POST['nameHidden']
    conta = Conta.objects.get(id=id)
    conta.delete()
    return redirect('inicio')


