from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Income
from .serializers import IncomeSerializer
from .permissions import IsOwner
from rest_framework import permissions


class IncomeListAPIView(ListCreateAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner, )
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
