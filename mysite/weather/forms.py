from django import forms

class NameForm(forms.Form):
    address = forms.CharField(label='Address', max_length=100)

# class WeatherForm(forms.Form):
#     address = forms.CharField(label='Address',)