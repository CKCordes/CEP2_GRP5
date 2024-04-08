from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from .KGscripts.update_db import updatedb
import json
from django.views.decorators.csrf import csrf_exempt

def index(request):
    patient_list = Patient.objects.order_by("-patient_id")[:5]
    output = ", ".join([q.patient_id for q in patient_list])
    return HttpResponse(output)

def login(request):
    return HttpResponse("You need to login")

@csrf_exempt
def dbupdater(request):
    try:
        heucod_json = request.read()
        print(heucod_json)
        data = json.loads(heucod_json)
        updatedb(data)
        return HttpResponse("POST success")
    except:    
        return HttpResponse("Her skal du POST")