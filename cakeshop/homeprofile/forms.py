from django import forms
cate_choices=[
    ('birth','Birthday',),
    ('anni','Anniversary'),
    ('grad', 'Graduation'),
    ('kid','Kids'),
    ('pastry','Pastries'),
]

class Homepro(forms.Form):
    name=forms.CharField(label="Cake Name*",widget=forms.TextInput(attrs={'placeholder':'Enter cake name','class':'form-control'}))
    category =forms.CharField(label="Category*", widget=forms.Select(choices=cate_choices, attrs={'class':'form-control'}))
    cimg=forms.ImageField(label="Cake image*", widget=forms.FileInput(attrs={'class':'form-control-file'}))
    des=forms.CharField(label="Description*",widget=forms.Textarea(attrs={'placeholder':'Enter Description','class':'form-control'}))
    price500=forms.IntegerField(label="Price of 500 gms",required= False,widget=forms.TextInput(attrs={'placeholder':'Enter Price of 500gms','class':'form-control'}))
    price1=forms.IntegerField(label="Price of 1 kg",required= False,widget=forms.TextInput(attrs={'placeholder':'Enter Price of 1kg','class':'form-control'}))
    price2=forms.IntegerField(label="Price of 2 kg",required= False,widget=forms.TextInput(attrs={'placeholder':'Enter Price of 2kg','class':'form-control'}))
    price2=forms.IntegerField(label="Price of 2 kg",required= False,widget=forms.TextInput(attrs={'placeholder':'Enter Price of 2kg','class':'form-control'}))
    price3=forms.IntegerField(label="Price of 3 kg",required= False,widget=forms.TextInput(attrs={'placeholder':'Enter Price of 3kg','class':'form-control'}))
    def clean(self):
        price500 = self.cleaned_data.get('price500')
        price1 = self.cleaned_data.get('price1')
        price2 = self.cleaned_data.get('price2')
        price3 = self.cleaned_data.get('price3')
        if not price500 and not price1 and not price2 and not price3:
            raise forms.ValidationError('One of fields is required')
        return self.cleaned_data