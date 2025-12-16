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

class MenuItem(BaseModel):
    name = models.CharField(
        max_length=150,
        db_column='nome',
        verbose_name='Nome'
    )

    category_id = models.ForeignKey(
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
        return self.name + ' - ' + self.category_id.name

class Ingredient(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='nome',
        verbose_name='Nome'
    )

    class Meta:
        db_table = 'tb_ingredientes'
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'

    def __str__(self):
        return self.name

class MenuItemIngredient(BaseModel):
    menu_item_id = models.ForeignKey(
        MenuItem, 
        on_delete=models.CASCADE,
        db_column='id_item_menu',
        verbose_name='Item do menu'
    )
    
    ingredient_id = models.ForeignKey(
        Ingredient, 
        on_delete=models.PROTECT,
        db_column='id_ingrediente',
        verbose_name='Ingrediente'
    )

    quantity = models.PositiveIntegerField(
        default=1,
        db_column='quantidade',
        verbose_name='Quantidade'
    )

    class Meta:
        db_table = 'tb_item_menu_ingredientes'
        verbose_name = 'Ingrediente do item do menu'
        verbose_name_plural = 'Ingredientes do item do menu'

        unique_together = ('menu_item_id', 'ingredient_id')

    def __str__(self):
        return self.menu_item_id.name + ' - ' + self.ingredient_id.name

class Additional(BaseModel):
    name = models.CharField(
        max_length=100,
        db_column='nome',
        verbose_name='Nome'
    )

    price = models.DecimalField(
        max_digits=7, 
        decimal_places=2,
        db_column='preco',
        verbose_name='Preco'
    )

    class Meta:
        db_table = 'tb_adicionais'
        verbose_name = 'Adicional'
        verbose_name_plural = 'Adicionais'

        unique_together = ('name', 'price')
        
    def __str__(self):
        return self.name + ' - ' + str(self.price)

class MenuItemAdditional(BaseModel):
    menu_item_id = models.ForeignKey(
        MenuItem, 
        on_delete=models.CASCADE,
        db_column='id_item_menu',
        verbose_name='Item do menu'
    )
    
    additional_id = models.ForeignKey(
        Additional, 
        on_delete=models.PROTECT,
        db_column='id_adicional',
        verbose_name='Adicional'
    )

    class Meta:
        db_table = 'tb_item_menu_adicionais'
        verbose_name = 'Adicional do item do menu'
        verbose_name_plural = 'Adicionais do item do menu'

        unique_together = ('menu_item_id', 'additional_id')

        
    def __str__(self):
        return self.menu_item_id.name + ' - ' + self.additional_id.name

class MeatPoint(BaseModel):
    name = models.CharField(
        max_length=50,
        db_column='nome',
        verbose_name='Nome'
    )
    
    class Meta:
        db_table = 'tb_pontos_carne'
        verbose_name = 'Ponto de carne'
        verbose_name_plural = 'Pontos de carne'

    def __str__(self):
        return self.name
