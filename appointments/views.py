from django.shortcuts import render, redirect
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth.decorators import login_required

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments_list.html', {
        'appointments': appointments
    })

def add_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']
        date = request.POST['date']

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            status='Scheduled'
        )
        return redirect('/appointments/')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'add_appointment.html', {
        'patients': patients,
        'doctors': doctors
    })

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments_list.html', {
        'appointments': appointments
    })


@login_required
def add_appointment(request):
    if request.method == 'POST':
        patient_id = request.POST['patient']
        doctor_id = request.POST['doctor']
        date = request.POST['date']

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            status='Scheduled'
        )
        return redirect('/appointments/')

    patients = Patient.objects.all()
    doctors = Doctor.objects.all()

    return render(request, 'add_appointment.html', {
        'patients': patients,
        'doctors': doctors
    })

@login_required
def complete_appointment(request, id):
    appointment = Appointment.objects.get(id=id)
    appointment.status = 'Completed'
    appointment.save()
    return redirect('/appointments/')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def add_appointment_api(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient')
        doctor_id = request.POST.get('doctor')
        date = request.POST.get('date')

        Appointment.objects.create(
            patient_id=patient_id,
            doctor_id=doctor_id,
            date=date,
            status='Scheduled'
        )

        return JsonResponse({
            'message': 'Appointment created successfully'
        })
