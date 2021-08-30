from django.urls import path
from . import views 

urlpatterns=[
    path('list/', views.get_all_measurements, name='measurementList'),
    path('see/<int:identificacion>/', views.get_measurement, name='get_measurement_id'),
    path('delete/<int:identificacion>/', views.delete_measurement, name='delete_measurement_id'),
    path('change/<int:identificacion>/<str:unidad>', views.change_measurement, name='change_measurement_id')
]