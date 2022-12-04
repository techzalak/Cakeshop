from django.shortcuts import render

# Create your views here.
def pastries(request):
    return render(request,'pastries.html')