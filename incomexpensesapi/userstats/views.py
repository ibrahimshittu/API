from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expenses.models import Expense
from income.models import Income
from rest_framework import status, response
# Create your views here.


class ExpenseSummaryStats(APIView):
    def get_categories(self, expense):
        return expense.category

    def get_amount_per_category(self, expenses_list, categories):
        expenses = expenses_list.filter(category=categories)

        amount = 0

        for expense in expenses:
            amount += expense.amount
        return {'amount': str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        last_year = today_date - datetime.timedelta(days=365)

        expenses = Expense.objects.filter(
            owner=request.user, date__gte=last_year, date__lte=today_date)

        categories = list(set(map(self.get_categories, expenses)))

        data = {}

        for expense in expenses:
            for category in categories:
                data[category] = self.get_amount_per_category(
                    expenses, category)

        return response.Response({'category_data': data}, status.HTTP_200_OK)


class IncomeSummaryStats(APIView):
    def get_categories(self, income):
        return income.source

    def get_amount_per_source(self, incomes_list, sources):
        incomes = incomes_list.filter(source=sources)

        amount = 0

        for income in incomes:
            amount += income.amount
        return {'amount': str(amount)}

    def get(self, request):
        today_date = datetime.date.today()
        last_year = today_date - datetime.timedelta(days=365)

        incomes = Income.objects.filter(
            owner=request.user, date__gte=last_year, date__lte=today_date)

        sources = list(set(map(self.get_categories, incomes)))

        data = {}

        for income in incomes:
            for source in sources:
                data[source] = self.get_amount_per_source(
                    incomes, source)

        return response.Response({'income_source_data': data}, status.HTTP_200_OK)
