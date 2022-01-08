from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import registerView, VerifyEmail, loginview

urlpatterns = [
    path('register/', registerView.as_view(), name="register"),
    path('login/', loginview.as_view(), name="login"),
    path('verify-email/', VerifyEmail.as_view(), name="verify-email"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
