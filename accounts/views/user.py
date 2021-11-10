from django.contrib import messages
from django.contrib.auth import login , authenticate , logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Count
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, UpdateView
from ..decorators import unauthenticated_user
from ..models import Account, Author
from ..forms import  UserSignupForm, login_form   #AuthorSignupForm,


class UserSignupView(CreateView):
    model = Account
    form_class = UserSignupForm
    template_name = 'accounts/signup.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
@unauthenticated_user
def login_view (request):
    user=request.user
    if request.POST:
        form = login_form(request.POST)
        if form.is_valid:
                email= request.POST['email']
                password =request.POST['password']
                user = authenticate(request , email=email , password=password)
                if user is not None and user.is_active:
                    login(request,user)
                    return redirect('home')
                else:
                    messages.info(request,'Email or password is incorrect') 
    context = {}        
    return render (request , 'accounts/login.html' , context )        

    
def logout_view (request):
    logout(request)
    return redirect('home')

def forgot_password_view(request):
    
    return redirect(request,'accounts/forgot.html')


    