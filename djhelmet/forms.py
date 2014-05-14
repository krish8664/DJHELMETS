from django import forms

class Admin_login(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(Admin_login, self).__init__(*args, **kwargs)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 1 or len(password) > 30:
            raise forms.ValidationError('Enter between 1 and 30 characters')
        return password

class add_product(forms.Form):
    product_brand_name  =   forms.CharField(label = 'Enter Brand Name', required = True)
    product_model_name  =   forms.CharField(label = 'Enter Model Name', required = True)
    price               =   forms.CharField(label = 'Enter Price in INR', required = True)
    product_color       =   forms.CharField(required = True)