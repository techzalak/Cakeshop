from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
class FranchiseSignup(UserCreationForm):
    brand=forms.CharField(label="Brand Name*",widget=forms.TextInput(attrs={'placeholder':'Enter brand name','class':'form-control'}))
    addr=forms.CharField(label="Address*",widget=forms.TextInput(attrs={'placeholder':'Enter address of shop','class':'form-control'}))
    pin=forms.CharField(label="Pincode*",widget=forms.TextInput(attrs={'placeholder':'Enter pincode of shop','class':'form-control'}))
    gstno=forms.CharField(label="GST no",widget=forms.TextInput(attrs={'placeholder':'Enter GST no of shop','class':'form-control'}))
    nameper=forms.CharField(label="Name of form filler",widget=forms.TextInput(attrs={'placeholder':'Enter name of form filler','class':'form-control'}))
    email=forms.EmailField(label="Email of form filler",widget=forms.TextInput(attrs={'placeholder':'Enter email of form filler','class':'form-control'}))
    mobile=forms.CharField(label="Mobile No",widget=forms.TextInput(attrs={'placeholder':'Enter mobile number','class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'form-control'}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter password','class':'form-control'}), help_text="")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['brand', 'addr' ,'pin','gstno','nameper','email','mobile','username','password1','password2']
        help_texts = {
            'username': None,
            'password1':"",
            'password2':"",
       
        }
    def clean_pin(self):
        valname = self.cleaned_data['pin']
        if(len(valname) != 6 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid pin code of 6 digits')
        return valname
    def clean_mobile(self):
        valname = self.cleaned_data['mobile']
        if(len(valname) != 10 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid mobile number of 10 digits')
        return valname
    def clean_gstno(self):
        valname=self.cleaned_data['gstno']
        if(len(valname) != 15):
            raise forms.ValidationError('Enter a valid Gst Number of your shop')
        return valname

class HomemadeSignup(UserCreationForm):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'Enter name','class':'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder':'Enter email address','class':'form-control'}))
    addr=forms.CharField(label="Address*",widget=forms.TextInput(attrs={'placeholder':'Enter address','class':'form-control'}))
    pin=forms.CharField(label="Pincode*",widget=forms.TextInput(attrs={'placeholder':'Enter pincode','class':'form-control'}))
    mobile=forms.CharField(label="Mobile No",widget=forms.TextInput(attrs={'placeholder':'Enter mobile number','class':'form-control'}))
    fssai=forms.ImageField(label="Submit fssai certificate", required=False,widget=forms.FileInput(attrs={'class':'form-control-file'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'form-control'}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter password','class':'form-control'}), help_text="")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name','email','addr' ,'pin','mobile','fssai','username','password1','password2']
        help_texts = {
            'username': None,
            'password1':"",
            'password2':"",
       
        }
    def clean_pin(self):
        valname = self.cleaned_data['pin']
        if(len(valname) != 6 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid pin code of 6 digits')
        return valname

    def clean_mobile(self):
        valname = self.cleaned_data['mobile']
        if(len(valname) != 10 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid mobile number of 10 digits')
        return valname

class CustomerSignup(UserCreationForm):
    name=forms.CharField(label="Name",widget=forms.TextInput(attrs={'placeholder':'Enter name','class':'form-control'}))
    email=forms.EmailField(label="Email",widget=forms.TextInput(attrs={'placeholder':'Enter email address','class':'form-control'}))
    addr=forms.CharField(label="Address*",widget=forms.TextInput(attrs={'placeholder':'Enter address','class':'form-control'}))
    pin=forms.CharField(label="Pincode*",widget=forms.TextInput(attrs={'placeholder':'Enter pincode','class':'form-control'}))
    mobile=forms.CharField(label="Mobile No",widget=forms.TextInput(attrs={'placeholder':'Enter mobile number','class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter username','class':'form-control'}))
    password2=forms.CharField(label="Confirm Password", widget=forms.PasswordInput(attrs={'placeholder':'Re-Enter password','class':'form-control'}), help_text="")
    password1=forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder':'Enter password','class':'form-control'}))
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['name','email','addr' ,'pin','mobile','username','password1','password2']
        help_texts = {
            'username': None,
            'password1':"",
            'password2':"",
       
        }
    def clean_pin(self):
        valname = self.cleaned_data['pin']
        if(len(valname) != 6 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid pin code of 6 digits')
        return valname
    def clean_mobile(self):
        valname = self.cleaned_data['mobile']
        if(len(valname) != 10 or not valname.isdecimal()):
            raise forms.ValidationError('Enter a valid mobile number of 10 digits')
        return valname