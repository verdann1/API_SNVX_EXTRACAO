from django.contrib import admin
from results.models import Result

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sample',
        'force_N',
        'result_percentage',
        'comment',
        'sample_taken_datetime',
        'sample_extraction_datetime',
        'sample_type',
        'sample_side',
        'production_batch'
    )
