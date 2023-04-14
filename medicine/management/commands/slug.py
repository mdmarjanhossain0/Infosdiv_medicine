from django.core.management.base import BaseCommand
from django.db import connection
import requests

cursor = connection.cursor()
import json


from slugify import slugify


from medicine.models import GenericMedicineBangla, GenericMedicine, Medicine


class Command(BaseCommand):
    help = "Creating model objects according the file path specified"

    def handle(self, *args, **options):
        medicines = Medicine.objects.all()

        for medicine in medicines:
            if medicine.slug == "":
                medicine.slug = slugify(f"{medicine.name} {medicine.weight}")
                medicine.save()
                print(medicine.pk)
