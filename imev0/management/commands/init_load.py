from django.core.management.base import BaseCommand, CommandError
from imev0.models import Transaction
from openpyxl import load_workbook
import jdatetime as jdate


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, *args, **options):
        print(options['file_path'])
        wb = load_workbook(filename='imev0/test2.xlsx', read_only=True)
        ws = wb.active  # ws is now an IterableWorksheet
        for row in ws:
            if row[0].value == 'تاریخ':
                continue
            dates = row[0].value.split('/')
            persian_date = jdate.date(int(dates[0]), int(dates[1]), int(dates[2]))
            f = Transaction(date=persian_date, product=row[1].value, producer=row[2].value,
                            supply=float(row[5].value), demand=float(row[8].value),
                            treatment=float(row[11].value), value_KRials=float(row[16].value),
                            sub_group=row[18].value, group=row[19].value, main_group=row[20].value)
            f.save()

