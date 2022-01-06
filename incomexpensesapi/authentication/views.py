from django.shortcuts import render
from rest_framework import generics, status, views
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .serializers import registerSerializer, emailVerificationSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .utils import Util
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import jwt

# Create your views here.


class registerView(generics.GenericAPIView):

    serializer_class = registerSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        model_user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(model_user).access_token

        current_site = get_current_site(request).domain
        relativeLink = reverse("verify-email")

        absurl = 'http://' + current_site + \
            relativeLink + "?token=" + str(token)

        email_body = "Hi, " + model_user.username + \
            " Use the link below to verify your email address: \n" + absurl

        data = {
            "to_email": model_user.email, "email_body": email_body, "email_subject": "Verify Your Account"
        }
        Util.send_mail(data)

        return Response({"details": user_data, "message": "chill!, check your email to activate your account"}, status=status.HTTP_200_OK)


class VerifyEmail(views.APIView):
    serializer_class = emailVerificationSerializer
    token_param_config = openapi.Parameter(
        "token", in_=openapi.IN_QUERY, type=openapi.TYPE_STRING, description="")

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')

        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms="HS256")
            user = User.objects.get(id=payload["user_id"])
            # print(user)

            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response("Congrats fam!, Email activated successfully", status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as e:
            return Response("Activation expired, refresh!", status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError as e:
            return Response({"Invalid Token, refresh!"}, status.HTTP_400_BAD_REQUEST)
