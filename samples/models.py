from django.db import models
from assembly.models import Assembly
from products.models import Product


class Sample(models.Model):
    """
    Representa uma amostra, vinculada a um assembly específico e associada a um ou mais produtos.
    """
    assembly = models.ForeignKey(
        Assembly,
        on_delete=models.PROTECT,
        related_name='samples'
    )
    products = models.ManyToManyField(
        Product,
        related_name='samples',
        help_text='Produtos associados à amostra.'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        product_list = ", ".join([product.part_number for product in self.products.all()[:3]])
        if self.products.count() > 3:
            product_list += "..."
        return f'{self.assembly} - {product_list}'