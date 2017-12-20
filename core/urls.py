from django.conf.urls import url
from core.views import conta, categoria, autenticacao


urlpatterns = [
    url(r'^$', conta.inicio, name="inicio"),
    url(r'^inserir_conta/$', conta.inserir_conta, name="inserir_conta"),
    url(r'^delete/$', conta.delete, name='delete'),
    url(r'^atualizar_conta/(?P<pk>\d+)/$', conta.atualizar_conta, name='atualizar_conta'),
    url(r'^conta_atualizada/$', conta.conta_atualizada, name='conta_atualizada'),
    url(r'^inserir_categoria/$', categoria.inserir_categoria, name='inserir_categoria'),
    url(r'^atualizar_categoria/(?P<pk>\d+)/$', categoria.atualizar_categoria, name='atualizar_categoria'),
    url(r'^categoria_atualizada/$', categoria.cotegoria_atualizada, name='categoria_atualizada'),
    url(r'^delete_categoria/$', categoria.delete_categoria, name='delete_categoria'),
    url(r'^autenticacao/$', autenticacao.auth, name='autenticacao'),
    url(r'^sair/$', autenticacao.logout_conta, name='sair')
]