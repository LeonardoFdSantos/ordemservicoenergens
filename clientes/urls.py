from django.contrib import admin
from django.urls import path
from django.conf.urls import url 
from clientes import views

urlpatterns = [
    url(r'^api/Clientes$', views.clientes_list),
    url(r'^api/Clientes/(?P<pk>[0-9]+)$', views.clientes_detail),
    url(r'^api/DadosConcessionarias$', views.DadosConcessionarias_list),
    url(r'^api/DadosConcessionarias/(?P<pk>[0-9]+)$', views.DadosConcessionarias_detail),
    url(r'^api/RespostaComercial$', views.RespostaComercial_list),
    url(r'^api/RespostaComercial/(?P<pk>[0-9]+)$', views.RespostaComercial_detail),
    url(r'^api/RespostaTecnica$', views.RespostaTecnica_list),
    url(r'^api/RespostaTecnica/(?P<pk>[0-9]+)$', views.RespostaTecnica_detail),
]