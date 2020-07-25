from django.urls import path
from .views import *

from django.contrib.auth import views as auth_views


urlpatterns = [
    path('registration', registration, name="register"),
    path('', login_auth, name="login"),
    path('logout/', logout_auth, name="logout"),

    path('home', homepage, name="homepage"),
    path('update-profile', update_profile, name="update"),

    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="User/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="User/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="User/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="User/password_reset_done.html"), 
        name="password_reset_complete"),

]