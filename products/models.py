from django.db import models


PROJECT_CHOICES = (
    ('GM', 'GEM'),
    ('VW', '27X'),
    ('23X', '23X'),
    ('216', '216'),
    ('ONIX', 'ONIX'),
    ('MCO', 'MCO'),
    ('GEM', 'GEM'),
    ('CRETA', 'CRETA'),
    ('BR2-HB20', 'BR2-HB20'),
    ('SU2B-CRETA', 'SU2B-CRETA'),
    ('Chery', 'Chery 15/T17/T1A'),
)


class Product(models.Model):
    part_number = models.CharField(max_length=255)
    project = models.CharField(
        max_length=100,
        choices=PROJECT_CHOICES,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.part_number
