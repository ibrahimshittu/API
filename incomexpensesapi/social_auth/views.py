from django.shortcuts import render
from rest_framework import generics, response, status
from .serializers import GoogleAuthViewSerializer


class GoogleAuthView(generics.GenericAPIView):

    serializer_class = GoogleAuthViewSerializer

    def post(self, request):
        serializer  = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data['auth_token']
        return response.Response(data, status.HTTP_201_CREATED)
