from django import forms
from django.forms import fields
from .models import Customer
from django.contrib.auth import password_validation
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm, UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _




class CustomerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}



class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus':True, 'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs=
    {'autocomplete': 'current-password', 'class':'form-control'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Old Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'current-password', 'autofocus':True, 'class':'form-control'}))
    
    new_password1 = forms.CharField(label=_('New Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}), 
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_('Confirm  New Password'), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class':'form-control'}))



class ResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"), max_length=254, 
    widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class':'form-control'}))


class ConfirmPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, 
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}),
    help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False,
    widget=forms.PasswordInput(attrs={'autocomplete':'new-password', 'class':'form-control'}))


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','delivary_mail','country']
        widgets = {'name':forms.TextInput(attrs={'class':'form-control'}), 'delivary_mail':forms.TextInput(attrs={'class':'form-control'}),
        'country':forms.Select(attrs={'class':'form-control'}),}



class PortfolioCheckoutForm(forms.Form):
    # theme_id = forms.IntegerField(widget=forms.HiddenInput())
    # pricing_id = forms.IntegerField(widget=forms.HiddenInput())
    doamain_name = forms.CharField(max_length=100, label= 'Desired or Existing domain name',
    widget=forms.TextInput(attrs={'class':'form-control'}))
    buy_doamin = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), 
    choices=[('Yes', 'Yes, help me buying this domain'), ('No', 'No, I already have this domain')], 
    label='You want to buy domain from Us ?')


class CheckFrm(forms.Form):
    theme_id = forms.IntegerField()
    pricing_id = forms.IntegerField()
    # adress = forms.ChoiceField()
    domain = forms.CharField(max_length=110)
    buy_doamin = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}), 
    choices=[('Yes', 'Yes, help me buying my domain'), ('No', 'No, I already have a domain')], 
    label='You want to buy domain from Us ?')
