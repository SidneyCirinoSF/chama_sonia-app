from django.urls import path
from . import views

app_name = 'ticket'

urlpatterns = [
    path('', views.pagina_home, name='home'),
    path('editar/<uuid:ticket_id>/', views.editar_ticket, name='editar_ticket'),
    path('deletar/<uuid:ticket_id>/', views.deletar_ticket, name='deletar_ticket'),
]