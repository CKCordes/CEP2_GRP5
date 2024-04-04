from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from .KGscripts.update_db import updatedb
import json

def index(request):
    patient_list = Patient.objects.order_by("-patient_id")[:5]
    output = ", ".join([q.patient_id for q in patient_list])
    return HttpResponse(output)

def login(request):
    return HttpResponse("You need to login")

def dbupdater(request):
    heucod_json = request.read()
    data = json.loads(heucod_json)
    updatedb(data)
    return
