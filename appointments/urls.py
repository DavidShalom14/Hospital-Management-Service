from django.urls import path
from .views import appointment_list, add_appointment, complete_appointment, add_appointment_api

urlpatterns = [
    path('', appointment_list),
    path('add/', add_appointment),
    path('complete/<int:id>/', complete_appointment),
    path('api/add/', add_appointment_api),
]
