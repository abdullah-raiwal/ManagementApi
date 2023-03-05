from django.urls import path, include
from registrar_app.api import views


urlpatterns = [
    path("upload-doc/", views.ApplicationFormView.as_view(), name='add-application'),
    path('all-applications/', views.ApplicationListView.as_view(), name='application-list')
] 