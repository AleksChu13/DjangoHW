from django.urls import path
from measurement.views import SensorUpdate, MeasurementCreate, SensorsViewCreate
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsViewCreate.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', MeasurementCreate.as_view())
]