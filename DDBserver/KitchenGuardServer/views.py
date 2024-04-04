from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient

def index(request):
    patient_list = Patient.objects.order_by("-patient_id")[:5]
    output = ", ".join([q.patient_id for q in patient_list])
    return HttpResponse(output)

def login(request):
    return HttpResponse("You need to login")