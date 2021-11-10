from django.db import models
from accounts.models import Author
from django.utils.translation import gettext as _

# Create your models here.
class Articles(models.Model):
    id_author = models.ForeignKey(Author, on_delete=models.CASCADE)
    Title = models.CharField(max_length=255 )
    Abstract = models.TextField (max_length=700 )
    Journal = models.CharField(max_length=255 )



    # user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)


    
    # profession = models.CharField(max_length=255,verbose_name=_('Profession') , default=None )
    # institution = models.CharField(max_length=255,verbose_name=_('Institution') , default=None )
    # domain_of_interest = models.CharField(max_length=255,verbose_name=_('Domain of Interest') , default=None )
    # laboratory_affiliation = models.CharField(max_length=255,verbose_name=_('Laboratory Affiliation'), default=None )
    # biography = models.TextField (max_length=700,verbose_name=_('Short biography') , default=None , blank=False)
    # resume = models.FileField(_("Resume"), upload_to=author_directory_path , null=True,  blank=False )
    
