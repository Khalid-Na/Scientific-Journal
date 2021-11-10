from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate 
from django.db.models import fields
from django.forms.models import ModelForm
from django_countries.fields import CountryField
from django.contrib.auth import authenticate
from django.db import transaction
from django.forms.utils import ValidationError
from .models import Account , Author, Reviewer

class UserSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True, help_text='Required. Add a valid email address')
    first_name = forms.CharField(max_length=55,required=True ,  help_text='Required. Enter your first name' )
    last_name =forms.CharField(max_length=55,required=True  ,  help_text='Required. Enter your last name')
    country = CountryField(blank_label=_('Select country')) 
    class Meta(UserCreationForm):
        model = Account
        fields = (
                  'email',
                  'first_name',
                  'last_name',
                  'country',
                  'password1',
                  'password2',
                  )

    
class AuthorSignupForm (forms.ModelForm):
    profession = forms.CharField( max_length=255, required=True)
    institution = forms.CharField(max_length=255, required=True )
    domain_of_interest = forms.CharField(max_length=255, required=True )
    laboratory_affiliation = forms.CharField(max_length=255, required=True )
    biography = forms.TextInput (attrs={'size': 700, 'title': 'Short bio'} )
    resume = forms.FileField(required=True)
    class Meta(forms.ModelForm):
        model = Author
        fields = (
                  'profession',
                  'institution' ,
                  'domain_of_interest',
                  'laboratory_affiliation',
                  'biography' ,
                'resume' ,
                  )

    def save(self,pk,profession,institution,domain_of_interest,laboratory_affiliation,biography,resume): 
        instance = Account.objects.get(id=pk)
        instance.is_author = True
        instance.save()
        instance = Author.objects.create(user = instance , 
                                        profession =profession , 
                                        institution = institution,
                                        domain_of_interest = domain_of_interest,
                                        laboratory_affiliation =laboratory_affiliation,
                                        biography =biography,
                                        resume = resume
                                        )
        return instance
class ReviewerSignupForm (forms.ModelForm):
    profession = forms.CharField( max_length=255, required=False)
    domain_of_research = forms.CharField(max_length=255, required=False )
    biography = forms.TextInput (attrs={'size': 700, 'title': 'Short bio'})
    resume = forms.FileField()
    
    class Meta(forms.ModelForm):
        model = Reviewer
        fields = (
                  'profession',
                  'domain_of_research' ,
                  'biography' ,
                  'resume' ,
                  )

    def save(self,pk,profession,domain_of_research,biography,resume): 
        instance = Account.objects.get(id=pk)
        instance.is_reviewer = True
        instance.save()
        instance = Reviewer.objects.create(user = instance , 
                                        profession =profession , 
                                        domain_of_research = domain_of_research,
                                        biography =biography,
                                        resume = resume
                                        )
        return instance

class login_form (forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    class Meta(ModelForm):
        model = Account
        fields = ('email','password')



class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)