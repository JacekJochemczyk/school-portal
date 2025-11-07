from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class PortalTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Własny serializer JWT:
    - dodaje dane użytkownika do odpowiedzi
    - blokuje logowanie szkoły, jeśli nie została zatwierdzona
    """
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user

        # Blokada logowania dla szkół bez akceptacji
        if getattr(user, "user_type", None) == "school" and not getattr(user, "is_approved", False):
            raise AuthenticationFailed(
                "Konto szkoły oczekuje na akceptację administratora.", code="not_approved"
            )

        # Zwracamy dodatkowe informacje o użytkowniku
        data["user"] = {
            "id": user.id,
            "username": user.username,
            "user_type": getattr(user, "user_type", None),
            "is_approved": getattr(user, "is_approved", None),
        }

        return data


class PortalTokenObtainPairView(TokenObtainPairView):
    serializer_class = PortalTokenObtainPairSerializer
