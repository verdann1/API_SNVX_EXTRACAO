from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


class Assembly(models.Model):
    """
    Representa um assembly, identificado pelo seu nome.
    Exemplos: KD01 - 1°TURNO, ENGENHARIA/QUALIDADE.
    """
    # Validação para nomes no formato "KD01 - 1°TURNO" ou "ENGENHARIA/QUALIDADE"
    ASSEMBLY_REGEX = r'^([A-Z]{2}\d{2} - \d°TURNO|ENGENHARIA/QUALIDADE)$'

    name = models.CharField(
        max_length=200,
        unique=True,
        validators=[
            RegexValidator(
                regex=ASSEMBLY_REGEX,
                message='O nome do assembly deve seguir o formato "KD01 - 1°TURNO" ou "ENGENHARIA/QUALIDADE".'
            )
        ],
        help_text='Nome do assembly (deve ser único). Exemplos: KD01 - 1°TURNO, ENGENHARIA/QUALIDADE.'
    )
    created_at = models.DateTimeField(auto_now_add=True, help_text='Data de criação do assembly.')
    updated_at = models.DateTimeField(auto_now=True, help_text='Data da última atualização do assembly.')

    def __str__(self):
        return self.name

    def clean(self):
        """
        Validações personalizadas para o modelo Assembly.
        """
        super().clean()
        if not self.name.strip():
            raise ValidationError('O nome do assembly não pode ser vazio ou conter apenas espaços.')

    class Meta:
        ordering = ['name']  # Ordenação padrão: ordem alfabética
        verbose_name = 'Assembly'
        verbose_name_plural = 'Assemblies'