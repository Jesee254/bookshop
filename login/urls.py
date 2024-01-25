from django.urls import path
from . import views

app_name="login"
urlpatterns=[
    path("register/",views.register, name="register"),
    path("", views.login_user, name="login"),
    path('home/',views.signout,name="signout"),
]