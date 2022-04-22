from django import forms
import datetime

class DatePickerInput(forms.DateInput):
    input_type = 'date'
    attrs={'min': datetime.datetime.today().date(), 'max': (datetime.datetime.today() + datetime.timedelta(days=4)).date()}

class RegionForm(forms.Form):
    region = forms.CharField(label='City', max_length=100)
    start_date = forms.DateField(widget=DatePickerInput(DatePickerInput.attrs))
    end_date = forms.DateField(widget=DatePickerInput(DatePickerInput.attrs))

    