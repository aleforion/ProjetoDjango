from django.conf.urls import url
from core.views import controle


urlpatterns = [
    url(r'^$', controle.inicio, name="inicio"),
    url(r'^inserir_conta/$', controle.inserir_conta, name="inserir_conta"),
    url(r'^inserir/$', controle.inserir, name='inserir'),
    url(r'^delete/(?P<pk>\d+)/$', controle.delete, name='delete'),
    url(r'atualizar_conta/(?P<pk>\d+)/$', controle.atualizar_conta, name='atualizar_conta'),
    url(r'conta_atualizada/$', controle.conta_atualizada, name='conta_atualizada'),
]