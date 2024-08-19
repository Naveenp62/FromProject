from django.shortcuts import render

# Create your views here.
def func(request):
    a="HI "+str(request.POST.get('sname'))
    return render(request,'index.html',{'result':a})
def func1(request):
    result=None
    if request.method=="POST":
        a=int(request.POST.get('num'))
        if a%2==0:
            result=True
        else:
            result=False
    return render(request,'home.html',{'res':result})
def func2(request):
    result=None
    if request.method=="POST":
        a=int(request.POST.get('num'))
        if a<=2:
            result=False
        for i in range(2,a):
            if a%i==0:
                result=False
                break
        else:
            result=True
    return render(request,'page.html',{'res':result})
def func3(request):
    if request.method == 'POST':
        a = int(request.POST.get('num1'))
        b = int(request.POST.get('num2'))
        if a>b:
            result=True
        else:
            result=False
                    
        return render(request, 'greatest.html', {'res': result})
    else:
        return render(request, 'greatest.html', {'res': None})