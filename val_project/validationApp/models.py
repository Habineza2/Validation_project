from django.db import models

from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

from django.db import models






def validate_date_of_birth(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(_("Participants must be 18 years or older."))

class Participant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    

   

    def validate_phone_number(value):
      if not value.startswith('+250'):
        raise ValidationError(_('Phone number should start with +250'))

    date_of_birth = models.DateField(validators=[validate_date_of_birth])
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(validators=[
        RegexValidator(regex=r'.*ur\.ac\.rw.*', message="Email must contain UR (ur.ac.rw)")
    ])
    phone_number = models.CharField(max_length=15, validators=[validate_phone_number])
    
    reference_number = models.IntegerField(validators=[RegexValidator(regex=r'^[1-9]\d{1,2}$', message="Reference number must be between 99 and 999")])
    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    





class Vehicle(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        
    ]

    COLOR_CHOICES = [
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Green', 'Green'),
        
    ]
    
    def validate_date_of_vehicles(value):
      today = date.today()
      age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
      if age > 23:
        raise ValidationError(_("vehicle must be made no letter ."))
    def validate_plate_number(value):
      valid_prefixes = ['RAA', 'RAB', 'RAC', 'RAD', 'RAE', 'RAF', 'RAG', 'RAH',
        'RNP', 'RDF', 'IT', 'GR', 'CD']
      if value and not any(value.startswith(prefix) for prefix in valid_prefixes):
        raise ValidationError('Invalid plate number.')
      
    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    model = models.CharField(max_length=50)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    plate_number = models.CharField(max_length=7, validators=[validate_plate_number],default="")  
    manufacture_date = models.DateField(validators=[validate_date_of_vehicles])
    Participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, null=True, blank=True)

    def clean(self):
        if self.make == 'Car' and self.manufacture_date <= date(2000, 1, 1):
            raise ValidationError("Car manufacture date should be after 01/01/2000")

    def __str__(self):
        return f"{self.make} {self.model} ({self.plate_number})"
    







from django.contrib.auth.models import User
from django.db import models

class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)




from django.db import models

class DynamicModel(models.Model):
    operation = models.CharField(max_length=10)

    def perform_operation(self, a, b):
        if self.operation == 'add':
            result = a + b
        elif self.operation == 'subtract':
            result = a - b
        else:
            result = 'Invalid operation'

        return result

