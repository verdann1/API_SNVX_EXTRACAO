import csv
from django.core.management.base import BaseCommand
from results.models import Result
from samples.models import Sample
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Importa dados de um arquivo CSV para o modelo Result'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Caminho para o arquivo CSV a ser importado')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    sample = Sample.objects.get(id=row['sample_id'])
                    result = Result(
                        sample=sample,
                        force_N=row['force_N'],
                        result_percentage=row['result_percentage'],
                        comment=row.get('comment', ''),
                        sample_taken_date=row['sample_taken_date'],
                        sample_extraction_date=row['sample_extraction_date'],
                        sample_type=row['sample_type'],
                        sample_side=row['sample_side'],
                        production_batch=row['production_batch']
                    )
                    result.full_clean()  # Valida os dados antes de salvar
                    result.save()
                    self.stdout.write(self.style.SUCCESS(f"Resultado importado com sucesso: {result}"))
                except ObjectDoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Sample com id {row['sample_id']} não encontrado"))
                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Erro ao importar resultado: {e}"))
