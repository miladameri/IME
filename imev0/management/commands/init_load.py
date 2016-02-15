from django.core.management.base import BaseCommand, CommandError
from imev0.models import Transaction
from openpyxl import load_workbook
import datetime
from imev0.models import *


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, *args, **options):
        print(options['file_path'])
        wb = load_workbook(filename='imev0/test2.xlsx', read_only=True)
        ws = wb.active  # ws is now an IterableWorksheet
        i = 0
        for row in ws:
            if i == 0:
                i += 1
                continue
            dates = row[0].value.split('/')
            thisGroup = Group.objects.filter(name=row[19].value)
            if thisGroup == None:

            persian_date = datetime.date(int(dates[0]), int(dates[1]), int(dates[2]))
            f = Transaction(date=persian_date,
                            product=Product.objects.filter(name=row[1].value),
                            producer=Producer.objects.filter(name=row[2].value),
                            supply=float(row[5].value),
                            demand=float(row[8].value),
                            trade=float(row[11].value),
                            value_KRials=float(row[16].value),
                            group=thisGroup)
            f.save()