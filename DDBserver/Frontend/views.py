from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from KitchenGuardServer.models import Patient

def index(request):
    patients = Patient.objects.all()
        
    return render(request, "index.html", {'patients': patients})

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
