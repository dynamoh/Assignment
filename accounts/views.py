from django.shortcuts import render,redirect
from django.http import Http404
from .models import Profile
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def show_list(request):
    user = request.user
    obj_check = Profile.objects.filter(username=user).first()
    if user.manager == False:
        return render(request,'home.html',{'obj':obj_check,'user':0})
    else:
        return render(request,'home.html',{'obj':obj_check,'user':1})

@login_required
def sort_list(request):
    user = request.user
    obj_check = Profile.objects.filter(username=user).first()
    if user.manager == True:
        sear = request.GET.get("search")
        opt1 = request.GET.get("opt1")
        opt2 = request.GET.get("opt2")
        opt3 = request.GET.get("opt3")
        opt4 = request.GET.get("opt4")
        opt5 = request.GET.get("opt5")
        print(opt1,opt5)
        print(sear)
        list = Profile.objects.all()
        lf=[]
        lf.append(list)
        print(lf,list)

        listf = list.filter(skills__icontains='?')
        k=0

        if opt1!=None:
            list1 = list.filter(skills__icontains=opt1)
            listf = listf|list1
            k=1
        if opt2!=None:
            list2 = list.filter(skills__icontains=opt2)
            listf = listf|list2
            k=1
        if opt3!=None:
            list3 = list.filter(skills__icontains=opt3)
            listf = listf|list3
            k=1
        if opt4!=None:
            list4 = list.filter(skills__icontains=opt4)
            listf = listf|list4
            k=1
        if opt5!=None:
            list5 = list.filter(skills__icontains=opt5)
            listf = listf|list5
            k=1

        if k==0:
            listf = Profile.objects.all()


        if sear==None:
            obj =  listf.filter(username__manager=False).order_by('-projects_count')
        else:
            obj =  listf.filter(username__manager=False).filter(Q(name__icontains = sear)|Q(year_of_study__icontains = sear)|Q(preference__icontains = sear)|Q(skills__icontains = sear)|Q(projects_count__icontains = sear)).order_by('-projects_count')
        return render(request,'list.html',{'obj':obj,'user':1})
    else:
        raise Http404








    #
