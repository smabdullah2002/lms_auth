from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TeacherModel
from django.contrib.auth.hashers import make_password, check_password

class TeacherRegistrationView(APIView):
    def post(self, request):
        phone_number= request.data.get("phone_number")
        full_name= request.data.get("full_name")
        profile_picture= request.data.get("profile_picture")
        gender= request.data.get("gender")
        website= request.data.get("website")
        password= make_password(request.data.get("password"))

        TeacherModel.objects.create(
            phone_number=phone_number,
            full_name=full_name,
            profile_picture=profile_picture,
            gender=gender,
            website=website,
            password=password
        )
        
        return Response(
            {"message": "Teacher registered successfully"},
            status=status.HTTP_201_CREATED
        )


class TeacherLoginView(APIView):
    def post(self, request):
        phone_number= request.data.get("phone_number")
        password= request.data.get("password")
        try:
            teacher=TeacherModel.objects.filter(phone_number=phone_number).last()
            if teacher and check_password(password, teacher.password):
                return Response(
                    {"message": "Login successful"},
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Invalid phone number or password"},
                    status=status.HTTP_400_BAD_REQUEST
                )
        except TeacherModel.DoesNotExist:
            return Response(
                {"message": "Teacher not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        
