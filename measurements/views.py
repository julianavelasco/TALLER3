from django.shortcuts import render
from .logic.logic_measurements import change_measurement_by_id, delete_measurement_by_id, get_measurements
from .logic.logic_measurements import get_measurement_by_id
from django.http import HttpResponse
from django.core import serializers

def get_all_measurements(request):
    measurements=get_measurements()
    measurement_list=serializers.serialize('json', measurements)
    return HttpResponse(measurement_list, content_type='application/json')
    
def get_measurement(request, identificacion):
    measurement=get_measurement_by_id(identificacion)
    measurement_id = serializers.serialize('json', [measurement])
    return HttpResponse(measurement_id, content_type='application/json')

def delete_measurement(request, identificacion):
    delete_measurement_by_id(identificacion)
    measurement_list=serializers.serialize("json", get_measurements())
    return HttpResponse(measurement_list,content_type="application/json")
    
def change_measurement(request, identificacion, unidad):
    measurement_change=serializers.serialize("json", [change_measurement_by_id(identificacion, unidad)])
    return HttpResponse(measurement_change,content_type="application/json")
    