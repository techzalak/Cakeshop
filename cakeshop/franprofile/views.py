from django.shortcuts import render,HttpResponseRedirect
from .forms import Franchisepro
from homepage.models import Cakeitem,SignFranchise,Signhome
from django.contrib.auth import login,logout,authenticate
# Create your views here.
def fadd(request):
    if(request.user.is_authenticated):
        franitem=Cakeitem.objects.filter(user=request.user)
        return render(request,'franadd.html',{'fitem':franitem})
    else:
        return HttpResponseRedirect('/franchise/')


def frandata(request): 
    if(request.user.is_authenticated):
        if(request.method=='POST'):
            fp1=Franchisepro(request.POST,request.FILES, prefix="fp1")
            currentuse= SignFranchise.objects.get(user=request.user) 
            if(fp1.is_valid()):
                br=currentuse.brand
                cn=fp1.cleaned_data['name']
                ci=fp1.cleaned_data['cimg']
                ct=fp1.cleaned_data['category']
                pr500=fp1.cleaned_data['price500']
                pr1=fp1.cleaned_data['price1']
                pr2=fp1.cleaned_data['price2']
                pr3=fp1.cleaned_data['price3']
                de=fp1.cleaned_data['des']
                frreg=Cakeitem(user=request.user,brand=br,name=cn,cimg=ci,category=ct,price500=pr500,price1=pr1,price2=pr2,price3=pr3,des=de)
                frreg.save()
                return HttpResponseRedirect('/franprofile/')
        else:
            fp1 = Franchisepro(prefix="fp1")
        return render(request,'franprofile.html', {'fp1': fp1})
    else:
        return HttpResponseRedirect('/franchise/')
            
       
    #return render(request,'franprofile.html')
#To update item
def updatefdata(request,id):
    if request.method == 'POST':
        eitem=Cakeitem.objects.get(pk=id)
        fp1=Franchisepro(request.POST,request.FILES)
        currentuse= SignFranchise.objects.get(user=request.user) 
        if fp1.is_valid():
            br=currentuse.brand
            cn=fp1.cleaned_data['name']
            ci=fp1.cleaned_data['cimg']
            ct=fp1.cleaned_data['category']
            pr500=fp1.cleaned_data['price500']
            pr1=fp1.cleaned_data['price1']
            pr2=fp1.cleaned_data['price2']
            pr3=fp1.cleaned_data['price3']
            de=fp1.cleaned_data['des']
            fup=Cakeitem(id=eitem.id,user=request.user,brand=br,name=cn,cimg=ci,category=ct,price500=pr500,price1=pr1,price2=pr2,price3=pr3,des=de)
            fup.save()
            return HttpResponseRedirect('/franprofile/')
    else:
        eitem=Cakeitem.objects.filter(pk=id).values('user','brand','name','category','cimg','price500','price1','price2','price3','des')
        fp1=Franchisepro(eitem[0])
    return render(request, 'franprofile.html', {'fp1':fp1})

#To delete items
def deletefdata(request, id):
    if request.method == 'POST':
        ditem=Cakeitem.objects.get(pk=id)
        ditem.delete()
        return HttpResponseRedirect('/franprofile/')

#Logout

def flogout(request):
    logout(request)
    return HttpResponseRedirect('/franchise/')