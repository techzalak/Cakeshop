from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from homepage.models import Cakeitem
from django.views import View
# Create your views here.
#def b_monginis(request):
   # franitem=Cakeitem.objects.filter(brand='Monginis')
    #return render(request,'brmonginis.html',{'fitem':franitem})

def b_monginis(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="Monginis")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="Monginis").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="Monginis").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="Monginis").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="Monginis").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="Monginis").filter(category="pastry") 

    return render(request,'brmonginis.html',{'fitem':franitem})

def b_ribbal(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="Ribbons and Balloons").filter(category="pastry") 

    return render(request,'brribbal.html',{'fitem':franitem})
    
def b_merwans(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="Merwans")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="Merwans").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="Merwans").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="Merwans").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="Merwans").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="Merwans").filter(category="pastry") 

    return render(request,'brmerwans.html',{'fitem':franitem})

def b_heaven(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="7th Heaven")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="7th Heaven").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="7th Heaven").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="7th Heaven").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="7th Heaven").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="7th Heaven").filter(category="pastry") 

    return render(request,'brheaven.html',{'fitem':franitem})

def b_basrob(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="Baskin-Robins").filter(category="pastry") 

    return render(request,'brbasrob.html',{'fitem':franitem})

def b_lgateau(request, data=None):   
    if data == None:
        franitem=Cakeitem.objects.filter(brand="Le gateau")
    

    elif data == 'birth':
        franitem=Cakeitem.objects.filter(brand="Le gateau").filter(category="birth")
    elif data == 'anni':
        franitem=Cakeitem.objects.filter(brand="Le gateau").filter(category="anni")
    elif data == 'grad':
        franitem=Cakeitem.objects.filter(brand="Le gateau").filter(category="grad")
    elif data == 'kid':
        franitem=Cakeitem.objects.filter(brand="Le gateau").filter(category="kid")
    elif data == 'pastry':
        franitem=Cakeitem.objects.filter(brand="Le gateau").filter(category="pastry") 

    return render(request,'brlgateau.html',{'fitem':franitem})


class MondetView(View):
    def get(self, request, pid):
        bprod=Cakeitem.objects.get(id=pid)
        return render(request,'monginisdet.html',{'bprod': bprod})