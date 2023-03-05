from django.shortcuts import render
from rest_framework import generics
from registrar_app.api.serializers import ApplicationFormSerializer
from registrar_app.models import Application
from permissions import isRegistrar

class ApplicationFormView(generics.CreateAPIView):
    permission_classes = [isRegistrar]
    serializer_class = ApplicationFormSerializer


class ApplicationListView(generics.ListAPIView):
    permission_classes = [isRegistrar]
    serializer_class = ApplicationFormSerializer
    queryset = Application.objects.all()