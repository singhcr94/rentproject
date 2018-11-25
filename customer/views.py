from django.shortcuts import render,redirect
from customer import models
from .forms import postform,postmovie
from .models import info,person
from django.db.models.functions import Lower
from django.template import RequestContext
def home(request):
    return render(request,'table.html')
def addc(request):
    form = postform(request.POST)
    if request.method=='POST':
        if form.is_valid():
            form.save(commit=True)
            return redirect('http://127.0.0.1:8000/addmovies')
    form=postform()
    return render(request,'add.html',{'form':form})
def addm(request):
    form2 = postmovie(request.POST)
    if request.method=='POST':
        if form2.is_valid():
            form2.save(commit=True)
            return redirect('http://127.0.0.1:8000/availables')
    form2=postmovie()
    return render(request,'addmovie.html',{'form2':form2})
def assignm(request):
    if request.method=='POST':
        formresult=request.POST
        print(request.body)
        formvalues=list(formresult.values())
        print(formvalues)
        form4=person.objects.get(firstname__in=formvalues).id
        print(form4)
        movie=info.objects.filter(moviename=formvalues[2]).update(rentby=form4)
        return redirect('http://127.0.0.1:8000/availables')
    result = info.objects.filter(rentby__isnull=True)
    result2 = person.objects.all()
    return render(request,'assignmovie.html',{'k':result,'kp':result2})
def availablem(request):
    a=info.objects.filter(rentby__isnull=True).order_by(Lower("moviename"))
    return render(request,'available.html',{'k':a})
def rentedm(request):
    column1= info.objects.filter(rentby__isnull=False)
    print(column1)
    x=info.objects.values_list('rentby',flat=True).filter(rentby__isnull=False)
    if request.method=="POST":
        formresult=request.POST
        print(formresult)
        value=list(formresult.values())
        print(value)
        update=info.objects.filter(moviename__in=value).update(rentby='')
        return redirect('http://127.0.0.1:8000/availables')
    m=info.objects.filter(rentby_id__in=x).order_by(Lower("moviename"))
    persons=person.objects.filter(id__in=x)
    movie=zip(list(m),list(persons))
    return render(request,'rented.html',{'m':m})
def removem(request):
    if request.method=="POST":
        formresult=request.POST
        values=list(formresult.values())
        update=info.objects.filter(moviename__in=values).delete()
        return redirect('http://127.0.0.1:8000/availables')
    movies=info.objects.all().order_by(Lower("moviename"))
    return render(request,'removemovie.html',{'movies':movies})
def removec(request):
    if request.method=="POST":
        formresult=request.POST
        values=list(formresult.values())
        update=person.objects.filter(firstname__in=values).delete()
        return redirect('http://127.0.0.1:8000/home')
    persons=person.objects.all().order_by(Lower("firstname"))
    return render(request,'remove.html',{'persons':persons})
def edit(request):
    form1=request.POST
    values=form1.values()
    form2=person.objects.get(firstname__in=values)
    print(form2)
    form4 = postform(request.POST,instance=form2)
    form=postform(instance=form2)
    if form4.is_valid():
        form4.save(commit=True)
        return redirect('http://127.0.0.1:8000/removes')
    return render(request, 'edits.html', {'form':form})
