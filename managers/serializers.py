from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.contrib.auth.models import User
from managers.models import Manager


class ManagerLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, max_length=50)


class UserRegisterSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=50)
    password = serializers.CharField(min_length=4, max_length=50)
    confirm_password = serializers.CharField(min_length=4, max_length=50)
    email = serializers.EmailField()
    phone = serializers.CharField(min_length=1, max_length=50)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError("Username already exists")

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise ValidationError("Passwords don't match")
        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email',]


class ManagerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Manager
        fields = ('id', 'user', 'phone')

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user


        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        user.save()

        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        return instance
