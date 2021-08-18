from django import forms
from .models import Person

from django import forms

from phonenumber_field.formfields import PhoneNumberField

# from .models import NullablePhoneNumber


class PhoneNumberForm(forms.ModelForm):
    class Meta:
#         model = NullablePhoneNumber
        fields = ["phone_number"]


class CustomPhoneNumberFormField(PhoneNumberField):
    phonenumber = PhoneNumberField()
    # pass

class NameForm(forms.Form):
    name = forms.CharField(max_length=80)


class NumberForm(forms.Form):
    phonenumber = PhoneNumberField()

