from django import forms
from .models import productDetails, productPath, productSuggestions, Manufacturer, Category

class productForm(forms.ModelForm):
    class Meta:
        model = productDetails
        fields ="__all__"
        labels ={
            'Product Name':'Name of Product',
        }
    def __init__(self, *args, **kwargs):
        super(productForm,self).__init__(*args, **kwargs)
        self.fields['category_Id'].empty_label ="Select"
        self.fields['manufacturer_Id'].empty_label ="Select"

class pathForm(forms.ModelForm):
    class Meta:
        model = productPath
        fields="__all__"

class OrderForm(forms.ModelForm):
    class Meta:
        model = productSuggestions
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super(OrderForm,self).__init__(*args, **kwargs)
        self.fields['productId'].empty_label ="Select"

class ManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields ="__all__"

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields ="__all__"