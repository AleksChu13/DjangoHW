# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    CreateAPIView,
)
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementCreateSerializer


class SensorsViewCreate(ListCreateAPIView):


    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):


    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(CreateAPIView):


    serializer_class = MeasurementCreateSerializer