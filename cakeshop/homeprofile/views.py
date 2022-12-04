from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,HttpResponseRedirect
from homepage.models import Cakeitem,Signhome
# Create your views here.
from .forms import Homepro
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def homedata(request): 
    if(request.user.is_authenticated):
 
        if(request.method=='POST'):
            hp1=Homepro(request.POST,request.FILES,prefix="hp1")
            currentuse= Signhome.objects.get(user=request.user) 
            if(hp1.is_valid()):
                br="homemade"
                cn=hp1.cleaned_data['name']
                ci=hp1.cleaned_data['cimg']
                ct=hp1.cleaned_data['category']
                pr500=hp1.cleaned_data['price500']
                pr1=hp1.cleaned_data['price1']
                pr2=hp1.cleaned_data['price2']
                pr3=hp1.cleaned_data['price3']
                de=hp1.cleaned_data['des']
                print(cn)
                hmreg=Cakeitem(user=request.user,brand=br,name=cn,cimg=ci,category=ct,price500=pr500,price1=pr1,price2=pr2,price3=pr3,des=de)
                hmreg.save()
                return HttpResponseRedirect('/homeprofile/')
        else:
            hp1 = Homepro(prefix="hp1")
        return render(request,'homeprofile.html', {'hp1': hp1})  

def homeadd(request):
    if(request.user.is_authenticated):
        franitem=Cakeitem.objects.filter(user=request.user)
        return render(request,'homeadd.html',{'fitem':franitem})
    else:
        return HttpResponseRedirect('/homebaker/')

def deletehdata(request, id):
    if request.method == 'POST':
        ditem=Cakeitem.objects.get(pk=id)
        ditem.delete()
        return HttpResponseRedirect('/homeprofile/')

def hlogout(request):
    logout(request)
    return HttpResponseRedirect('/homebaker/')  

def updatehdata(request,id):
    if request.method == 'POST':
        eitem=Cakeitem.objects.get(pk=id)
        hp1=Homepro(request.POST,request.FILES)
        currentuse= Signhome.objects.get(user=request.user)
        if hp1.is_valid():
            br="homemade"
            cn=hp1.cleaned_data['name']
            ci=hp1.cleaned_data['cimg']
            ct=hp1.cleaned_data['category']
            pr500=hp1.cleaned_data['price500']
            pr1=hp1.cleaned_data['price1']
            pr2=hp1.cleaned_data['price2']
            pr3=hp1.cleaned_data['price3']
            de=hp1.cleaned_data['des']
            fup=Cakeitem(id=eitem.id,user=request.user,brand=br,name=cn,cimg=ci,category=ct,price500=pr500,price1=pr1,price2=pr2,price3=pr3,des=de)
            fup.save()
            return HttpResponseRedirect('/homeprofile/')
    else:
        eitem=Cakeitem.objects.filter(pk=id).values('user','brand','name','category','cimg','price500','price1','price2','price3','des')
        hp1=Homepro(eitem[0])
    return render(request, 'homeprofile.html', {'hp1':hp1})