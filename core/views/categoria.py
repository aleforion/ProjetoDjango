from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models.controle import Categoria
from core.forms.formulario import CategoriaForm


@login_required
def inserir_categoria(request):
    dados = {}
    dados['form'] = CategoriaForm()
    dados['lista_categoria'] = Categoria.objects.all()
    categoria = CategoriaForm(request.POST)
    if categoria.is_valid():
        categoria.save()
        return redirect('inserir_categoria')
    return render(request, 'core/inserir_categoria.html', dados)

@login_required
def atualizar_categoria(request, pk):
    dados = {}
    categoria = Categoria.objects.get(id=pk)
    dados['form'] = CategoriaForm(instance=categoria)
    dados['pk'] = pk
    return render(request, 'core/atualizar_categoria.html', dados)

@login_required
def cotegoria_atualizada(request):
    categoria = Categoria.objects.get(pk=request.POST['id_categoria'])
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('inserir_categoria')

@login_required
def delete_categoria(request):
    id = request.POST['nameHidden']
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('inserir_categoria')