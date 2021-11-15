from rest_framework import serializers
from .models import Flight , Passenger , Reservation
from django.contrib.auth.models import User
# from rest_framework.authtoken.views import Token

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        # fields = ['flightNumber' , 'operatingAirlines' , 'departureCity']
        fields = ('flightNumber' , 'operatingAirlines' , 'departureCity')
        
class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = ('firstName', 'lastName', 'email', 'phone')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('flight', 'passenger', 'user')

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username', 'password']
#   # password görünmesin diye
#         extra_kwargs = {
#             'password':{
#                'write_only':True,
#                'required' : True
#         } 
#     def create(self,validated_data):
#         user = User.objects.create_user(**validated_data)
#         Token.objects.create(user=user)
#         return user
      
