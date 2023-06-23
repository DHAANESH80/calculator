from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request,'home.html')

def simple(request):
    p= float(request.POST["num1"])
    r= (float(request.POST["num2"]))/100
    t= float(request.POST["num3"])
    res1 = round(p*r*t,2)
    return render(request,"home.html",{"result1":res1})

def compund(request):
    p= float(request.POST["num1"])
    r= (float(request.POST["num2"]))/100
    t= float(request.POST["num3"])
    res0 = p*(pow((1+r),t))
    res2=round(res0-p,2)
    return render(request,"home.html",{"result2":res2})

def sip(request):
    p= float(request.POST["num1"])
    r= (float(request.POST["num2"]))/12
    r1=r/100
    t= float(request.POST["num3"])
    res3 = round(p*(((1+r1)**t -1)/r1)*(1+r1),2)
    return render(request,"home.html",{"result3":res3})

def Lumpsum(request):
    p= float(request.POST["num1"])
    r= (float(request.POST["num2"]))/100
    t= float(request.POST["num3"])
    res4= round(p*(pow((1+r),t)),2)
    return render(request,"home.html",{"result4":res4})

def fd(request):
    p= float(request.POST["num1"])
    r= (float(request.POST["num2"]))/100
    t= float(request.POST["num3"])
    res5= round(p*((1+r)**t),2)
    return render(request,"home.html",{"result5":res5})

def cagr(request):
    i= float(request.POST["num1"])
    f= float(request.POST["num2"])
    t= float(request.POST["num3"])
    res= ((f/i)**(1/t))-1
    res6=round(res*100,2)
    return render(request,"home.html",{"result6":res6})






