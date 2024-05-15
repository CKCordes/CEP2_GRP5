from django.http import HttpResponse, JsonResponse
from .models import Patient, Event
from .KGscripts.update_db import updatedb
import json
from django.views.decorators.csrf import csrf_exempt
from .KGscripts.scripts import *



@csrf_exempt
def dbupdater(request):
    try:
        heucod_json = request.read()
        data = json.loads(heucod_json)
        updatedb(data)
        return JsonResponse({"message": "Database updated successfully"})
    except Exception as e:
        return JsonResponse({"error": f"An error occurred: {e}"})
    
def allEvents(request):
    try:
        patient_id = request.GET.get('patient_id')
                
        if patient_id:
            patient = Patient.objects.get(patient_id = patient_id)
            events = Event.objects.filter(patient = patient)

        else:
            events = Event.objects.none()
        
        serialized_data = serializeData(events)
        return JsonResponse({'data': serialized_data})    
        
    except Exception as e:
        return JsonResponse({"Error" : f"Error occured: {e}"})
    
def cookingEvents(request):
    try:
        patient_id = request.GET.get('patient_id')
                
        if patient_id:
            patient = Patient.objects.get(patient_id = patient_id)
            cookingEvents = Event.objects.filter(event_type_enum = 82136, patient = patient)
            trackingEvents = Event.objects.filter(event_type_enum = 82099, patient=patient).only(sensor__sensor_location = 'kitchen')
        else:
            cookingEvents = Event.objects.none()
        # 82136 enum is CookingDeviceUsage - CookingDeviceUsage is the
        
        # Cleaning cooking events 
        
        comprisedCookingEvents = getCookingEvents(cookingEvents)
        serialized_data = serializeData(comprisedCookingEvents)
        return JsonResponse({'data': serialized_data})    
        
    except Exception as e:
        return JsonResponse({"Error" : f"Error occured: {e}"})
    
def awayTime(request):
    patient_id = request.GET.get('patient_id')
                
    if patient_id:
        patient = Patient.objects.get(patient_id = patient_id)
        #Away time is when a sensor posts an occupied event while stove is on
        # Meaning we should compare a cooking event list with a away time list
        cookingEvents = Event.objects.filter(event_type_enum = 82136, patient = patient)
        
        # 'filter' gets all tracking events, 'exclude' removes all tracking events from the kitchen
        trackingEvents = Event.objects.filter(event_type_enum = 82099, patient=patient).exclude(sensor__sensor_location = 'kitchen')
    else:
        cookingEvents = Event.objects.none()
        trackingEvents = Event.objects.none()
    
    try:

        comprisedCookingEvents = getCookingEvents(cookingEvents)
        comprisedTrackingEvents = getTrackingEvents(trackingEvents)

        overlappingEvents = getOverlapingEvents(comprisedCookingEvents, comprisedTrackingEvents)
 
        serialized_data = serializeData(overlappingEvents)
        return JsonResponse({'data': serialized_data}) 

    except Exception as e:
        return JsonResponse({"Error" : f"Error occured: {e}"}) 