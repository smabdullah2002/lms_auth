from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TeacherModel
from django.contrib.auth.hashers import make_password, check_password
from .serializers import TeacherRegistrationSerializer
import requests


class TeacherRegistrationView(APIView):
    
    ######function to send OTP to another service(exaple of microservice)
    def send_otp(self, phone_number):
        url = "http://127.0.0.1:8001/otp/send/"
        payload = {
            "otp_for": "sms",
            "identifier": phone_number,
            "reason": "registration"
            }

        otp_script= requests.post(
            url="http://127.0.0.1:8001/otp/send/",
            data=payload
        )
        print("message====>>>>", otp_script.status_code)

    
    def post(self, request):
        user_provided_data= request.data
        register_serializer=TeacherRegistrationSerializer(data= user_provided_data)
        # print("=============", register_serializer.initial_data.get("phone_number")[-11:])
        if TeacherModel.objects.filter(phone_number=register_serializer.initial_data.get("phone_number")[-11:]).exists():
            return Response(
                {"message": "Phone number already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if register_serializer.is_valid():
            TeacherModel.objects.create(
            phone_number=register_serializer.validated_data.get("phone_number")[-11:],
            full_name=register_serializer.validated_data.get("full_name"),
            profile_picture=register_serializer.validated_data.get("profile_picture"),
            gender=register_serializer.validated_data.get("gender"),
            # website=register_serializer.validated_data.get("full_name"),,
            password=make_password(register_serializer.validated_data.get("password")),
            )
            self.send_otp(register_serializer.validated_data.get("phone_number")[-11:])
            
            return Response(
                {"message": "Registration successful"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {"message": "Invalid data",
                "errors": register_serializer.errors},   
            )
        

        
        ########## not using serializer ##########
        # phone_number= request.data.get("phone_number")
        # full_name= request.data.get("full_name")
        # profile_picture= request.data.get("profile_picture")
        # gender= request.data.get("gender")
        # website= request.data.get("website")
        # password= make_password(request.data.get("password"))


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
        
        
