from django.urls import path
from .views import UserStats

urlpatterns = [
    path('expense-summary/', UserStats.as_view(), name="expense-summary"),

]
