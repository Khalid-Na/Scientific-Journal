from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..models import Account, Author
from ..forms import AuthorSignupForm

@login_required
def author_signup_view(request,pk):
    context={}
    user = request.user
    if user.is_authenticated and user.is_author==False:
        form=AuthorSignupForm(request.POST,request.FILES )
        if request.method == 'POST':
            form=AuthorSignupForm(request.POST , request.FILES)
            if form.is_valid():
                profession= form.cleaned_data['profession']
                institution= form.cleaned_data['institution']
                domain_of_interest= form.cleaned_data['domain_of_interest']
                laboratory_affiliation= form.cleaned_data['laboratory_affiliation']
                biography= form.cleaned_data['biography']
                resume= request.FILES['resume']
                form.save(pk,profession,institution,domain_of_interest,laboratory_affiliation,biography,resume)
                return redirect('home')
            else:
                context ={'form':form}
                return render(request,'accounts/signupAuthor.html',context)
        context ={'form':form}
    return render(request,'accounts/signupAuthor.html',context)
    
    