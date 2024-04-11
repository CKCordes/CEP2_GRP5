from django.shortcuts import render
from django.http import HttpResponse
from .models import Patient
from .KGscripts.update_db import updatedb
import json
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login

def index(request):
    patient_list = Patient.objects.order_by("-patient_id")[:5]
    output = ", ".join([q.patient_id for q in patient_list])
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('/index')  
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

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