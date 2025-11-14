from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ticket

@login_required
def pagina_home(request):
    # Se for superusuário, mostra todos os tickets
    if request.user.is_superuser:
        tickets = Ticket.objects.all().order_by('-created_at')
    else:
        # Usuário normal só vê seus próprios tickets
        tickets = Ticket.objects.filter(usuario=request.user).order_by('-created_at')
    
    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        
        Ticket.objects.create(
            titulo=titulo,
            descricao=descricao,
            prioridade=prioridade.upper(),
            status='ABERTO',
            usuario=request.user
        )
        
        messages.success(request, f'Chamado "{titulo}" criado com sucesso!')
        return redirect('ticket:home')
    
    context = {'tickets': tickets}
    return render(request, 'ticket/home.html', context)

@login_required
def editar_ticket(request, ticket_id):
    # Superusuário pode editar qualquer ticket, usuário normal só os próprios
    if request.user.is_superuser:
        ticket = get_object_or_404(Ticket, id=ticket_id)
    else:
        ticket = get_object_or_404(Ticket, id=ticket_id, usuario=request.user)
    
    if request.method == 'POST':
        ticket.titulo = request.POST.get('titulo')
        ticket.descricao = request.POST.get('descricao')
        ticket.prioridade = request.POST.get('prioridade')
        ticket.status = request.POST.get('status')
        ticket.save()
        
        messages.success(request, f'Chamado "{ticket.titulo}" atualizado com sucesso!')
        return redirect('ticket:home')
    
    context = {'ticket': ticket}
    return render(request, 'ticket/editar_ticket.html', context)

@login_required
def deletar_ticket(request, ticket_id):
    # Superusuário pode deletar qualquer ticket, usuário normal só os próprios
    if request.user.is_superuser:
        ticket = get_object_or_404(Ticket, id=ticket_id)
    else:
        ticket = get_object_or_404(Ticket, id=ticket_id, usuario=request.user)
    
    titulo_ticket = ticket.titulo
    ticket.delete()
    
    messages.success(request, f'Chamado "{titulo_ticket}" deletado com sucesso!')
    return redirect('ticket:home')