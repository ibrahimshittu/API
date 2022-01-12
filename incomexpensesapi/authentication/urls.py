from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import registerView, LogoutView, VerifyEmail, loginview, PasswordTokenCheckAPIView, RequestPasswordReset, SetNewPassword

urlpatterns = [
    path('register/', registerView.as_view(), name="register"),
    path('login/', loginview.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('verify-email/', VerifyEmail.as_view(), name="verify-email"),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-password-reset-email/',
         RequestPasswordReset.as_view(), name='request-password-reset'),
    path('password-reset-check/<uidb64>/<token>',
         PasswordTokenCheckAPIView.as_view(), name='password_reset_check'),
    path('reset-password/',
         SetNewPassword.as_view(), name='reset_password'),
]
