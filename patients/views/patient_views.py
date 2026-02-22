from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..models import Patient

@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patients/list.html', {'patients': patients})

@login_required
def patient_create(request):
    if request.method == "POST":
        Patient.objects.create(
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            age=request.POST.get('age'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone')
        )
        return redirect('patient_list')
        
    return render(request, 'patients/create.html')

@login_required
def patient_update(request, id):
    patient = get_object_or_404(Patient, id=id)
    
    if request.method == "POST":
        patient.first_name = request.POST.get('first_name')
        patient.last_name = request.POST.get('last_name')
        patient.age = request.POST.get('age')
        patient.email = request.POST.get('email')
        patient.phone = request.POST.get('phone')
        patient.save()
        return redirect('patient_list')
        
    return render(request, 'patients/update.html', {'patient': patient})

@login_required
def patient_delete(request, id):
    patient = get_object_or_404(Patient, id=id)
    patient.delete()
    return redirect('patient_list')
