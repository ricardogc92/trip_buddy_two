from django.shortcuts import render, redirect
from .models import User, Trips
from django.contrib import messages

# Create your views here.
def new(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context={
        'user':User.objects.get(id=request.session['user_id'])
    }
    return render(request,'create_trip.html', context)

def create(request):
    if request.method=='POST':
        errors=Trips.objects.validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect('/trips/new')
        user=User.objects.get(id=request.session['user_id'])
        new_trip=Trips.objects.create(
            destination=request.POST['destination'],
            start_date=request.POST['start_date'],
            end_date=request.POST['end_date'],
            plan=request.POST['plan'],
            owner=user
        )
    return redirect('/dashboard')

def delete(request, trip_id):
    trip=Trips.objects.get(id=trip_id)
    trip.delete()
    return redirect('/dashboard')

def edit(request, trip_id):
    context={
        'user':User.objects.get(id=request.session['user_id']),
        'trip':Trips.objects.get(id=trip_id),
    }
    return render(request, 'edit.html', context)

def update(request, trip_id):
    if request.method=='POST':
        errors=Trips.objects.validator(request.POST)
        if errors:
            for value in errors.values():
                messages.error(request, value)
            return redirect(f'/trips/edit/{trip_id}')
        trip=Trips.objects.get(id=trip_id)
        trip.destination=request.POST['destination']
        trip.start_date=request.POST['start_date']
        trip.end_date=request.POST['end_date']
        trip.plan=request.POST['plan']
        trip.save()
    return redirect('/dashboard')

def join(request, trip_id):
    user=User.objects.get(id=request.session['user_id'])
    trip=Trips.objects.get(id=trip_id)
    trip.users_joined.add(user)
    return redirect('/dashboard')

def show(request, trip_id):
    context={
        'user': User.objects.get(id=request.session['user_id']),
        'trip': Trips.objects.get(id=trip_id)
    }
    return render(request,'show.html',context)

def cancel(request, trip_id):
    user=User.objects.get(id=request.session['user_id'])
    trip=Trips.objects.get(id=trip_id)
    trip.users_joined.remove(user)
    return redirect('/dashboard')
