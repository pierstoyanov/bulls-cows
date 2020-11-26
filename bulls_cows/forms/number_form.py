from django import forms

class NumberForm(forms.Form):
    # digit_zero = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_one = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_two = forms.IntegerField(max_value=9, min_value=0, label='')
    # digit_three = forms.IntegerField(max_value=9, min_value=0, label='')
    digits_input = forms.IntegerField(widget=TextInput(attrs={'type':'number'}))