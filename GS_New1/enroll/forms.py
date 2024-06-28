from django import forms

class StudentRegistration(forms.Form):
    name = forms.CharField(help_text='only letters are allowed', label='Full Name', widget=forms.TextInput(attrs={'class':'name_class'}))
    email = forms.EmailField(help_text='email contains "@"', label='Email Address')
    passs = forms.BooleanField(label='Pass', required=False)
    # key = forms.CharField(widget=forms.HiddenInput)