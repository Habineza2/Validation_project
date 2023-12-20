from datetime import date
from django import forms
from .models import Participant,Vehicle
from django.forms import inlineformset_factory
class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'make',
            'model',
            'color',
            'plate_number',
            'manufacture_date',
        ]
        widgets = {
            'manufacture_date': forms.DateInput(attrs={'type': 'date'}),
        }
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = [
            'date_of_birth',
            'first_name',
            'last_name',
            'middle_name',
            'email',
            'phone_number',
            'reference_number',
            'gender',   

        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if 'ur.ac.rw' not in email:
            raise forms.ValidationError("Email must contain UR (ur.ac.rw)")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.startswith('+'):
            raise forms.ValidationError("Phone number must start with + country code")
        return phone_number

    def clean_reference_number(self):
        reference_number = self.cleaned_data.get('reference_number')
        if not 99 <= reference_number <= 999:
            raise forms.ValidationError("Reference number must be between 99 and 999")
        return reference_number

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        if age < 18:
            raise forms.ValidationError("Participants must be 18 years or older.")
        return date_of_birth
    

VehicleFormSet = inlineformset_factory(
    Participant,
    Vehicle,
    form=VehicleForm,
    extra=1,)









