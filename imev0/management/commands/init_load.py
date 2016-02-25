from django.core.management.base import BaseCommand, CommandError
from imev0.models import Transaction
from openpyxl import load_workbook
import datetime
from imev0.models import *


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_path', nargs=1, type=str)

    def handle(self, file_path, *args, **options):
        print(file_path)
        wb = load_workbook(filename='imev0/test2.xlsx', read_only=True)
        ws = wb.active  # ws is now an IterableWorksheet
        i = 0
        for row in ws:
            if i == 0:
                i += 1
                continue
            dates = row[0].value.split('/')


            productNum = Product.objects.filter(name=row[1].value).count()
            if productNum == 0:
                groupNum = Group.objects.filter(name=row[18].value).count()
                if groupNum == 0:
                    subGroupNum = SubGroup.objects.filter(name=row[19].value).count()
                    if subGroupNum == 0:
                        mainGroupNum = MainGroup.objects.filter(name=row[20].value).count()
                        if mainGroupNum == 0:
                            thisMain = MainGroup(name=row[20].value)
                            thisMain.save()
                        else:
                            thisMain = MainGroup.objects.filter(name=row[20].value)[0]
                        thisSub = SubGroup(name=row[19].value, mainGroup=thisMain)
                        thisSub.save()
                    else:
                        thisSub = SubGroup.objects.filter(name=row[19].value)[0]
                    thisGroup = Group(name=row[18].value, subGroup=thisSub)
                    thisGroup.save()
                else:
                    thisGroup = Group.objects.filter(name=row[18].value)[0]
                thisProduct = Product(name=row[1].value, group=thisGroup)
                thisProduct.save()
            else:
                thisProduct = Product.objects.filter(name=row[1].value)[0]

            producerNum = Producer.objects.filter(name=row[2].value).count()
            if producerNum == 0:
                thisProducer = Producer(name=row[2].value)
                thisProducer.save()
            else:
                thisProducer = Producer.objects.filter(name=row[2].value)[0]

            if thisProduct not in thisProducer.products.all():
                thisProducer.products.add(thisProduct)
            persian_date = datetime.date(int(dates[0]), int(dates[1]), int(dates[2]))

            f = Transaction(date=persian_date,
                            product=thisProduct,
                            producer=thisProducer,
                            supply=float(row[5].value),
                            demand=float(row[8].value),
                            trade=float(row[11].value),
                            value_KRials=float(row[16].value))
            f.save()