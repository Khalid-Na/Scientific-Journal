from django.shortcuts import render

# Create your views here.
def auth_guide_view (request):
    return render (request, './journals/authorsguide.html')



def about_journal_view(request):
    return render (request, './journals/aboutjournal.html')