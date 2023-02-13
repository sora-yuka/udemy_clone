from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from application.accounts.views import (
    StudentRegisterAPIView, TeacherRegisterAPIView,
    ChangePasswordAPIView, MentorActivationAPIView, 
    StudentActivationAPIView, ForgotPasswordAPIView, SetNewPasswordAPIView
)

urlpatterns = [
    path("register/student/", StudentRegisterAPIView.as_view()),
    path("register/teacher/", TeacherRegisterAPIView.as_view()),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name="token_refrest"),
    path("change_password/", ChangePasswordAPIView.as_view()),
    path("confirm-mentor/<uuid:activation_code>/", MentorActivationAPIView.as_view()),
    path("confirm/<uuid:activation_code>/", StudentActivationAPIView.as_view()),
    path("forgot_password/", ForgotPasswordAPIView.as_view()),
    path("recovery/<uuid:activation_code>/", SetNewPasswordAPIView.as_view()),
]
