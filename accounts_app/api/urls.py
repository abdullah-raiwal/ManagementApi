from django.urls import path, include
from accounts_app.api import views


urlpatterns = [
    path("registrar/signup/", views.RegistrarRegisterView.as_view(), name='registrar-signup'),
    path("registrar/login/", views.RegistrarLoginView.as_view(), name='registrar-login'),
    
    
]