from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from account.serializers import EmployeeRegisterSerializer, RestaurantRegisterSerializer, EmployeeSerializer, \
    RestaurantSerializer, RestaurantLoginSerializer, EmployeeLoginSerializer


class RegisterEmployeeAPI(GenericAPIView):
    serializer_class = EmployeeRegisterSerializer
    print(f"SERIALISER = {serializer_class}")

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        employee = serializer.save()
        employee_data = EmployeeSerializer(employee, context=self.get_serializer_context()).data

        return Response({
            "employee": employee_data,
            "username": employee.user.username
        })


class RegisterRestaurantAPI(GenericAPIView):
    serializer_class = RestaurantRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.save()
        company_data = RestaurantSerializer(company, context=self.get_serializer_context()).data
        return Response({
            "company": company_data,
            "username": company.user.username
        })


class LoginRestaurantAPI(GenericAPIView):
    serializer_class = RestaurantLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.validated_data
        company_data = RestaurantSerializer(company, context=self.get_serializer_context()).data
        return Response({
            "company": company_data,
            "username": company.user.username
        })


class LoginEmployeeAPI(GenericAPIView):
    serializer_class = EmployeeLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        company = serializer.validated_data
        company_data = EmployeeSerializer(company, context=self.get_serializer_context()).data
        return Response({
            "company": company_data,
            "username": company.user.username
        })
