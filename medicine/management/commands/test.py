from django.core.management.base import BaseCommand
from django.db import connection
import requests

cursor = connection.cursor()


import json


from medicine.models import GenericMedicineBangla, GenericMedicine


class Command(BaseCommand):
    help = "Creating model objects according the file path specified"

    def handle(self, *args, **options):
        with open("drug_generics.json") as json_file:
            data = json.load(json_file)
            for item in data:
                # try:

                if item.get("url", ""):
                    slug = item.get("url", "")
                else:
                    slug = ""
                medicine = GenericMedicine(
                    pk=item.get("drug_generic_id"),
                    medicine_generic=item.get("drug_generic", None),
                    introduction=item.get("introduction", None),
                    uses_for=item.get("uses_for", None),
                    therapeutic_class=item.get("therapeutic_class", None),
                    dose=item.get("dose", None),
                    administration=item.get("administration", None),
                    side_effect=item.get("side_effect", None),
                    precaution=item.get("precaution", None),
                    interaction=item.get("interaction", None),
                    pregnancy_lactation_use=item.get("pregnancy_lactation_use", None),
                    acute_overdose=item.get("acute_overdose", None),
                    contraindication=item.get("contraindication", None),
                    use_direction=item.get("use_direction", None),
                    storage_condition=item.get("storage_condition", None),
                    special_warning=item.get("special_warning", None),
                    interaction_other_medicine=item.get(
                        "interaction_other_madicine", None
                    ),
                    slug=slug,
                    ads=item.get("ads", None),
                )
                medicine.save()
                print(item.get("drug_generic_id", None))
            # except:
            #     print(item)
