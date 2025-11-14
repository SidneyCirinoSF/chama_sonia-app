import uuid
from django.db import models

class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    titulo = models.CharField(max_length=100)

    descricao = models.TextField(max_length=500)

    status = models.CharField(
        max_length=30,
        choices=[
                ('ABERTO', 'Aberto'),
                ('FECHADO', 'Fechado'),
            ],
            default='ABERTO'
    )

    prioridade = models.CharField(
        max_length=30,
        choices=[
                ('ALTA', 'Alta'),
                ('MEDIA', 'Média'),
                ('BAIXA', 'Baixa'),
            ],
            default='MEDIA'
    )

    usuario = models.ForeignKey(
        'user.Usuario',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='tickets'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo