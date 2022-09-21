from cgitb import lookup
from django.urls import path,include
from . import views 
from rest_framework_nested import routers

rota = routers.DefaultRouter()
rota.register('tipoClient',views.TiposCliente,basename='tipoClient')
rota.register('client',views.Cliente,basename='client')
rota.register('user',views.Usuario,basename='user')
rota.register('conta',views.Conta,basename='conta')
rota.register('endereco',views.Endereco,basename='endereco')
rota.register('transf',views.Transferencia,basename='transf')
rota.register('cartao',views.Cartoes,basename='cartao')
rota.register('faturas',views.Faturas,basename='faturas')
rota.register('empr',views.Emprestimos,basename='empr')
rota.register('pgtoEmp',views.PgtoEmprestimo,basename='pgtoEmp')
rota.register('extrato',views.Extrato,basename='extrato')

rota_cliente =routers.NestedSimpleRouter(rota,'client',lookup='client')

urlpatterns = [
    path('',include(rota.urls)),
    path('',include(rota_cliente))
]
