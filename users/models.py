from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Classe para definição de campos padrões em todas as tabelas
    """
    phone = models.CharField(
        max_length=20, 
        blank=True, 
        null=True, 
        db_column='telefone', 
        verbose_name='Telefone'
    )

    class Meta:
        db_table = 'tb_usuario'
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return self.username