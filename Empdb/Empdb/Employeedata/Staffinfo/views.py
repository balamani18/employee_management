from django.shortcuts import render
from .models import EmpDetails,Salaryinfo
def loademp(request):
    return render(request,"addemp.html")
def loadsal(request):
    return render(request,"addsal.html")
def upemp(request):
    return render(request,"upemp.html")
def upsal(request):
    return render(request,"upsal.html")
def delemp(request):
    return render(request,"delemp.html")
def seremp(request):
    return render(request,"seremp.html")

def getemp(request):
    if request.method =="POST":
        try:
            ename = request.POST['n']
            empid = int(request.POST['i'])
            edept = request.POST['d']
            eexp = int(request.POST['e'])
            ed = EmpDetails(eid=empid,name=ename,dept=edept,exp=eexp)
            ed.save()
            result="Data Saved..."
            return render(request,"addemp.html",{'r':result})
        except:
            result = "Data Not Saved..."
            return render(request,"addemp.html",{'r':result})

def getsal(request):
    if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ebasic = int(request.POST['ba'])
            elop = int(request.POST['el'])
            ebonus = int(request.POST['bo'])
            si = Salaryinfo(eid=empid,basic=ebasic,lop = elop,bonus=ebonus)
            si.save()
            result="Data Saved..."
            return render(request,"addsal.html",{'r':result})
        except:
            result = "Data Not Saved..."
            return render(request,"addsal.html",{'r':result})

def updateemp(request):
   if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            eexp = int(request.POST['e'])
            ed = EmpDetails.objects.get(eid=empid)
            ed.exp = eexp
            ed.save()
            result="Data updated..."
            return render(request,"upemp.html",{'r':result})
        except:
            result = "Invalid Id"
            return render(request,"upemp.html",{'r':result})

def updatesal(request):
   if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ebasic = int(request.POST['ba'])
            si = Salaryinfo.objects.get(eid=empid)
            si.basic = ebasic
            si.save()
            result="Data updated..."
            return render(request,"upsal.html",{'r':result})
        except:
            result = "Invalid Id"
            return render(request,"upsal.html",{'r':result})

def deleteemp(request):
    if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ed = EmpDetails.objects.get(eid=empid)
            ed.delete()
            si = Salaryinfo.objects.get(eid=empid)
            si.delete()
            result="Data Deleted..."
            return render(request,"delemp.html",{'r':result})
        except:
            result = "Invalid Id"
            return render(request,"delemp.html",{'r':result})

def  searchemp(request):
    if request.method =="POST":
        try:
            empid = int(request.POST['i'])
            ed = EmpDetails.objects.get(eid=empid)  
            si = Salaryinfo.objects.get(eid=empid)
            total=si.basic+si.bonus-si.lop
            return render(request,"pro.html",{'ei':ed.eid,'en':ed.name,'ed':ed.dept,'ex':ed.exp,'bas':si.basic,'el':si.lop,'bon':si.bonus,'t':total})
        except:
            result = "Invalid Id"
            return render(request,"seremp.html",{'r':result})

           