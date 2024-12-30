from rest_framework import views, response, permissions, status

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
        pet_collection = services.get_user_pet(user=request.user)
        serializer = pet_serializer.PetSerializer(pet_collection, many=True)

        return response.Response(data=serializer.data)


class PetRetrieveUpdateDeleteApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pet_id):
        pet = services.get_user_pet_detail(pet_id=pet_id)

        serializer = pet_serializer.PetSerializer(pet)

        return response.Response(data=serializer.data)

    def delete(self, request, pet_id):
        services.delete_user_pet(user=request.user, pet_id=pet_id)
        return response.Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pet_id):
        serializer = pet_serializer.PetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pet = serializer.validated_data
        serializer.instance = services.update_user_pet(
            user=request.user, pet_id=pet_id, pet_data=pet
        )

        return response.Response(data=serializer.data)
