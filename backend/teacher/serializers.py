from rest_framework import serializers
from _applib.model_choices_field import GenderChoice


class TeacherRegistrationSerializer(serializers.Serializer):
    phone_number= serializers.RegexField(
        max_length=14,
        regex=r'^(?:\+88|88)?01[3-9]\d{8}$',
        error_messages={
            'invalid': 'Invalid phone number format'
        }
    )
    full_name= serializers.CharField(max_length=100)
    profile_picture=serializers.CharField(max_length=300)
    gender= serializers.ChoiceField(
        choices=GenderChoice.choices,
        error_messages={
            'invalid': 'Invalid gender'
        }
    )
    password=serializers.CharField(max_length=20)
    
    