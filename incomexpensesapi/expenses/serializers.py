from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(
    #     required=True, max_length=68, min_length=6)
    # amount = serializers.CharField(
    #     required=True, max_length=68, min_length=6)
    # description = serializers.TextField()
    # date = serializers.DateField()

    class Meta:
        model = Expense
        fields = ['category', 'amount', 'description', 'date']
