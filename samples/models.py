from django.db import models
from products.models import Product
from assembly.models import Assembly


class Sample(models.Model):
    assembly = models.ForeignKey(
        Assembly,
        on_delete=models.PROTECT,
        related_name='samples'
    )
    products = models.ManyToManyField(Product, related_name='samples')

    def __str__(self):
        return f'{self.assembly} - {", ".join([product.part_number for product in self.products.all()])}'
