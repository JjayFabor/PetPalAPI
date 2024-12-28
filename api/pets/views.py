from rest_framework import views, response, permissions

from user import authentication
from . import serializer as pet_serializer
from . import services


class PetCreateListApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = pet_serializer.PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data

        # Add or create pet
        serializer.instance = services.create_pet(user=request.user, pet_dc=data)

        return response.Response(data=serializer.data)

    def get(self, request):
        return response.Response(data="hello")
