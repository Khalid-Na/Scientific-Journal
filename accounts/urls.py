from django.urls import path , include
from django.contrib.auth import urls , views as auth_views

from accounts.views import  user , home , author, reviewer , contact

app_name = 'accounts'

urlpatterns = [
#     path('',home.home_view,name='home'),
    
    path('aboutus/',home.aboutus_view,name='aboutus'),
    path('contactus/',contact.contact_view,name='contactus'),
    path('contactus/success',contact.success_view,name='success'),
    
    
    path('signup/', user.UserSignupView.as_view(), name='user_signup'),
    path('login/',user.login_view , name='login'),
    path('logout/',user.logout_view, name = 'logout'),
   
    path('signup/author/<slug:pk>', author.author_signup_view, name='author_signup'),
    path('signup/author/<slug:pk>', author.author_signup_view, name='dash_author'),
    path('signup/reviewer/<slug:pk>', reviewer.reviewer_signup_view, name='reviewer_signup'),
    
    # path('forgot-password/',user.forgot_password_view, name = 'forgot-password'),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
         name = 'reset_password'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html')  , 
         name = 'password_reset_done'),  
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'), 
         name = 'password_reset_confirm'), 
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'), 
         name = 'password_reset_complete'), 
    
]