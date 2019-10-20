from django import forms
class LengthConverterForm(forms.Form):
    MEASUREMENTS = (
        ('centimetre', 'Centimetre'),
        ('metre', 'Metre'),
        ('mile', 'Mile'),
        ('kilometer', 'KiloMeter'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS, widget=forms.Select(attrs={'class':'regDropDown'}))
    input_value = forms.DecimalField(decimal_places=3, widget=forms.TextInput(attrs={'class':' inputfield'}))
    output_unit = forms.ChoiceField(choices=MEASUREMENTS, widget=forms.Select(attrs={'class':'regDropDown'}))
    output_value = forms.DecimalField(decimal_places=3, required=False, widget=forms.TextInput(attrs={'class':'outputfield', 'readonly':True}))