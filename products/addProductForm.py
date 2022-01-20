from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput
from django import forms
from .models import Carton


class AddCartonAndProductForm(forms.ModelForm):
    class Meta:
        model = Carton
        fields = ['carton_id','product_quantity','production_date','expiry_date']
        widgets = {
            'production_date':DatePickerInput(format='%d-%m-%Y'),
            'expiry_date':DatePickerInput(format='%d-%m-%Y'),
        }