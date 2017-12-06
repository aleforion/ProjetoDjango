from django.shortcuts import render, redirect
from core.models.controle import Categoria
from core.forms.formulario import CategoriaForm


def inserir_categoria(request):
    dados = {}
    dados['form'] = CategoriaForm()
    dados['lista_categoria'] = Categoria.objects.all()
    return render(request, 'core/inserir_categoria.html', dados)


def categoria_adicionada(request):
    categoria = CategoriaForm(request.POST)
    if categoria.is_valid:
        categoria.save()
        return redirect('inserir_categoria')
    return redirect('inicio')


def atualizar_categoria(request, pk):
    dados = {}
    categoria = Categoria.objects.get(id=pk)
    dados['form'] = CategoriaForm(instance=categoria)
    dados['pk'] = pk
    return render(request, 'core/atualizar_categoria.html', dados)


def cotegoria_atualizada(request):
    categoria = Categoria.objects.get(pk=request.POST['id_categoria'])
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid:
        form.save()
        return redirect('inserir_categoria')


def delete_categoria(request, pk):
    categoria = Categoria.objects.get(id=pk)
    categoria.delete()
    return redirect('inserir_categoria')