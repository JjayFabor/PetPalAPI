from rest_framework import views, response, exceptions, permissions
from . import serializer as user_serializer
from . import services


class RegisterApi(views.APIView):

    def post(self, request):
        serializer = user_serializer.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        data = serializer.validated_data
        serializer.instance = services.create_user(user_dc=data)

        print(data)

        return response.Response(data=serializer.data)
