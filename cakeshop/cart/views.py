from django.db.models import Q
from django.http import request
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from .models import Cartitem,Cart
from homepage.models import Cakeitem,SignCustomer
# Create your views here.
def cartdata(request):
    pid=request.GET.get('prod_id')
    cakeid=Cakeitem.objects.get(id=pid)
    kg=request.GET.get('kg')
    reg=Cart(cid=cakeid, kg=kg, user=request.user)
    reg.save()
    return redirect('/cart')
def showcart(request):
    if request.user.is_authenticated:
        user=request.user
        carts=Cart.objects.filter(user=request.user)
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
            print(amt)
        else:
            totamt= None
        return render(request, 'cart.html',{'carts':carts, 'totamt':totamt,'amt': amt, 'discount': discount})

def pluscart(request):
    if request.method == "GET":
        user=request.user
        cid = request.GET['cid']
        c = Cart.objects.get(Q(cid=cid) & Q(user=request.user))
        c.quan+=1
        c.save()
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
            data ={
                'quan': c.quan,
                'amt': amt,
                'totamt': totamt,
                'discount': discount
            }
            return JsonResponse(data)
def minuscart(request):
    if request.method == "GET":
        user=request.user
        cid = request.GET['cid']
        c = Cart.objects.get(Q(cid=cid) & Q(user=request.user))
        c.quan-=1
        c.save()
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
            data ={
                'quan': c.quan,
                'amt': amt,
                'totamt': totamt,
                'discount': discount
            }
            return JsonResponse(data)
def removeitem(request):
    if request.method == "GET":
        user=request.user
        cid = request.GET['cid']
        c = Cart.objects.get(Q(cid=cid) & Q(user=request.user))
        c.delete()
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
            data ={
                'amt': amt,
                'totamt': totamt,
                'discount': discount
            }
            return JsonResponse(data)
