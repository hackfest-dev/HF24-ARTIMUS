# forms.py

from django import forms
from .models import VehicleMaintenance

class VehicleMaintenanceForm(forms.ModelForm):
    class Meta:
        model = VehicleMaintenance
        fields = ['vehicle_number', 'maintenance_date', 'maintenance_type', 'description']
