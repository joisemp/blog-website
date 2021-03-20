from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.forms.models import model_to_dict
from blog.models import Profile

#------------------------------------------------------------------------------------------------------------------------------------------------------

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


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'profile_pic', 'website_url', 'instagram_url', 'facebook_url', 'twitter_url', 'linkedin_url', 'snapchat_url')
        widgets = {
                'bio':forms.Textarea(attrs={'class':'form-control'}),
                #'profile_pic':forms.TextInput(attrs={'class':'form-control'}), # This is the author input. The value is automatically entered useing javascript in the front end and the text box is hidden so that the user can't edit it.,
                'website_url':forms.TextInput(attrs={'class':'form-control'}),
                'instagram_url':forms.TextInput(attrs={'class':'form-control'}),
                'facebook_url':forms.TextInput(attrs={'class':'form-control'}),
                'twitter_url':forms.TextInput(attrs={'class':'form-control'}),
                'linkedin_url':forms.TextInput(attrs={'class':'form-control'}),
                'snapchat_url':forms.TextInput(attrs={'class':'form-control'}),         
            }
        
        