from django.contrib import admin

# Register your models here.
from .models import Member, Profile, Shopper, Gift, Category

admin.site.register(Member)
admin.site.register(Profile)
admin.site.register(Gift)
admin.site.register(Category)