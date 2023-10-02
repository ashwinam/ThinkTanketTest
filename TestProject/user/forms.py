from django import forms
from .models import UserTbl


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserTbl
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'date_of_birth', 'hobbies']
        widgets = {
            'hobbies': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
        }


class SignInForm(forms.ModelForm):
    class Meta:
        model = UserTbl
        fields = ['email', 'password']
