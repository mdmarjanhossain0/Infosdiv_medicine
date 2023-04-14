from django.core.management.base import BaseCommand
from django.db import connection
import requests

cursor = connection.cursor()


import json


from medicine.models import GenericMedicineBangla, GenericMedicine, Medicine


class Command(BaseCommand):
    help = "Creating model objects according the file path specified"

    def handle(self, *args, **options):
        with open("drugs.json") as json_file:
            data = json.load(json_file)
            for item in data:
                try:
                    if int(item.get("generic_id", 0)) == 0:
                        if item.get("url", ""):
                            slug = item.get("url", "")
                        else:
                            slug = ""
                        medicine = Medicine(
                            pk=item.get("drug_id", None),
                            name=item.get("name", None),
                            generic_id=None,
                            generic_bn=None,
                            type=item.get("type_id", None),
                            manufacturer=item.get("manufacturer_id", None),
                            generic_name=item.get("generic_name", None),
                            manufacturer_name=item.get("manufacturer_name", None),
                            measurement_unit=item.get("measurement_unit", None),
                            category=item.get("category", None),
                            weight=item.get("weight", None),
                            price=item.get("price", None),
                            view_count=0,
                            medicine_type=item.get("drug_type", None),
                            consumer_type=item.get("consume_type", None),
                            medicine_type_bn=item.get("drug_type_bn", None),
                            slug=slug,
                        )
                        medicine.save()
                        print(item.get("drug_id", None))
                except:
                    print(item)
