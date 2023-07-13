from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from .models import Items, Vendors, StockIn, StockOut, Reports


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")


class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ("username", "email")


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        exclude = ["qr_code"]


class ItemUpdateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = '__all__'


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = "__all__"


class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = "__all__"


class StockinForm(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = "__all__"


class StockinUpdate(forms.ModelForm):
    class Meta:
        model = StockIn
        fields = "__all__"


class StockoutForm(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = "__all__"


class StockoutUpdate(forms.ModelForm):
    class Meta:
        model = StockOut
        fields = "__all__"


class ReportForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = "__all__"


class ReportUpdateForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = '__all__'
