from .views import FlightViewSet , PassengerViewSet , ReservationViewSet
from django.urls import path,include

# urlpatterns = [
#     path('flight/',FlightViewSet.as_view, name='flight'),
#     path('passenger/',PassengerViewSet.as_view,name='passenger' ),
#     path('reservation/',ReservationViewSet,name='reservation'),
# ]


from rest_framework import routers
router = routers.DefaultRouter()
router.register('flight', FlightViewSet)
router.register('passenger', PassengerViewSet)
router.register('reservation', ReservationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]