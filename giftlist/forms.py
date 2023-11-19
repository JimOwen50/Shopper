from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import Gift, Member, Profile

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['username', 'password1', 'password2']


# - Login a user

class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class GiftForm(forms.ModelForm):
    class Meta:
        model=Gift
        fields = ["name", 
                  "description", 
                  "category", 
                  "retailer",
                  "retailer_link", 
                  "qty_asked_for"]
        
        
class MemberProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ["shirt_size", 
                  "pants_size", 
                  "shoe_size",
                  "favorite_music_artist",
                  "favorite_gift_card", 
                  "favorite_color"]

# - Update a record

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["name", 
                  "description", 
                  "category", 
                  "retailer",
                  "retailer_link", 
                  "qty_asked_for"]
        
        
# - Purchase Gift

class PurchaseGiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ["retailer",
                  "qty_purchased",
                  "price",]




# - Create a record

# class CreateRecordForm(forms.ModelForm):

#     class Meta:

#         model = Record
#         fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']


# # - Update a record

# class UpdateRecordForm(forms.ModelForm):

#     class Meta:

#         model = Record
#         fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', 'country']
