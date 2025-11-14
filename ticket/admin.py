from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        'titulo', 
        'status', 
        'prioridade', 
        'usuario', 
        'created_at'
    )
    
    list_filter = ('status', 'prioridade', 'created_at')
    
    search_fields = ('titulo', 'descricao')

    ordering = ('-created_at',)