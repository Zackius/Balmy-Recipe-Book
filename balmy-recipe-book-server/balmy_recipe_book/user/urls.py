from . import views
from django.urls import path 


urlpatterns =[
    path("user/register", views.RegisterNewUser.as_view(), name="register user")
    
]