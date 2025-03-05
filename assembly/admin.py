from django.contrib import admin
from assembly.models import Assembly


@admin.register(Assembly)
class AssemblyAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Assembly.
    """
    list_display = ('id', 'name', 'created_at', 'updated_at')
    list_filter = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('name',)
        }),
        ('Datas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Oculta esta seção por padrão
        }),
    )