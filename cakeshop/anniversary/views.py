from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from homepage.models import Cakeitem,SignFranchise,SignCustomer
# Create your views here.


def anni(request, data=None):
    if request.user.is_authenticated:
        cus=SignCustomer.objects.get(user=request.user)
        fran=SignFranchise.objects.filter(pin=cus.pin)
        print(fran)
        bcakes=Cakeitem.objects.none()
        for f in fran:
            if data == None:
                cak=Cakeitem.objects.filter(category="anni").filter(user=f.user)
            if data == '400-600':
                cak =Cakeitem.objects.filter(category="anni").filter(price500__gte=400, price500__lt=600).filter(user=f.user)
            elif data =='600-900':
                cak = Cakeitem.objects.filter(category="anni").filter(price1__gte=600, price1__lt=900, price500=None).filter(user=f.user)
            elif data =='900-1500':
                cak = Cakeitem.objects.filter(category="anni").filter(price2__gte=900, price2__lt=1500, price500=None, price1=None).filter(user=f.user)
            elif data =='Above1500':
                cak = Cakeitem.objects.filter(category="anni").filter(price3__gte=1500, price500=None, price1=None, price2=None).filter(user=f.user)

            elif data == 'Monginis':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="Monginis").filter(user=f.user)
            elif data == 'RibbonsandBallons':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="Ribbons and Balloons").filter(user=f.user)
            elif data == 'Merwans':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="Merwans").filter(user=f.user)
            elif data == '7thHeaven':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="7th Heaven").filter(user=f.user)
            elif data == 'BaskinRobins':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="Baskin-Robins").filter(user=f.user)
            elif data == 'legateau':
                cak=Cakeitem.objects.filter(category="anni").filter(brand="Le gateau").filter(user=f.user)
            bcakes = bcakes | cak
    else:
            if data == None:
                bcakes=Cakeitem.objects.filter(category="anni")
            if data == '400-600':
                bcakes =Cakeitem.objects.filter(category="anni").filter(price500__gte=400, price500__lt=600)
            elif data =='600-900':
                bcakes= Cakeitem.objects.filter(category="anni").filter(price1__gte=600, price1__lt=900, price500=None)
            elif data =='900-1500':
                bcakes= Cakeitem.objects.filter(category="anni").filter(price2__gte=900, price2__lt=1500, price500=None, price1=None)
            elif data =='Above1500':
                bcakes= Cakeitem.objects.filter(category="anni").filter(price3__gte=1500, price500=None, price1=None, price2=None) 

            elif data == 'Monginis':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="Monginis")
            elif data == 'RibbonsandBallons':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="Ribbons and Balloons")
            elif data == 'Merwans':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="Merwans")
            elif data == '7thHeaven':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="7th Heaven")
            elif data == 'BaskinRobins':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="Baskin-Robins")
            elif data == 'legateau':
                bcakes=Cakeitem.objects.filter(category="anni").filter(brand="Le gateau")
    return render(request,'anniversary.html',{'bcakes':bcakes})
class AnnidetView(View):
    def get(self, request, pid):
        bprod=Cakeitem.objects.get(id=pid)
        return render(request,'anniversarydet.html',{'bprod': bprod})