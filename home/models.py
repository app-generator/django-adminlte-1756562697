# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Trackingconfiguration(models.Model):

    #__Trackingconfiguration_FIELDS__
    par = models.CharField(max_length=255, null=True, blank=True)
    timeframe = models.CharField(max_length=255, null=True, blank=True)

    #__Trackingconfiguration_FIELDS__END

    class Meta:
        verbose_name        = _("Trackingconfiguration")
        verbose_name_plural = _("Trackingconfiguration")


class Candle(models.Model):

    #__Candle_FIELDS__
    open = models.IntegerField(null=True, blank=True)
    close = models.IntegerField(null=True, blank=True)
    high = models.IntegerField(null=True, blank=True)
    low = models.IntegerField(null=True, blank=True)
    quotevol = models.IntegerField(null=True, blank=True)
    basevol = models.IntegerField(null=True, blank=True)
    timestamp = models.IntegerField(null=True, blank=True)
    time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    tracking_configuration = models.ForeignKey(TrackingConfiguration, on_delete=models.CASCADE)

    #__Candle_FIELDS__END

    class Meta:
        verbose_name        = _("Candle")
        verbose_name_plural = _("Candle")



#__MODELS__END
