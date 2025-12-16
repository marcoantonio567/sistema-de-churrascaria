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

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    name = models.CharField(
        max_length=150,
        db_column='nome',
        verbose_name='Nome'
    )

    category = models.ForeignKey(
        Category, 
        on_delete=models.PROTECT,
        db_column='id_categoria',
        verbose_name='Categoria'
    )

    image = models.ImageField(
        upload_to="menu_items/", 
        blank=True, 
        null=True,
        db_column='imagem',
        verbose_name='Imagem'
    )

    price = models.DecimalField(
        max_digits=8, 
        decimal_places=2,
        db_column='preco',
        verbose_name='Preco'
    )

    description = models.TextField(
        blank=True,
        db_column='descricao',
        verbose_name='Descricao'
    )

    estimated_time = models.PositiveIntegerField(
        help_text="Tempo em minutos",
        db_column='tempo_estimado',
        verbose_name='Tempo estimado'
    )

    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'tb_item_menu'
        verbose_name = 'Item do menu'
        verbose_name_plural = 'Itens do menu'

    def __str__(self):
        return self.name + ' - ' + self.category.name
