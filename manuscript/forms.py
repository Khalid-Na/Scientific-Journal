from django.forms.models import modelform_factory
from accounts.models import Account, Author
from django import forms
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.forms import ModelForm, formsets, widgets
from manuscript.models import Manuscript, Manuscript_Authors,Manu_keyword
from accounts.models import Account
class Create_manuscript(ModelForm):

  """def selectAuthor(request,pk):
    author = Account.objects.get(id=pk)
    return author """
  class Meta:
      model = Manuscript 
 
      fields = '__all__'
      widgets = {
            'manuscript_id': forms.HiddenInput,
            'author': forms.HiddenInput,
            'reviewers': forms.HiddenInput,
        } 
       



class Authorsform(ModelForm):
  class Meta:
    model= Manuscript_Authors
    fields = ('name','email')
#AuthourFormset = modelformset_factory(Manuscript_Authors, fields=('name','email'))
#ormset = AuthourFormset()



    
    