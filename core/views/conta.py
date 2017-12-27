from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models.controle import Conta, Categoria
from core.forms.formulario import ContaForm
from django.db.models import Sum
from django.http import JsonResponse

@login_required
def inicio (request):
    dados = {}
    dados['lista_conta'] = Conta.objects.all().order_by('-descricao')
    dados['soma'] = Conta.objects.all().aggregate(Sum('valor'))
    dados['vPagos'] = Conta.objects.filter(pago=True).aggregate(Sum('valor'))
    dados['vNaoPagos'] = Conta.objects.filter(pago=False).aggregate(Sum('valor'))
    dados['categorias'] = Categoria.objects.all()
    return render(request, 'core/lista_conta.html', dados)

@login_required
def inserir_conta(request):
    dados = {}
    dados['form'] = ContaForm()
    conta = ContaForm(request.POST)
    if conta.is_valid():
        conta.save()
        lista_conta = {}
        dados_conta = []
        contas = Conta.objects.all().order_by('descricao')
        for c in contas:
            if c.vencimento == "" or c.vencimento == None:
                c.vencimento = ""
            else:
                registro_conta = {'descricao': c.descricao, 'categoria': c.categoria.nome, 'valor': c.valor,
                                  'vencimento': c.vencimento, 'pago': c.pago, 'id': c.id}
                dados_conta.append(registro_conta)
            lista_conta['lista_conta'] = dados_conta
        return JsonResponse(lista_conta)
    return render(request, 'core/inserir_conta.html', dados)

@login_required
def atualizar_conta(request, pk):
    dados = {}
    conta = Conta.objects.get(id=pk)
    dados['form'] = ContaForm(instance=conta)
    dados['pk'] = pk
    return render(request, 'core/atualizar_conta.html', dados)

@login_required
def conta_atualizada(request):
    conta = Conta.objects.get(pk=request.POST['id_conta'])
    form = ContaForm(request.POST or None, instance=conta)
    if form.is_valid:
        form.save()
        return redirect('inicio')

@login_required
def delete(request):
    id = request.POST['nameHidden']
    conta = Conta.objects.get(id=id)
    conta.delete()
    return redirect('inicio')


