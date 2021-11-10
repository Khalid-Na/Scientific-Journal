from django.urls import path
from . import views
from manuscript.views import ManuscriptList

app_name = 'manuscript'
urlpatterns = [
    path('create/<slug:pk>',views.create_manuscript, name = 'create manuscript'),
    path('LIST/', ManuscriptList.as_view(), name = ' manuscripts'),
    path('reviewer/<int:pk>', views.apply_Reviewer, name = 'reviewer'),
    path('keywords/<int:manu>',views.ChooseKeywords, name = 'create '),
   
    
]

