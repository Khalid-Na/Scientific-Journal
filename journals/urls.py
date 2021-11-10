from django.urls import path 
from . import views

app_name = 'journals'

urlpatterns = [
    
    path('Authors-guide/',views.auth_guide_view,name='auth_guide'),
    path('About/',views.about_journal_view,name='about_journal'),
    
    
]