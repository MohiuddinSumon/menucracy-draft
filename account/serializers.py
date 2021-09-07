from rest_framework import serializers
from .models import User, Employee, Restaurant
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'is_employee', 'is_restaurant')
        extra_kwargs = {'password': {'write_only': True}}


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('user', 'email_address')


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('user', 'email_address', 'restaurant_name')


class EmployeeRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Employee
        fields = ('user', 'email_address')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data['user']['username'], validated_data['email_address'],
                                        validated_data['user']['password'])
        employee = Employee.objects.create(user=user, email_address=validated_data.pop('email_address'))
        return employee


class RestaurantRegisterSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)

    class Meta:
        model = Restaurant
        fields = ('user', 'restaurant_name', 'email_address')
        extra_kwargs = {'password': {'write_only': True}, 'username': {'write_only': True}}

    def create(self, validated_data, *args, **kwargs):
        user = User.objects.create_user(validated_data['user']['username'], validated_data['email_address'],
                                        validated_data['user']['password'])
        restaurant = Restaurant.objects.create(user=user, email_address=validated_data.pop('email_address'),
                                               restaurant_name=validated_data.pop('restaurant_name'))
        return restaurant


class EmployeeLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        employee = authenticate(**data)
        if employee and employee.is_active:
            return employee
        raise serializers.ValidationError("Incorrect Credentials")

    class Meta:
        fields = ['username', 'password', 'is_employee', 'is_company']
        extra_kwargs = {'is_employee': {'required': False},
                        'is_company': {'required': False}}


class RestaurantLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        employee = authenticate(**data)
        if employee and employee.is_active:
            return employee
        raise serializers.ValidationError("Incorrect Credentials")

    class Meta:
        fields = ['username', 'password', 'is_employee', 'is_company']
        extra_kwargs = {'is_employee': {'required': False},
                        'is_company': {'required': False}}
