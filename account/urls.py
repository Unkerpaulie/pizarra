from django.urls import path
from . import views

app_name = "account"


urlpatterns = [
    path('signup/', views.account_signup, name="signup"),
    path('login/', views.account_login, name="login"),
]
