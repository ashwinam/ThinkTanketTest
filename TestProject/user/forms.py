from django import forms
from .models import UserTbl


class SignUpForm(forms.ModelForm):
    class Meta:
        model = UserTbl
        fields = ['first_name', 'last_name', 'username', 'email', 'mobile_no', 'date_of_birth', 'hobbies']
        widgets = {
            'hobbies': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'date_of_birth': forms.DateInput(attrs={'type':'date'})
        }


class SignInForm(forms.Form):
    email = forms.EmailField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

