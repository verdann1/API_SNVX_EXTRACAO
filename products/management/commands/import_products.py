import csv
from django.core.management.base import BaseCommand
from products.models import Product


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo CSV com produtos',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']

        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    part_number = row['part_number']
                    project = row['project']

                    self.stdout.write(self.style.NOTICE(f'Importando: {part_number}'))

                    # Verifica se os campos existem no modelo Product
                    if hasattr(Product, 'part_number') and hasattr(Product, 'project'):
                        Product.objects.create(
                            part_number=part_number,
                            project=project,
                        )
                    else:
                        self.stdout.write(self.style.ERROR('Os campos part_number ou project não existem no modelo Product.'))

            self.stdout.write(self.style.SUCCESS('PRODUTOS IMPORTADOS COM SUCESSO!'))

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao importar produtos: {e}'))
