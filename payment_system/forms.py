from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('website','location','email')

class contactForm(forms.Form):
    full_name = forms.CharField(required=False,max_length=100,help_text='100 Characters max.')
    email = forms.CharField(required=True)
    comment = forms.CharField(required=True,widget=forms.Textarea)
