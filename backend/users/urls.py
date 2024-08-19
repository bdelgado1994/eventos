from users.views import RegisterView, CustomTokenObtainPairView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", CustomTokenObtainPairView.as_view(), name="login")
]
