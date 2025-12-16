from django.db import models
from django.conf import settings
from core.helpers.models import BaseModel

class Category(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='nome',
        verbose_name='Nome'
    )
    
    description = models.TextField(
        blank=True,
        db_column='descricao',
        verbose_name='Descricao'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'tb_categoria'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
