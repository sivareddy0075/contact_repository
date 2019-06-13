from django import forms
class ContaForm(forms.Form):
    first_name = forms.CharField(
        label='Enter Your First Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'First Name',
                 'class': 'form-control'

            }
        )
    )
    last_name = forms.CharField(
        label='Enter Your Last Name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Last Name',
                'class': 'form-control'
            }
        )
    )
    salary = forms.IntegerField(
        label='Enter Your Salary',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Salary',
                'class': 'form-control'
            }
        )
    )
    location = forms.CharField(
        label='Enter Your Location',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Location',
                'class': 'form-control'
            }
        )
    )
    mobile = forms.IntegerField(
        label='Enter Your Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Mobile Number',
                'class': 'form-control'
            }
        )
    )
