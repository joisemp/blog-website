from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from django.forms.models import model_to_dict

class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


        # The for loop below removes the input requirements text listed near the inputs of username, password1, password2. Remove the for loop statement to display the input requirements
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    username= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # last_login= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    # is_superuser= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_staff= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # is_active= forms.CharField(max_length=100, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    # date_joined= forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model=User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields['password'].widget.attrs['class'] = 'form-control'
        #self.fields['password'].help_text = None

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2= forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')