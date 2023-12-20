from django.shortcuts import redirect, render
from django.forms import formset_factory

from validationApp.models import Participant, Vehicle
from .forms import ParticipantForm, VehicleForm



def participant_form_view(request):
    VehicleFormSet = formset_factory(VehicleForm, extra=1, can_delete=True)

    if request.method == 'POST':
        participant_form = ParticipantForm(request.POST)
        vehicle_formset = VehicleFormSet(request.POST, prefix='vehicles')

        if participant_form.is_valid() and vehicle_formset.is_valid():
            participant = participant_form.save()
            for form in vehicle_formset:
                if not form.cleaned_data.get('DELETE', False):
                    vehicle = form.save(commit=False)
                    vehicle.participant = participant
                    vehicle.save()

            # Redirect to a success page
            return redirect('success')
    else:
        participant_form = ParticipantForm()
        vehicle_formset = VehicleFormSet(prefix='vehicles')

    return render(request, 'participant_create.html', {'participant_form': participant_form, 'vehicle_formset': vehicle_formset})

def success(request):
    return render(request, 'success.html')

def vehicle_registration(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform any other necessary actions
            form.save()
            # Redirect to a success page or another view
            return redirect('success_page')
    else:
        form = VehicleForm()

    return render(request, 'vehicle_form.html', {'form': form})




import logging

logger = logging.getLogger(__name__)

def your_function():
    # your code here
    logger.info('Your log message')







from django.http import HttpResponse
from django.shortcuts import render

def dynamic_view(request, operation, a, b):
    if operation == 'add':
        result = int(a) + int(b)
    elif operation == 'subtract':
        result = int(a) - int(b)
    else:
        result = 'Invalid operation'

    return render(request, 'result.html', {'result': result})    
    