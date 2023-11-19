from django.db import models

# Create your models here.
from datetime import date
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['category_name']

    def __str__(self):
        return self.category_name
    

class Gift(models.Model):
    STATUS = (
    ('Available', 'Available'),
    ('Purchased', 'Purchased'),
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.CASCADE)
    retailer = models.CharField(max_length=200, null=True, blank=True)
    retailer_link = models.URLField(max_length=200, null=True, blank=True, help_text="For example: the link to an item on Amazon.")
    qty_asked_for = models.IntegerField(default=1 , null=True)
    qty_purchased = models.IntegerField(default=0, null=True , blank=True)
    estimated_price = models.FloatField(null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS, default='Available')
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    purchased_by = models.ForeignKey("Member", related_name='related_gift_purchaser', null=True, blank=True, on_delete=models.CASCADE)
    gift_for = models.ForeignKey("Member", related_name='related_gifts_for_member', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @property
    def select_cat(self):
        return self.get_category_display()        

 

    

class Member(models.Model):
    first_name= models.CharField(max_length=200, null=True)
    last_name= models.CharField(max_length=200, null=True)
    email= models.EmailField(max_length=200, null=True, blank=True)
    cellphone= models.CharField(max_length=200,null=True, blank=True)
    parent= models.ForeignKey("auth.User", null=True, blank=True, on_delete=models.CASCADE)
    date_created= models.DateTimeField(auto_now_add=True, null=True)
    is_shopper = models.BooleanField(default=False)

    
    def __str__(self):
        return self.first_name
    



class Shopper(Member):
    purchased_gifts = models.ForeignKey("Gift", null=True, blank=True, on_delete=models.CASCADE)
    favorite_coffee = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.first_name
    
class Profile(models.Model):
    profile_for = models.ForeignKey('Member',null=True, blank=True, on_delete=models.CASCADE)
    shirt_size = models.CharField(max_length=50, null=True, blank=True)
    pants_size = models.CharField(max_length=50, null=True, blank=True)
    shoe_size = models.CharField(max_length=50, null=True, blank=True)
    favorite_music_artist = models.CharField(max_length=50, null=True, blank=True)
    favorite_gift_card = models.CharField(max_length=50, null=True, blank=True)
    favorite_color = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.profile_for.first_name
    
    @property
    def get_id(self):
        return self.profile_for.id







