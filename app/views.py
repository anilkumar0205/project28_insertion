from django.shortcuts import render

from django.http import HttpResponse

from django.db.models.functions import Length

# Create your views here.

from app.models import *

def display_dept(request):
    DLTO=Dept.objects.all()
    DLTO=Dept.objects.all().order_by('dept_no')
    DLTO=Dept.objects.all().order_by('-dept_no')
    DLTO=Dept.objects.all().order_by(Length('dept_name'))
    DLTO=Dept.objects.all().order_by(Length('dept_name').desc())
    d={'dept': DLTO}
    return render(request,'display_dept.html',d)

def display_emp(request):
    ELTO=Emp.objects.all()
    ELTO=Emp.objects.all().order_by('sal')
    ELTO=Emp.objects.all().order_by('-sal')
    d={'emp' : ELTO}
    return render(request,'display_emp.html',d)


def insert_dept(request):
    dno=int(input('enter deptno'))
    dn=input('enter the name')
    DO=Dept.objects.get_or_create(dept_no=dno,dept_name=dn)[0]
    DO.save()
    return HttpResponse('the dept is added')

def insert_emp(request):
    dn=int(input('enter dept no'))
    DO=Dept.objects.get(dept_no=dn)
    eno=int(input('enter emp no'))
    en=input('enter the ename')
    
    s=int(input('enter the sal'))
    e=input('enter email')
    j=input('enter the job')
    dno=Emp.objects.get_or_create(dept_no=DO,ename=en,emp_no=eno,sal=s,email=e,job=j)[0]
    dno.save()
    return HttpResponse('employee information is inserted')