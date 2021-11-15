from .models import Flight , Passenger , Reservation
from .serializers import FlightSerializer , PassengerSerializer , ReservationSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


class FlightViewSet(ModelViewSet):
  queryset = Flight.objects.all()
  serializer_class = FlightSerializer
#   permissions_class = [IsAuthenticated]
#   authentication_classes = (TokenAuthentication,)

class PassengerViewSet(ModelViewSet):
  queryset = Passenger.objects.all()
  serializer_class =PassengerSerializer

class ReservationViewSet(ModelViewSet):
  queryset = Reservation.objects.all()
  serializer_class = ReservationSerializer