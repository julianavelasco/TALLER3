from ..models import Measurement

def get_measurements():
    measurements=Measurement.objects.all()
    return measurements

def get_measurement_by_id(identificacion):
    return Measurement.objects.get(id=identificacion)

def delete_measurement_by_id(identificacion):
    Measurement.objects.filter(id = identificacion).delete()

def change_measurement_by_id(identificacion, unidad):
    measurement=Measurement.objects.get(id=identificacion) 
    measurement.unit= unidad
    measurement.save()
    return measurement