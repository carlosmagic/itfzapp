# Standard Library
import datetime
import logging
from decimal import Decimal

# Django
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core import mail
from django.core.cache import cache
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxValueValidator,
    MinValueValidator
)
from django.db import models
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils import (
    timezone,
    translation
)
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

# wger
from wger.core.models import Language
from wger.utils.cache import cache_mapper
from wger.utils.constants import TWOPLACES
from wger.utils.fields import Html5TimeField
from wger.utils.managers import SubmissionManager
from wger.utils.models import (
    AbstractLicenseModel,
    AbstractSubmissionModel
)
from wger.utils.units import AbstractWeight
from wger.weight.models import WeightEntry

# Create your models here.

class WellnessInfo(models.Model):
    """
    A Wellness Info for user
    """

    # Metaclass to set some other properties
    class Meta:

        # Order by creation_date, descending (oldest first)
        ordering = ["-creation_date", ]

    user = models.ForeignKey(User,
                             verbose_name=_('User'),
                             editable=False,
                             on_delete=models.CASCADE
                             )
    language = models.ForeignKey(Language,
                                 verbose_name=_('Language'),
                                 editable=False,
                                 on_delete=models.CASCADE)
    creation_date = models.DateField(_('Creation date'), auto_now_add=True)
    description = models.CharField(max_length=(80),
                                   blank=True,
                                   verbose_name=_('Description'),
                                   help_text=_('Wellness atribute filling for determinate user'))

    def __str__(self):
        """
        Return a more human-readable representation
        """
        if self.description:
            return "{0}".format(self.description)
        else:
            return "{0}".format(_("Wellness"))

class WellnessEntry(models.Model):

    class WellnessOptions(models.IntegerChoices):

        UNO = 1
        DOS = 2
        TRES = 3
        CUATRO = 4
        CINCO = 5

    class WellnessOptionsBool(models.IntegerChoices):

        NO = 0
        SI = 1   

    class Meta:
        ordering = ["wellness_date", ]



    user = models.CharField(max_length=200, null=False, blank=False)

    language = models.ForeignKey(Language,
                                 verbose_name=_('Language'),
                                 editable=False,
                                 on_delete=models.CASCADE,
                                 null=True,
                                 blank=True)

    creation_date = models.DateField(_('Date'), auto_now_add=True)
    update_date = models.DateField(_('Date'),
                                   auto_now=True,
                                   blank=True,
                                   editable=False)
    
    wellness_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False)

    wellnes_energy = models.IntegerField(choices=WellnessOptions.choices, null=False, blank=False, verbose_name="Energía")

    wellnes_sleep = models.IntegerField(choices=WellnessOptions.choices, null=False, blank=False)

    wellnes_motivation = models.IntegerField(choices=WellnessOptions.choices, null=False, blank=False)

    wellnes_stress = models.IntegerField(choices=WellnessOptions.choices, null=False, blank=False)

    wellnes_hungry = models.IntegerField(choices=WellnessOptions.choices, null=False, blank=False)

    wellnes_steps = models.IntegerField(null=False, blank=False, default=500 )

    wellnes_bath = models.IntegerField(choices=WellnessOptionsBool.choices, null=False, blank=False, default=0)

    wellnes_fasting = models.IntegerField(choices=WellnessOptionsBool.choices, null=False, blank=False, default=0)
