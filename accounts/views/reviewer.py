from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from ..models import Account, Author
from ..forms import AuthorSignupForm , ReviewerSignupForm

@login_required(login_url='accounts:login')
def reviewer_signup_view(request,pk):
    context={}
    user = request.user
    if user.is_reviewer==False:
        form=ReviewerSignupForm(request.POST , request.FILES)
        if request.method == 'POST':
            form=ReviewerSignupForm(request.POST , request.FILES)
            if form.is_valid():
                profession= form.cleaned_data['profession']
                domain_of_research = form.cleaned_data['domain_of_research']
                biography= form.cleaned_data['biography']
                resume= request.FILES['resume']
                form.save(pk,profession,domain_of_research,biography,resume)
                return redirect('home')
        
        context ={'form':form}
    return render(request,'accounts/signupReviewer.html',context)
    
    