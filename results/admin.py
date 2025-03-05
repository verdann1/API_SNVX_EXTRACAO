from django.contrib import admin
from results.models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    """
    Configuração do admin para o modelo Result.
    """
    list_display = (
        'id',
        'sample',
        'force_N',
        'result_percentage',
        'comment_truncated',
        'sample_taken_datetime',
        'sample_extraction_datetime',
        'sample_type',
        'sample_side',
        'production_batch'
    )
    list_filter = ('sample_type', 'sample_side', 'production_batch', 'sample_taken_datetime')
    search_fields = ('sample__assembly__name', 'production_batch', 'comment')
    ordering = ('-sample_taken_datetime',)
    readonly_fields = ('sample_taken_datetime', 'sample_extraction_datetime')

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('sample', 'force_N', 'result_percentage', 'comment')
        }),
        ('Detalhes da Amostra', {
            'fields': (
                'sample_taken_datetime',
                'sample_extraction_datetime',
                'sample_type',
                'sample_side',
                'production_batch'
            ),
            'classes': ('collapse',)  # Oculta esta seção por padrão
        }),
    )

    def comment_truncated(self, obj):
        """
        Exibe apenas os primeiros 30 caracteres do comentário.
        """
        return obj.comment[:30] + "..." if obj.comment else "-"
    comment_truncated.short_description = 'Comment'