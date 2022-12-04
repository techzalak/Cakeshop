from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Cakeitem,SignFranchise,SignCustomer
from django.views import View
# Create your views here.
#homepage
def kidcake(request, data=None):  
     if request.user.is_authenticated:
        cus=SignCustomer.objects.get(user=request.user)
        fran=SignFranchise.objects.filter(pin=cus.pin)
        print(fran)
        bcakes=Cakeitem.objects.none()
        for f in fran:

          if data == None:
               cak=Cakeitem.objects.filter(category="kid").filter(user=f.user)
          if data == 'Below600':
               cak = Cakeitem.objects.filter(category="kid").filter(price500__lt=600).filter(user=f.user)
          elif data =='600-1000':
               cak = Cakeitem.objects.filter(category="kid").filter(price1__gte=600, price1__lt=1000, price500=None).filter(user=f.user)
          elif data =='Above1000':
               cak = Cakeitem.objects.filter(category="kid").filter(price2__gte=1000, price500=None, price1=None).filter(user=f.user)
          
          elif data == 'Monginis':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="Monginis").filter(user=f.user)
          elif data == 'RibbonsandBallons':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="Ribbons and Balloons").filter(user=f.user)
          elif data == 'Merwans':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="Merwans").filter(user=f.user)
          elif data == '7thHeaven':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="7th Heaven").filter(user=f.user)
          elif data == 'BaskinRobins':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="Baskin-Robins").filter(user=f.user)
          elif data == 'LeGateau':
               cak=Cakeitem.objects.filter(category="kid").filter(brand="Le gateau").filter(user=f.user)  
          bcakes= bcakes | cak
     else:
          
          if data == None:
               bcakes=Cakeitem.objects.filter(category="kid")
          if data == 'Below600':
               bcakes = Cakeitem.objects.filter(category="kid").filter(price500__lt=600)
          elif data =='600-1000':
               bcakes = Cakeitem.objects.filter(category="kid").filter(price1__gte=600, price1__lt=1000, price500=None)
          elif data =='Above1000':
               bcakes = Cakeitem.objects.filter(category="kid").filter(price2__gte=1000, price500=None, price1=None)
          
          elif data == 'Monginis':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="Monginis")
          elif data == 'RibbonsandBallons':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="Ribbons and Balloons")
          elif data == 'Merwans':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="Merwans")
          elif data == '7thHeaven':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="7th Heaven")
          elif data == 'BaskinRobins':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="Baskin-Robins") 
          elif data == 'LeGateau':
               bcakes=Cakeitem.objects.filter(category="kid").filter(brand="Le gateau")  

     return render(request,'kids.html',{'bcakes':bcakes})
class KiddetView(View):
    def get(self, request, pid):
        bprod=Cakeitem.objects.get(id=pid)
        return render(request,'kidsdet.html',{'bprod': bprod})