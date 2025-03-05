from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Product.
    """
    list_display = ('id', 'part_number', 'project', 'suffix', 'is_active', 'created_at', 'updated_at')
    list_filter = ('project', 'is_active', 'created_at')
    search_fields = ('part_number', 'project', 'suffix')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('part_number', 'project', 'suffix', 'is_active')
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Oculta esta seção por padrão
        }),
    )