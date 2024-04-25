from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Patient, Sensor, Event
from .KGscripts.update_db import updatedb
import json
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login


@csrf_exempt
def dbupdater(request):
    try:
        heucod_json = request.read()
        data = json.loads(heucod_json)
        updatedb(data)
        return HttpResponse("POST success")
    except:    
        return HttpResponse("Her skal du POST")
    
def allEvents(request):
    try:
        data = Event.objects.all()
        
        serialized_data = [{'event_id': item.event_id, 
                            'sensor': item.sensor.sensor_id,
                            'patient': item.patient.patient_id} for item in data]
        return JsonResponse({'data': serialized_data})    
        
    except:
        return HttpResponse("SOMETHING'S BAD")
    
def someEvents(request):
    try:
        data = Event.objects.all()
        
        serialized_data = [{'event_id': item.event_id, 
                            'sensor': item.sensor.sensor_id,
                            'patient': item.patient.patient_id,
                            'event_type': item.event_type} for item in data]
        return JsonResponse({'data': serialized_data})    
        
    except:
        return HttpResponse("SOMETHING'S BAD")