from django.shortcuts import render, redirect
from .models import User
from travel_app.models import Trips
from django.contrib import messages
import bcrypt

# Create your views here.
def home(request):

    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        errors=User.objects.validator(request.POST)
        if len(errors)>0:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/')
        
        pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user=User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash
        )
        request.session['user_id'] = new_user.id
        return redirect('/dashboard')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'])
        if user:
            if bcrypt.checkpw(request.POST['password'].encode(), user[0].password.encode()):
                request.session['user_id']=user[0].id
                return redirect('/dashboard')
            else:
                messages.error(request, "Incorrect email/password match")
    return redirect('/')



def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'trips':Trips.objects.all(),
        'trip':Trips.objects.get
    }
    return render(request, 'dashboard.html', context)

