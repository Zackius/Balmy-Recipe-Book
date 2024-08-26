from django.shortcuts import render
from rest_framework import response, status
from rest_framework.generics import (
    GenericAPIView
)


# Create your views here.

class RegisterNewUser(GenericAPIView):
    "A class to register a new user to the system"
    
    def post(self, request):
        try:
            incoming_data = request.data
            print(incoming_data, "DJJJJJJJJJJJJJJJJJJ")

        except Exception as e:
            return response.Response(
                {"msg": f"An error occurred creating a single admin {e}"},
                status=status.HTTP_400_BAD_REQUEST,
            )     

