
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


#choice =( ('Male'),
        #('Female'))


class RegisterForm(UserCreationForm):

    #choice =( ('Male'),
        #    ('Female'))

    email_address = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    middle_name = forms.CharField(required = False)
    Gender = forms.ChoiceField(choices =[ ('','choose'),('','male'),('','female')])
    alternative_phone = forms.CharField(required = False)



    class meta:
        model = User
        fields = ['first_name', 'last_name','middle_name','Gender','phone','alternative_phone','email','password1','password2','f_name']
