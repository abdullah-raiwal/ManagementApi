from accounts_app.api.serializers import RegistrarRegisterSerializer, RegistrarLoginSerializer
from dj_rest_auth.registration.views import RegisterView, LoginView

class RegistrarRegisterView(RegisterView):
    serializer_class = RegistrarRegisterSerializer

class RegistrarLoginView(LoginView):
    serializer_class = RegistrarLoginSerializer

