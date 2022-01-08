from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsOwner
from rest_framework import permissions


class ExpenseListAPIView(ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class ExpenseDetailsAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner, )
    lookup_field = "id"

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)
