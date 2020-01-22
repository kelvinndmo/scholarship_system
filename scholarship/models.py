# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from utils.managers import ScholarQuerySet
from authentication.models import User

from utils.models import BaseAbstractModel

# Create your models here.

# Will add cloudinary as a third parrty files handler


class Scholarship(BaseAbstractModel):
    applicant = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='aplicant', blank=True)
    birth_certificate = models.FileField(
        db_index=True, upload_to='birth_certificates')
    national_id = models.FileField(
        db_index=True, upload_to='national_id')
    adress = models.TextField(blank=True, max_length=255)
    phone = models.CharField(blank=True, max_length=255)
    school_name = models.CharField(max_length=255)
    school_adress = models.CharField(max_length=300)
    academic_level = models.CharField(max_length=20)
    year_of_completion = models.CharField(max_length=5)
    is_approved = models.BooleanField(default=False)
    sponsor = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sponsor", blank=True, null=True)
    sponsor_reason = models.CharField(max_length=100, blank=True, null=True)
    recommendation_letter = models.FileField(
        upload_to='recommendation_letter', db_index=True)

    objects = models.Manager()
    active_objects = ScholarQuerySet.as_manager()

    def __str__(self):
        return f"{self.applicant}'s scholarship'"
