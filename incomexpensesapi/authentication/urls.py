from django.urls import path
from .views import registerView, VerifyEmail

urlpatterns = [
    path('register/', registerView.as_view(), name="register"),
    path('verify-email/', VerifyEmail.as_view(), name="verify-email"),
]
