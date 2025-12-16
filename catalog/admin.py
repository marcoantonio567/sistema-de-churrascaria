from django.contrib import admin
from .models import (
    Category,
    MenuItem,
    Ingredient,
    MenuItemIngredient,
    Additional,
    MenuItemAdditional,
    MeatPoint
)

class MenuItemIngredientInline(admin.TabularInline):
    model = MenuItemIngredient
    extra = 1
    fields = ('ingredient_id',)

class MenuItemAdditionalInline(admin.TabularInline):
    model = MenuItemAdditional
    extra = 1
    fields = ('additional_id',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name', 'description')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category_id', 'price', 'is_active')
    list_filter = ('category_id', 'is_active')
    search_fields = ('name', 'description')
    fieldsets = (
        ('Informações do Item', {
            'fields': ('name', 'category_id', 'price', 'description')
        }),
        ('Mídia e Detalhes', {
            'fields': ('image', 'estimated_time')
        }),
        ('Status', {
            'fields': ('is_active',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    inlines = [MenuItemIngredientInline, MenuItemAdditionalInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('Informações', {
            'fields': ('name',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    inlines = [MenuItemIngredientInline]

@admin.register(MenuItemIngredient)
class MenuItemIngredientAdmin(admin.ModelAdmin):
    list_display = ('menu_item_id', 'ingredient_id', 'quantity')
    list_filter = ('menu_item_id', 'ingredient_id')
    fieldsets = (
        ('Associação', {
            'fields': ('menu_item_id', 'ingredient_id', 'quantity')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(Additional)
class AdditionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    fieldsets = (
        ('Informações', {
            'fields': ('name', 'price')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
    inlines = [MenuItemAdditionalInline]

@admin.register(MenuItemAdditional)
class MenuItemAdditionalAdmin(admin.ModelAdmin):
    list_display = ('menu_item_id', 'additional_id')
    list_filter = ('menu_item_id', 'additional_id')
    fieldsets = (
        ('Associação', {
            'fields': ('menu_item_id', 'additional_id')
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

@admin.register(MeatPoint)
class MeatPointAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    fieldsets = (
        ('Informações', {
            'fields': ('name',)
        }),
        ('Metadados', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')
