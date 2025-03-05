from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from samples.models import Sample

SAMPLE_TYPE_CHOICES = (
    ('centragem', 'Centragem'),
    ('cone', 'Cone'),
)

SIDE_CHOICES = (
    ('direito', 'Direito'),
    ('esquerdo', 'Esquerdo'),
)


class Result(models.Model):
    """
    Representa os resultados de testes de extração realizados em amostras.
    """
    sample = models.ForeignKey(
        Sample,
        on_delete=models.PROTECT,
        related_name='results'
    )
    force_N = models.FloatField(
        validators=[
            MinValueValidator(0.0, 'A força não pode ser inferior a 0 N.'),
        ],
        help_text='Força em Newtons (N) do teste de extração.'
    )
    result_percentage = models.FloatField(
        validators=[
            MinValueValidator(0.0, 'O resultado não pode ser inferior a 0%.'),
            MaxValueValidator(100.0, 'O resultado não pode ser superior a 100%.'),
        ],
        help_text='Resultado em porcentagem (%) do teste de extração.'
    )
    comment = models.TextField(null=True, blank=True)
    sample_taken_datetime = models.DateTimeField(
        auto_now_add=True,
        help_text='Data e hora de retirada da amostra.'
    )
    sample_extraction_datetime = models.DateTimeField(
        auto_now=True,
        help_text='Data e hora de extração da amostra.'
    )
    sample_type = models.CharField(
        max_length=10,
        choices=SAMPLE_TYPE_CHOICES,
        help_text='Tipo da amostra (centragem ou cone).'
    )
    sample_side = models.CharField(
        max_length=8,
        choices=SIDE_CHOICES,
        help_text='Lado da amostra (direito ou esquerdo).'
    )
    production_batch = models.CharField(
        max_length=100,
        help_text='Lote de produção.'
    )

    def clean(self):
        super().clean()
        if self.sample_type == 'cone' and self.force_N < 400:
            raise ValidationError({
                'force_N': 'A força para "cone" deve ser maior ou igual a 400 N.'
            })
        if self.sample_type == 'centragem' and self.force_N < 500:
            raise ValidationError({
                'force_N': 'A força para "centragem" deve ser maior ou igual a 500 N.'
            })

    def __str__(self):
        return str(self.sample)