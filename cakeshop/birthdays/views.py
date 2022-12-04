from django.shortcuts import render
from .models import Birthday
from django.views import View
from homepage.models import Cakeitem,Signhome,SignFranchise,SignCustomer
# Create your views here.

def birthcakes(request, data=None):
     if request.user.is_authenticated:
        cus=SignCustomer.objects.get(user=request.user)
        fran=SignFranchise.objects.filter(pin=cus.pin)
        print(fran)
        bcakes=Cakeitem.objects.none()
        for f in fran:
          if data == None:
               cak=Cakeitem.objects.filter(category="birth").filter(user=f.user)
          if data == '300-500':
               cak =Cakeitem.objects.filter(category="birth").filter(price500__gte=300, price500__lt=500).filter(user=f.user)
          elif data =='500-700':
               cak = Cakeitem.objects.filter(category="birth").filter(price1__gte=500, price1__lt=700, price500=None).filter(user=f.user)
          elif data =='700-900':
               cak = Cakeitem.objects.filter(category="birth").filter(price1__gte=700, price1__lt=900, price500=None).filter(user=f.user)
          elif data == 'Monginis':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="Monginis").filter(user=f.user)
          elif data == 'RibbonsandBallons':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="Ribbons and Balloons").filter(user=f.user)
          elif data == 'Merwans':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="Merwans").filter(user=f.user)
          elif data == '7thHeaven':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="7th Heaven").filter(user=f.user)
          elif data == 'BaskinRobins':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="Baskin-Robins").filter(user=f.user)
          elif data == 'LeGateau':
               cak=Cakeitem.objects.filter(category="birth").filter(brand="Le gateau").filter(user=f.user)
          bcakes = bcakes | cak

     else:
          if data == None:
               bcakes=Cakeitem.objects.filter(category="birth")
          if data == '300-500':
               bcakes =Cakeitem.objects.filter(category="birth").filter(price500__gte=300, price500__lt=500)
          elif data =='500-700':
               bcakes = Cakeitem.objects.filter(category="birth").filter(price1__gte=500, price1__lt=700, price500=None)
          elif data =='700-900':
               bcakes = Cakeitem.objects.filter(category="birth").filter(price1__gte=700, price1__lt=900, price500=None)
          elif data == 'Monginis':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="Monginis")
          elif data == 'RibbonsandBallons':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="Ribbons and Balloons")
          elif data == 'Merwans':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="Merwans")
          elif data == '7thHeaven':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="7th Heaven")
          elif data == 'BaskinRobins':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="Baskin-Robins")
          elif data == 'LeGateau':
               bcakes=Cakeitem.objects.filter(category="birth").filter(brand="Le gateau")
     return render(request,'birthdays.html',{'bcakes': bcakes})
class BirthdetView(View):
    def get(self, request, pid):
        bprod=Cakeitem.objects.get(id=pid)
        return render(request,'birthdaydet.html',{'bprod': bprod})
