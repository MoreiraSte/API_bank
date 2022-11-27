
from django.urls import path,include
from . import views 
from rest_framework_nested import routers

rota = routers.DefaultRouter()

rota.register('client',views.ClienteViewSet,basename='client')
rota.register('conta',views.ContaViewSet,basename='conta')
rota.register('transf',views.TransfViewSet,basename='transf')
rota.register('cartao',views.CartaoViewSet,basename='cartao')
rota.register('empr',views.EmprestimoViewSet,basename='empr')



urlpatterns = rota.urls
