from rest_framework import serializers
from user import serializer as user_serializer
from . import services


class PetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    species = serializers.CharField()
    breed = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    medical_condition = serializers.CharField()
    user = user_serializer.UserSerializer(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.PetDataClass(**data)
