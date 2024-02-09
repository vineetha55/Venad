from django.urls import path
from . import views

urlpatterns=[
    path("",views.login_page,name="login_page"),
    path("login_check/",views.login_check,name="login_check")
]