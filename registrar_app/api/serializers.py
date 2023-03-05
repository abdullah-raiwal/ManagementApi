from registrar_app.models import Application
from rest_framework import serializers


class ApplicationFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"


