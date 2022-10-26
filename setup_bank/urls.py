
from django.urls import path,include
from . import views 
from rest_framework_nested import routers

rota = routers.DefaultRouter()

rota.register('client',views.ClienteViewSet,basename='client')
rota.register('user',views.UsuarioViewSet,basename='user')
rota.register('conta',views.ContaViewSet,basename='conta')
rota.register('transf',views.TransfViewSet,basename='transf')
rota.register('cartao',views.CartaoViewSet,basename='cartao')
rota.register('faturas',views.FaturaViewSet,basename='faturas')
rota.register('empr',views.EmprestimoViewSet,basename='empr')
rota.register('pgtoEmp',views.PgtoEmprViewSet,basename='pgtoEmp')
rota.register('extrato',views.ExtratoViewSet,basename='extrato')



urlpatterns = rota.urls
