from django.db import models


# 21 field model and json
class GenericMedicine(models.Model):
    medicine_generic = models.CharField(max_length=225)
    introduction = models.TextField(null=True, blank=True)
    uses_for = models.TextField(null=True, blank=True)
    therapeutic_class = models.TextField(null=True, blank=True)
    dose = models.TextField(null=True, blank=True)
    administration = models.TextField(null=True, blank=True)
    side_effect = models.TextField(null=True, blank=True)
    precaution = models.TextField(null=True, blank=True)
    interaction = models.TextField(null=True, blank=True)
    pregnancy_lactation_use = models.TextField(null=True, blank=True)
    acute_overdose = models.TextField(null=True, blank=True)
    contraindication = models.TextField(null=True, blank=True)
    use_direction = models.TextField(null=True, blank=True)
    storage_condition = models.TextField(null=True, blank=True)
    special_warning = models.TextField(null=True, blank=True)
    interaction_other_medicine = models.CharField(max_length=225, null=True, blank=True)
    slug = models.CharField(max_length=300)
    ads = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)


class GenericMedicineBangla(models.Model):
    medicine_generic_en = models.ForeignKey(
        GenericMedicine, on_delete=models.SET_NULL, null=True, blank=True
    )
    medicine_generic = models.CharField(max_length=300)
    introduction = models.TextField(null=True, blank=True)
    uses_for = models.TextField(null=True, blank=True)
    therapeutic_class = models.TextField(null=True, blank=True)
    dose = models.TextField(null=True, blank=True)
    administration = models.TextField(null=True, blank=True)
    side_effect = models.TextField(null=True, blank=True)
    precaution = models.TextField(null=True, blank=True)
    interaction = models.TextField(null=True, blank=True)
    pregnancy_lactation_use = models.TextField(null=True, blank=True)
    acute_overdose = models.TextField(null=True, blank=True)
    contraindication = models.TextField(null=True, blank=True)
    use_direction = models.TextField(null=True, blank=True)
    storage_condition = models.TextField(null=True, blank=True)
    special_warning = models.TextField(null=True, blank=True)
    interaction_other_medicine = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=500)
    ads = models.CharField(max_length=150, null=True)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)


# 25323 25324 25342 25344 25389


class Medicine(models.Model):

    name = models.CharField(max_length=300)
    generic = models.ForeignKey(
        GenericMedicine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generic",
    )
    generic_bn = models.ForeignKey(
        GenericMedicine,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="generic_bn",
    )
    type = models.TextField(null=True, blank=True)
    manufacturer = models.TextField(null=True, blank=True)
    generic_name = models.TextField(null=True, blank=True)
    manufacturer_name = models.TextField(null=True, blank=True)
    measurement_unit = models.TextField(null=True, blank=True)
    category = models.TextField(null=True, blank=True)
    weight = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)
    view_count = models.TextField(null=True, blank=True)
    medicine_type = models.TextField(null=True, blank=True)
    consumer_type = models.TextField(null=True, blank=True)
    medicine_type_bn = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=500)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)


class MedicineBangla(models.Model):
    medicine = models.OneToOneField(
        Medicine, on_delete=models.SET_NULL, null=True, blank=True
    )
    medicine_bn = models.ForeignKey(
        GenericMedicineBangla, on_delete=models.SET_NULL, null=True, blank=True
    )
    name = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(verbose_name="created_at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="updated_at", auto_now=True)
