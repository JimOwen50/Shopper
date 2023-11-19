from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from .models import *
from .forms import *
from django.http import HttpResponse, HttpResponseRedirect

def base(request):
    return render(request, 'giftlist/base.html')

def index(request):
    return render(request, 'giftlist/index.html')

def about(request):
    return render(request, 'giftlist/about.html')

def userlogin(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/view-my-list/")
    context = {'form':form}

    return render(request, 'giftlist/userlogin.html', context=context)

def user_logout(request):
    auth.logout(request)
    messages.success(request, "Logged Out !")
    return redirect("/userlogin")

# @login_required(login_url='userlogin')    
# def view_my_profile(request):
#     person = Member.objects.get(first_name=request.user.username)
#     profile = Profile.objects.get(profile_for=person)
#     form = MemberProfileForm()
#     if not profile:
#         if request.method == 'POST':
#             form = MemberProfileForm(request.POST)
#             if form.is_valid():
#                 new_post = form.save(commit=False)
#                 new_post.profile_for = person

#                 new_post.save()

#                 messages.success(request, "Your profile was added!")
#                 return redirect("/view-my-list/")
#         context = {'form':form, 'person':person}
#     context = {'form':form, 'person':person}
#     return render(request, 'giftlist/view-my-profile.html', context)

# @login_required(login_url='userlogin')
# def update_my_profile(request, pk):
#     record = Profile.objects.get(id=pk)
#     form = MemberProfileForm(instance=record)
#     if request.method == 'POST':
#         form = MemberProfileForm(request.POST, instance=record)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your profile was updated!")
#             return redirect("/view-my-list/")
#     context = {'form':form}
#     return render(request, 'giftlist/my-profile.html', context)



@login_required(login_url='userlogin')
def navbar(request):
    member = Member.objects.get(first_name=request.user.username)
    context = {'member':member}
    return render(request, 'giftlist/navbar.html', context)

@login_required(login_url='userlogin')
def purchase_gift(request, pk):
    gift = Gift.objects.get(id=pk)
    person = Gift.gift_for
    buyer = Member.objects.get(first_name=request.user.username)
    form = PurchaseGiftForm(instance=gift)
    if request.method == 'POST':
        form = PurchaseGiftForm(request.POST, instance=gift)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.purchased_by = buyer
            new_post.status = "Purchased"
            new_post.save()
            messages.success(request, "Gift purchased !")
            return redirect("/view-family-list/")
    context = {'gift':form, 'person':person}
    return render(request, 'giftlist/purchase-gift.html', context)

@login_required(login_url='userlogin')
def purchased_list(request):
    person = Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.filter(purchased_by = person).all().order_by('gift_for__first_name')
    
    # for recipient in recipients:
    #     gifts_bought = recipients[recipient]
    #     subtotal = sum(gifts_bought['qty-purchased']*gifts_bought['price'] for recipient in recipients)
    #     subtotal = '{:.2f}'.format(subtotal)
    #     # total += subtotal
    #     recipients[recipient] = {'gifts_bought':gifts_bought, 'subtotal':subtotal}
    
    gift_total = Gift.objects.filter(purchased_by = person).aggregate(gift_total=Sum('price'))['gift_total'] or 0
    gift_total = '{:.2f}'.format(gift_total)
    context = {'gifts':gifts, 'person':person, 'gift_total':gift_total}
    return render(request, 'giftlist/purchased-list.html', context)


# total = 0
# for org in orgs:
#     orders = orgs[org]
#     subtotal = sum(order['qty']*order['price'] for order in orders)
#     total += subtotal
#     orgs[org] = {'orders': orders, 'subtotal': subtotal}









@login_required(login_url='userlogin')
def update_my_gift(request, pk):
    record = Gift.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!")
            return redirect("/view-my-list/")
    context = {'form':form}
    return render(request, 'giftlist/update-my-gift.html', context)

@login_required(login_url='userlogin')
def add_gift(request):
    person = Member.objects.get(first_name=request.user.username)
    form = UpdateRecordForm()
    if request.method == 'POST':
        form = UpdateRecordForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.gift_for = person

            new_post.save()

            messages.success(request, "Your record was added!")
            return redirect("/view-my-list/")
    context = {'form':form}
    return render(request, 'giftlist/add-gift.html', context)


@login_required(login_url='userlogin')
def view_family_list(request):
    person= Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.all().order_by('gift_for__first_name', 'category', 'name', 'status')        
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-family-list.html', context)

@login_required(login_url='userlogin')
def view_sortby_category(request):
    person= Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.all().order_by('category','gift_for__first_name', 'name',)        
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-family-list.html', context)

@login_required(login_url='userlogin')
def view_sortby_status(request):
    person= Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.all().order_by('status','gift_for__first_name', 'name',)        
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-family-list.html', context)

@login_required(login_url='userlogin')
def view_sortby_person(request):
    person= Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.all().order_by('gift_for__first_name', 'status', 'name',)        
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-family-list.html', context)

@login_required(login_url='userlogin')
def view_sortby_gift(request):
    person= Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.all().order_by( 'name','gift_for__first_name', 'category', 'status',)        
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-family-list.html', context)

@login_required(login_url='userlogin')
def view_gift_details(request, pk):
    person = Member.objects.get(first_name=request.user.username)
    gift = Gift.objects.get(id=pk)
    context = {'gift':gift, 'person':person}
    return render(request, 'giftlist/view-gift-details.html', context)

@login_required(login_url='userlogin')
def view_my_list(request):
    person = Member.objects.get(first_name=request.user.username)
    gifts = Gift.objects.filter(gift_for = person).all()
    context = {'gifts':gifts, 'person':person}
    return render(request, 'giftlist/view-my-list.html', context)

@login_required(login_url='userlogin')
def delete_record(request, pk):
    record = Gift.objects.get(id=pk)
    record.delete()
    messages.success(request, "Your record was deleted!")
    return redirect('giftlist/view-my-list.html')




