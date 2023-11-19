from django.urls import path, include
from . import views

app_name = 'giftlist'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('navbar/', views.navbar, name='navbar'),
    path('purchase-gift/<pk>', views.purchase_gift, name='purchase-gift'),
    path('purchased-list/', views.purchased_list, name='purchased-list'),
    path('update-my-gift/<pk>', views.update_my_gift, name='update-my-gift'),
    path('view-family-list/', views.view_family_list, name='view-family-list'),
    path('view-gift-details/<pk>', views.view_gift_details, name='view-gift-details'),
    path('view-my-list/', views.view_my_list, name='view-my-list'),
    path('add-gift/', views.add_gift, name='add-gift'),
    path('view-sortby-category', views.view_sortby_category, name='view-sortby-category'),
    path('view-sortby-status', views.view_sortby_status, name='view-sortby-status'),
    path('view-sortby-person', views.view_sortby_person, name='view-sortby-person'),
    path('view-sortby-gift', views.view_sortby_gift, name='view-sortby-gift'),
]
