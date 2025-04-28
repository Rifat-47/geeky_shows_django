from django import forms
import re

class CustomerRegistration(forms.Form):
    cname = forms.CharField(label='Customer Name')
    cemail = forms.EmailField(label='Customer Email')
    cpassword = forms.CharField(label='Customer Password', widget=forms.PasswordInput)

    def clean_cname(self):
        customer_name = self.cleaned_data['cname'] # self.cleaned_data.get('cname')
        if len(customer_name) < 5 :
            raise forms.ValidationError("Customer name must have 5 character.")
        elif len(customer_name) > 20:
            raise forms.ValidationError("Name is too big!")
        return customer_name

    def clean_cemail(self):
        customer_email = self.cleaned_data.get('cemail')
        if len(customer_email) < 12:
            raise forms.ValidationError('Valid email contain 12 character')
        return customer_email

    def clean_cpassword(self):
        customer_password = self.cleaned_data['cpassword']
        if len(customer_password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        if not re.search(r'[A-Z]', customer_password):
            raise forms.ValidationError("Password must contain at least one uppercase letter.")
        if not re.search(r'[a-z]', customer_password):
            raise forms.ValidationError("Password must contain at least one lowercase letter.")
        if not re.search(r'[0-9]', customer_password):
            raise forms.ValidationError("Password must contain at least one digit.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', customer_password):
            raise forms.ValidationError("Password must contain at least one special character.")
        return customer_password