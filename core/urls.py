from django.conf.urls import url
from core.views import controle, categoria


urlpatterns = [
    url(r'^$', controle.inicio, name="inicio"),
    url(r'^inserir_conta/$', controle.inserir_conta, name="inserir_conta"),
    url(r'^inserir/$', controle.inserir, name='inserir'),
    url(r'^delete/(?P<pk>\d+)/$', controle.delete, name='delete'),
    url(r'atualizar_conta/(?P<pk>\d+)/$', controle.atualizar_conta, name='atualizar_conta'),
    url(r'conta_atualizada/$', controle.conta_atualizada, name='conta_atualizada'),
    url(r'^inserir_categoria/$', categoria.inserir_categoria, name='inserir_categoria'),
    url(r'^categoria_adicionada/$', categoria.categoria_adicionada, name='categoria_adicionada'),
    url(r'atualizar_categoria/(?P<pk>\d+)/$', categoria.atualizar_categoria, name='atualizar_categoria'),
    url(r'categoria_atualizada/$', categoria.cotegoria_atualizada, name='categoria_atualizada'),
    url(r'^delete_categoria/(?P<pk>\d+)/$', categoria.delete_categoria, name='delete_categoria'),
]