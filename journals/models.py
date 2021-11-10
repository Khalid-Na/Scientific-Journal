from django.contrib import admin
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Journals (models.Model):
    journal_id = models.BigAutoField(_("Journal ID"), primary_key=True)
    class Meta:
        verbose_name = _('Journal')
        verbose_name_plural = _('Journals') 
        

class Volume (models.Model):
    volume_id = models.BigAutoField(_("Volume ID"), primary_key=True)
    

class Issue (models.Model):
    issue_id = models.BigAutoField(_("Issue ID"), primary_key=True)