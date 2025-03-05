from django.contrib import admin
from samples.models import Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Sample.
    """
    list_display = ('id', 'assembly', 'product_list', 'created_at', 'updated_at')
    list_filter = ('assembly',)
    search_fields = ('assembly__name', 'products__part_number')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('assembly',)
        }),
        ('Produtos Associados', {
            'fields': ('products',),
            'classes': ('collapse',)  # Oculta esta seção por padrão
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Oculta esta seção por padrão
        }),
    )

    def product_list(self, obj):
        """
        Exibe até 3 produtos associados à amostra, adicionando "..." se houver mais.
        """
        products = obj.products.all()[:3]
        product_names = ", ".join([product.part_number for product in products])
        if obj.products.count() > 3:
            product_names += "..."
        return product_names
    product_list.short_description = 'Products'