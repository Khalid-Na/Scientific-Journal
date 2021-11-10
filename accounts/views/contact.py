from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import ContactForm
from ..models import Account

def contact_view(request):
    admin = [Account.objects.filter(is_admin=True)]
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid(): 
            from_email = form.cleaned_data['from_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, admin)
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('accounts:success')
    return render(request, 'accounts/contactus.html', {'form': form})


def success_view(request):
    return render(request, 'accounts/contactsuccess.html')