from accounts_app.api.serializers import RegistrarRegisterSerializer, RegistrarLoginSerializer
from dj_rest_auth.registration.views import RegisterView, LoginView
from rest_framework_simplejwt.tokens import RefreshToken


class RegistrarRegisterView(RegisterView):
    serializer_class = RegistrarRegisterSerializer


class RegistrarLoginView(LoginView):
    serializer_class = RegistrarLoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        if response.status_code == 200:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            refresh = RefreshToken.for_user(user)

            data = {
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                'user': serializer.data,
            }

            response.data = data

        return response
