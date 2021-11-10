from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, Group 
from django.db.models.fields import EmailField
from django.db.models.fields.files import FileField 
from django_countries.fields import CountryField
from django.utils.translation import gettext as _
import uuid
import os
class AccountManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,country, password=None):
        """
        Creates and saves a User with the given email, username, first_name, last_name, country and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            country=country,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name,last_name,country, password=None):
        """
        Creates and saves a superuser with the given email, first_name ,last_name, country code  and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            country=country,
        )
        user.is_admin = True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user
class Account(AbstractBaseUser ):
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users') 
    
    id = models.UUIDField(primary_key=True , default= uuid.uuid4 , editable=False)
    username = None 
    email = models.EmailField( verbose_name=_('email address'), max_length=255, unique=True,)
    first_name = models.CharField(verbose_name=_('first name'),max_length=55,)
    last_name = models.CharField(verbose_name=_('last name'),max_length=55,)
    country = CountryField()
    date_joined = models.DateField(verbose_name=_('date joined'),auto_now_add=True)
    last_login=models.DateTimeField(verbose_name=_('last login'),auto_now_add=True)
    is_active = models.BooleanField(verbose_name =_('Account active'),default=True)
    is_admin = models.BooleanField(verbose_name =_('Is administrator'),default=False)
    is_staff = models.BooleanField(verbose_name =_('staff'), default=False)
    is_superuser = models.BooleanField(verbose_name =_('super user'),default=False)
    is_reviewer = models.BooleanField(verbose_name =_('reviewer'),default=False)
    is_editor = models.BooleanField(verbose_name =_('editor'),default=False)
    is_chief_editor = models.BooleanField(verbose_name =_('editor in chief'),default=False)
    is_author = models.BooleanField(verbose_name =_('author'),default=False)
    is_publisher = models.BooleanField(verbose_name =_('publisher'),default=False)
    

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name','country']


    def __str__(self):
        return  self.email 

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
    
    
    

def author_directory_path(instance, filename): 
        return 'Resume Author/user_{0}/{1}'.format(instance.user.id, filename)
class Author(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=255,verbose_name=_('Profession') , default=None )
    institution = models.CharField(max_length=255,verbose_name=_('Institution') , default=None )
    domain_of_interest = models.CharField(max_length=255,verbose_name=_('Domain of Interest') , default=None )
    laboratory_affiliation = models.CharField(max_length=255,verbose_name=_('Laboratory Affiliation'), default=None )
    biography = models.TextField (max_length=700,verbose_name=_('Short biography') , default=None , blank=False)
    resume = models.FileField(_("Resume"), upload_to=author_directory_path , null=True,  blank=False )
    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Author') 
        
    

def reviewer_directory_path(instance, filename): 
    return 'Resume Reviewer/user_{0}/{1}'.format(instance.user.id, filename)
class Reviewer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=255,verbose_name=_('Profession')  )
    domain_of_research = models.CharField(max_length=255,verbose_name=_('Domain of Research') , default=None )
    biography = models.TextField (max_length=700,verbose_name=_('Short biography') , default=None , blank=False)
    resume = models.FileField(_("Resume"), upload_to=reviewer_directory_path, max_length=100 , null=True , blank= False)   
    class Meta:
        verbose_name = _('Reviewer')
        verbose_name_plural = _('Reviewers') 
        
    
def editor_directory_path(instance, filename): 
    return 'Resume Editor/user_{0}/{1}'.format(instance.user.id, filename)
class Editor(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=255,verbose_name=_('Profession') , default=None )
    domain_of_research = models.CharField(max_length=255,verbose_name=_('Domain of Research') , default=None )
    biography = models.TextField (max_length=700,verbose_name=_('Short biography') , default=None , blank=False)
    resume = models.FileField(_("Resume"), upload_to=editor_directory_path, max_length=100 , null=True , blank= False)   
    class Meta:
        verbose_name = _('Editor')
        verbose_name_plural = _('Editors') 





def editor_in_chief_directory_path(instance, filename): 
    return 'Resume EditorInChief/user_{0}/{1}'.format(instance.user.id, filename)
class EditorInChief(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    profession = models.CharField(max_length=255,verbose_name=_('Profession') , default=None )
    domain_of_research = models.CharField(max_length=255,verbose_name=_('Domain of Research') , default=None )
    biography = models.TextField (max_length=700,verbose_name=_('Short biography') , default=None , blank=False)
    resume = models.FileField(_("Resume"), upload_to=editor_in_chief_directory_path, max_length=100 , null=True , blank= False)   
    class Meta:
        verbose_name = _('Editor In Chief')
        verbose_name_plural = _('Editors In Chief')     
class Publisher(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, primary_key=True)
    affiliation = models.CharField(max_length=255,verbose_name=_('Affiliation') , default=None )
    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers') 