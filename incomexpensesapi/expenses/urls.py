from django.urls import path
from .views import ExpenseListAPIView, ExpenseDetailsAPIView

urlpatterns = [
    path('', ExpenseListAPIView.as_view(), name="expenses"),
    path('<int:id>/', ExpenseDetailsAPIView.as_view(), name="expense"),
]
