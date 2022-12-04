from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponseRedirect,redirect
from .forms import FranchiseSignup, HomemadeSignup,CustomerSignup
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .models import SignFranchise,Signhome,SignCustomer
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from .models import Cakeitem
# Create your views here.
def intro(request):
    if request.user.is_authenticated:
        cus=SignCustomer.objects.filter(user=request.user)
        print(cus)
        if cus.exists(): 
            for c in cus:
                fran=SignFranchise.objects.filter(pin=c.pin)
                ntfran =SignFranchise.objects.filter(~Q(pin=c.pin))
            print(fran)   
            print(ntfran)
            
        else:
            ntfran=None
            fran= SignFranchise.objects.all()
    else:
        ntfran=None
        fran= SignFranchise.objects.all()
    return render(request,'homepage.html',{'fran':fran,'ntfran':ntfran})
def contact(request):
    return render(request,'contactpage.html')
def offer(request):
    return render(request,'discounts.html')
def faq(request):
    return render(request,'faq.html')
def fran(request):
    if request.method == 'POST':
        if request.POST.get('signup'): #name of signup button if SignUp button is clicked
            fm1=FranchiseSignup(request.POST,prefix="fm1")
            fm2=AuthenticationForm(prefix="fm2")
            if fm1.is_valid():
                user=fm1.save()
                br=fm1.cleaned_data['brand']
                ad=fm1.cleaned_data['addr']
                pi=fm1.cleaned_data['pin']
                gs=fm1.cleaned_data['gstno']
                nm=fm1.cleaned_data['nameper']
                mo=fm1.cleaned_data['mobile']
                freg = SignFranchise(user=user, brand=br, address=ad, pin=pi, gst=gs, name=nm, mobile=mo)
                freg.save()
                messages.add_message(request, messages.SUCCESS, 'SignUp successful!!')
                return HttpResponseRedirect('/franchise/')
        elif request.POST.get('login'):
            fm2=AuthenticationForm(request=request, data=request.POST, prefix="fm2")
            fm1=FranchiseSignup(prefix="fm1")

            if fm2.is_valid():
                uname=fm2.cleaned_data['username']
                upass=fm2.cleaned_data['password']
                uid=User.objects.get(username=uname)
                fran=SignFranchise.objects.filter(user_id=uid)
                print(fran)
                au=authenticate(username=uname,password=upass)
                if au is not None and fran.exists():
                    login(request, au)
                    return HttpResponseRedirect('/franprofile/')
    else:
        fm2=AuthenticationForm(prefix="fm2")
        fm1=FranchiseSignup(prefix="fm1")
    
    return render(request,'franchise.html',{'fm1': fm1, 'fm2':fm2})

#Homemade bakers
def homebake(request):
    if request.method == 'POST':
        if request.POST.get('hsign'):
            hm1= HomemadeSignup(request.POST, prefix="hm1")
            hm2=AuthenticationForm(prefix="hm2")
            if hm1.is_valid():
                        user=hm1.save()
                        ad=hm1.cleaned_data['addr']
                        pi=hm1.cleaned_data['pin']
                        fs=hm1.cleaned_data['fssai']
                        nm=hm1.cleaned_data['name']
                        mo=hm1.cleaned_data['mobile']
                        hreg = Signhome(user=user,address=ad, pin=pi, fss=fs, name=nm, mobile=mo)
                        hreg.save()
                        return HttpResponseRedirect('/homepayment/')
        elif request.POST.get('hlogin'):
            hm2=AuthenticationForm(request=request, data=request.POST, prefix="hm2")
            hm1=HomemadeSignup(prefix="hm1")
            if hm2.is_valid():
                uname=hm2.cleaned_data['username']
                upass=hm2.cleaned_data['password']
                au=authenticate(username=uname,password=upass)
                if au is not None:
                    login(request, au)
                    return HttpResponseRedirect('/homeprofile/')
    else:
        hm2=AuthenticationForm(prefix="hm2")
        hm1=HomemadeSignup(prefix="hm1")
    return render(request,'homebaker.html',{'hm1': hm1,'hm2': hm2})

def custlogin(request):
    if request.method == 'POST':
        if request.POST.get('csign'):
            cm1= CustomerSignup(request.POST, prefix="cm1")
            cm2=AuthenticationForm(prefix="cm2")
            log=None
            if cm1.is_valid():
                    user=cm1.save()
                    ad=cm1.cleaned_data['addr']
                    pi=cm1.cleaned_data['pin']
                    nm=cm1.cleaned_data['name']
                    mo=cm1.cleaned_data['mobile']
                    hreg = SignCustomer(user=user,address=ad, pin=pi, name=nm, mobile=mo)
                    hreg.save()
                    return HttpResponseRedirect('/custlogin/')
        elif request.POST.get('clogin'):
            cm2=AuthenticationForm(request=request, data=request.POST, prefix="cm2")
            cm1=CustomerSignup(prefix="cm1")
            log=None
            if cm2.is_valid():
                uname=cm2.cleaned_data['username']
                upass=cm2.cleaned_data['password']
                uid=User.objects.get(username=uname)
                cust=SignCustomer.objects.filter(user_id=uid)
                print(fran)
                au=authenticate(username=uname,password=upass)
                if au is not None and cust.exists():
                    login(request, au)
                    log=request.user
                    return HttpResponseRedirect('/')
            
    else:
        cm2=AuthenticationForm(prefix="cm2")
        cm1=CustomerSignup(prefix="cm1") 
        log=None
    return render(request,'customerlogin.html',{'cm2':cm2,'cm1':cm1})
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')
def home(request, data=None): 
    if request.user.is_authenticated:
        cus=SignCustomer.objects.get(user=request.user)
        hom=Signhome.objects.filter(pin=cus.pin)
        franitem=Cakeitem.objects.none()
        for h in hom:
            if data == None:
                item=Cakeitem.objects.filter(brand="homemade").filter(user=h.user)
            elif data == 'birth':
                item=Cakeitem.objects.filter(brand="homemade").filter(category="birth").filter(user=h.user)
            elif data == 'anni':
                item=Cakeitem.objects.filter(brand="homemade").filter(category="anni").filter(user=h.user)
            elif data == 'grad':
                item=Cakeitem.objects.filter(brand="homemade").filter(category="grad").filter(user=h.user)
            elif data == 'kid':
                item=Cakeitem.objects.filter(brand="homemade").filter(category="kid").filter(user=h.user)
            elif data == 'pastry':
                item=Cakeitem.objects.filter(brand="homemade").filter(category="pastry").filter(user=h.user)
            franitem = franitem | item
    else:
            if data == None:
                franitem=Cakeitem.objects.filter(brand="homemade")
            elif data == 'birth':
                franitem=Cakeitem.objects.filter(brand="homemade").filter(category="birth")
            elif data == 'anni':
                franitem=Cakeitem.objects.filter(brand="homemade").filter(category="anni")
            elif data == 'grad':
                franitem=Cakeitem.objects.filter(brand="homemade").filter(category="grad")
            elif data == 'kid':
                franitem=Cakeitem.objects.filter(brand="homemade").filter(category="kid")
            elif data == 'pastry':
                franitem=Cakeitem.objects.filter(brand="homemade").filter(category="pastry")
    return render(request,'homemade.html',{'fitem':franitem})
def year(request):
    if request.method=='POST':
        user=request.user.username
        name=request.POST['name']
        email=request.POST['email']
        username=request.POST['usernam']
        print(username)
        print("USER:",user)
        if username==user:
            print(username)
            currentuse= SignCustomer.objects.get(user=request.user)
            currentuse.yearlsub="Yes"
            currentuse.save()
     
        else:
            messages.add_message(request, messages.ERROR, 'You need to login or incorrect username!')

    return render(request,'yearlysub.html')

def payhome(request):
    if request.method=='POST':
        messages.add_message(request, messages.SUCCESS, 'Sign Up successful!!!') 
        return HttpResponseRedirect('/homebaker/')
    return render(request, 'payhome.html')
