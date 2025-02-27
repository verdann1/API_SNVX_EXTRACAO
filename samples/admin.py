from django.contrib import admin
from samples.models import Sample


@admin.register(Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('id', 'assembly', 'product_list')

    def product_list(self, obj):
        return ", ".join([product.part_number for product in obj.products.all()])
    product_list.short_description = 'Products'
