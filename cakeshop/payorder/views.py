from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
import stripe
from django.urls import reverse
from .models import Cakeorder
from .models import Cakeitem
from cart.models import Cart
from homepage.models import SignCustomer
stripe.api_key = 'sk_test_tR3PYbcVNZZ796tH88S4VQ2u'
# Create your views here.
def pay(request):
    user= request.user
    citem=Cart.objects.filter(user=user)
    amt=0
    delamt= 60
    discount = 0
    useryear=SignCustomer.objects.get(user=request.user)
    carttot = [p for p in Cart.objects.all() if p.user == user]
    print(carttot)
    if carttot:
            for p in carttot:
                quant= p.quan
                if p.kg == 500:
                    amt= amt+ quant * p.cid.price500
                elif p.kg == 1:
                    amt= amt+ quant * p.cid.price1
                elif p.kg == 2:
                    amt= amt+ quant * p.cid.price2
                elif p.kg == 3:
                    amt= amt+ quant * p.cid.price3
            totamt=amt+delamt
            if useryear.yearlsub == 'Yes':
                discount = totamt * 0.05
                totamt = totamt - discount
    return render(request,'payment.html',{'totamt':totamt, 'discount': discount, 'amt': amt})
def charge(request):
    if request.method == 'POST':
        user=request.user
        amt=request.POST['amt']
        addr=request.POST['addr']
        deldate=request.POST['deldate']
        cart= Cart.objects.filter(user=user)
        for c in cart:
            Cakeorder(user=request.user,addr=addr,cid=c.cid,delivery_date=deldate, quan=c.quan, kg=c.kg).save()
            c.delete()
        print('Data', request.POST)
    return redirect(reverse('success', args=[amt]))
def success(request, args):
    amt = args
    return render(request, 'paysuccess.html',{'amt': amt})
def payind(request):
    user=request.user
    cid=request.GET.get("prod_id")
    citem=Cakeitem.objects.get(id=cid)
    kg=request.GET.get("kg")
    discount = 0
    useryear=SignCustomer.objects.get(user=request.user)
    print(kg)
    if kg == '500':
        amt=citem.price500
    elif kg == '1':
        amt=citem.price1
    elif kg == '2':
        amt=citem.price2
    elif kg == '3':
        amt=citem.price3 
    totamt= amt + 60
    if useryear.yearlsub == 'Yes':
        discount = totamt * 0.05
        totamt = totamt - discount
    return render(request,'payind.html',{'totamt':totamt, 'cid': cid, 'kg': kg, 'discount' : discount,'amt': amt})
def chargeind(request):
    if request.method == 'POST':
        user=request.user
        amt=request.POST['amt']
        addr=request.POST['addr']
        deldate=request.POST['deldate']
        cid=request.POST["prod_id"]
        kg=request.POST["kg"]
        citem=Cakeitem.objects.get(id=cid)
        Cakeorder(user=request.user,addr=addr,cid=citem,delivery_date=deldate, quan=1, kg=kg).save()
        print('Data', request.POST)
    return redirect(reverse('success', args=[amt]))