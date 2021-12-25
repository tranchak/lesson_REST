from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Prezent


class PrezentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Prezent
        fields='__all__'

class SerializerPrezent(serializers.Serializer):
    name=serializers.CharField()
    price=serializers.DecimalField(max_digits=8, decimal_places=2)
    description=serializers.CharField()
    # created=serializers.DateTimeField()

    def create(self, validated_data):
        return Prezent.objects.create(**validated_data)






class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']