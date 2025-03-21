from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
import random

User = get_user_model()

class RegisterAPI(APIView):
    permission_classes = [AllowAny]  # Allow access without authentication

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        otp = random.randint(100000, 999999)

        user = User.objects.create_user(email=email, password=password, username=email)
        user.otp = otp
        user.save()

        send_mail("OTP Verification", f"Your OTP is {otp}", "netravati1000@gmail.com", [email])

        return Response({"message": "OTP sent to email."}, status=201)

class VerifyOTPAPI(APIView):
    def post(self, request):
        email = request.data.get("email")
        otp = request.data.get("otp")

        user = User.objects.filter(email=email).first()
        if user and user.otp == otp:
            user.is_verified = True
            user.save()
            return Response({"message": "User verified successfully."})
        return Response({"error": "Invalid OTP"}, status=400)

from django.contrib.auth import authenticate


class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)
        if user and user.is_verified:
            response = Response({"message": "Login successful"})
            response.set_cookie("auth_token", user.get_session_auth_hash(), httponly=True)
            return response
        return Response({"error": "Invalid credentials"}, status=400)

class UserDetailsAPI(APIView):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"email": request.user.email, "username": request.user.username})

class LogoutAPI(APIView):
    def post(self, request):
        response = Response({"message": "Logged out successfully"})
        response.delete_cookie("auth_token")
        return response
