from rest_framework import serializers
from django.contrib.auth.models import User
from PustakaIntake.serializer import DynamicFieldsModelSerializer
from django.contrib.auth.password_validation import validate_password as pustaka_validate_password


class UserRegisterSerializer(DynamicFieldsModelSerializer):
    repeat_password = serializers.CharField(max_length=128, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password', 'repeat_password']
        extra_kwargs = {'password': {
            'write_only': True,
            'required': True
        },
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            }

        }

    @staticmethod
    def validate_password(password):
        pustaka_validate_password(password)
        return password

    def validate(self, attrs):
        if attrs['password'] != attrs['repeat_password']:
            raise serializers.ValidationError({'repeat_password': 'Does not match with password'})
        return attrs

    def create(self, validated_data):
        _ = validated_data.pop('repeat_password')
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user
