from accounts.models import Account, Author
from manuscript.models import Manuscript,Manuscript_Authors,Manu_keyword,Keywords
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .forms import Create_manuscript,Authorsform
from django.contrib.auth.decorators import login_required
import mimetypes
from django.views.generic.list import ListView
from django.forms.models import modelform_factory
from django import forms




#submit a manuscript 
@login_required
def create_manuscript(request,pk):
    FILE_TYPE = ['txt', 'docx','pdf']
    initial_author =dict( {
       
        'author':pk,
       
    })
    
   
    form_A = Create_manuscript(request.POST,request.FILES)
    form_B = Authorsform(request.POST)
    if request.method == 'POST':
        

        
        if form_A.is_valid()  :
            form_A.save()
          
            #form_B.save(False)
            #form_B.manuscript_id = form_A.manuscript_id
           # form_B.save()
            manu= form_A['manuscript_id'].value()
            return redirect('keywords/<int:manu>')
            
        return redirect ('dashboards:author')    
    context = {
            
            #'form_b':form_B,
            
        }
    form_A = Create_manuscript(initial=initial_author)
    return render(request,'manuscript/create.html', {'form_a':form_A,})

#dowloadd the example file for manuscript
 
#def download_file(request):
    # fill these variables with real values
    fl_path = 'manuscript/FILES/'
    filename = 'cv-fr.docx'

    fl = open(fl_path, 'r')
    mime_type, _ = mimetypes.guess_type(fl_path)
    response = HttpResponse(fl, content_type=mime_type)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response

#list of manuscript 

class ManuscriptList(ListView):

    model=Manuscript
    

       

    #context_object_name = 'Manuscript list'
    #queryset = Manuscript.objects
  
def apply_Reviewer(request,pk):
    return render(request,'manuscript/Manuscript list.html')


def ChooseKeywords(request,manu):
    KeywordForm = modelform_factory(Keywords,fields=('keyword',))
    KeywordForm1 = modelform_factory(Manu_keyword,fields=('manuscript','keyword'),widgets={ 'manuscript': forms.HiddenInput,})
    formset = KeywordForm(request.POST)
    formset1 = KeywordForm1(request.POST)
    manus=dict( {
       
        'manuscript':manu,
       
    })
    formset1 = KeywordForm1(initial=manus)

    if request.method == 'POST':
        
        if formset.is_valid() :
            formset.save()
            formset1.save()
        if formset1.is_valid():
            
            formset1.save()
        

    return render(request,'manuscript/manu_keyword.html', {'form':formset,'forma':formset1})


    
 
