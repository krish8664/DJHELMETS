from django import forms
from djhelmet.models import Colors, Size

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
    color=Colors.objects.all()
    size=Size.objects.all()
    print size
    product_brand_name  =   forms.CharField(label = 'Enter Brand Name', required = True)
    product_model_name  =   forms.CharField(label = 'Enter Model Name', required = True)
    price               =   forms.CharField(label = 'Enter Price in INR', required = True)
    COLOR_OPTIONS=()
    for selected_color in color:
        COLOR_OPTIONS+=((selected_color.color,selected_color.color),)
    product_color       = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=COLOR_OPTIONS)
    SIZE_OPTIONS=()
    for selected_size in size:
        SIZE_OPTIONS+=((selected_size.size,selected_size.size),)
    product_size        = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=SIZE_OPTIONS)
    picture             = forms.FileField(label='Select a file', help_text='max. 42 megabytes', required = False)

    def __init__(self, *args, **kwargs):
        super(add_product, self).__init__(*args, **kwargs)