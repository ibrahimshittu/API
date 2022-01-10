from django.urls import path
from .views import ExpenseSummaryStats, IncomeSummaryStats

urlpatterns = [
    path('expense-summary/', ExpenseSummaryStats.as_view(), name="expense-summary"),
    path('income-summary/', IncomeSummaryStats.as_view(), name="income-summary"),

]
