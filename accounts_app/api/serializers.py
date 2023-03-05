from rest_framework import serializers
from accounts_app.models import Registrar
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer


class RegistrarRegisterSerializer(RegisterSerializer):

    registrar = serializers.PrimaryKeyRelatedField(read_only=True)
    about = serializers.CharField(required=True)

    def save(self, request):
        user = super(RegistrarRegisterSerializer, self).save(request)
        user.is_registrar = True
        user.save()

        registrar = Registrar(
            registrar=user, about=self.cleaned_data.get('about'))
        registrar.save()

        return user


class RegistrarLoginSerializer(LoginSerializer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('email')

    class Meta:
        model = Registrar
        fields = ['username', 'password']

