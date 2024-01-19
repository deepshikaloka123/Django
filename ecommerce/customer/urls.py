from django.urls import path
from . import views
urlpatterns = [
    path("customer/signup/",views.customersignup.as_view()),
    path("customer/login/",views.customerlogin.as_view()),
    path("getProfile/<username>/",views.getProfile.as_view()),
    path("updateProfile/",views.updateProfile.as_view()),
    path("deleteCustomer/<username>/",views.deleteCustomer.as_view()),
]