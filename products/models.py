from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


PROJECT_CHOICES = (
    ('120', '120'),
    ('120 EU', '120 EU'),
    ('23X', '23X'),
    ('27X', '27X'),
    ('216', '216'),
    ('ONIX', 'Onix'),
    ('MCO', 'MCO'),
    ('GEM', 'GEM'),
    ('CRETA', 'Creta'),
    ('BR2-HB20', 'HB20 BR2'),
    ('SU2B-CRETA', 'Creta SU2B'),
    ('Chery15/T17/T1A', 'Chery 15/T17/T1A'),
)


class Product(models.Model):
    """
    Representa um produto identificado pelo seu número de peça (part_number).
    Cada produto está associado a um projeto específico.
    """
    part_number = models.CharField(
        max_length=255,
        validators=[
            RegexValidator(
                regex=r'^IM-\d{5}(-[A-Z0-9]+)?$',
                message='O número da peça deve seguir o formato IM-XXXXX ou IM-XXXXX-SUFX.'
            )
        ],
        help_text='Número da peça no formato IM-XXXXX ou IM-XXXXX-SUFX.'
    )
    project = models.CharField(
        max_length=100,
        choices=PROJECT_CHOICES,
        help_text='Projeto associado ao produto.'
    )
    suffix = models.CharField(
        max_length=10,
        blank=True,
        null=True,
        help_text='Sufixo opcional do número da peça (ex.: -BR, -DB).'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, help_text='Indica se o produto está ativo.')

    def clean(self):
        super().clean()
        if not self.project:
            raise ValidationError('O campo "project" é obrigatório.')
        if self.project not in dict(PROJECT_CHOICES):
            raise ValidationError(f'O projeto "{self.project}" não é válido.')

    def __str__(self):
        return f'{self.part_number} ({self.project})'