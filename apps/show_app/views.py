
from django.shortcuts import render, HttpResponse, redirect
from .models import Show
from django.contrib import messages

def index(request):
    context = {
    	"shows": Show.objects.all()
    }
    return render(request, "show_app/index.html",context)


def add(request):
    context = {
    	"shows": Show.objects.all()
    }
    return render(request, "show_app/add.html", context)

def add_process(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    #######################
    else:
        # request.method == "POST":
        tit = request.POST["s_tit"]
        net = request.POST["s_net"]
        rel = request.POST["s_rel"]
        funde = request.POST["s_des"]
        #######################
        # check to make sure to get information
        print(request.POST)
        ############send info to DB##########################
        new = Show.objects.create(title=tit, network=net, release_date=rel, desc=funde)
        ##### get last info from DB #############
        send = Show.objects.last()
        return redirect(f'/shows/{send.id}')
        #how to send info to 
     

def show(request,idr):
    context = {
    	"shows": Show.objects.get(id=idr),
    }
    return render(request, "show_app/show.html", context)

def edit(request,idr):
    context = {
        "shows": Show.objects.get(id=idr),
    }
    return render(request, "show_app/edit.html", context)

def edit_process(request,idr):
    errors = Show.objects.basic_validator(request.POST)
    print("*"*80)
    print(errors)
    print("*"*80)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{idr}/edit')
    else:
        tit = request.POST["s_tit"]
        net = request.POST["s_net"]
        rel = request.POST["s_rel"]
        funde = request.POST["s_des"]
        idd = request.POST["whatever"]
        print(request.POST)
        ####### need to update ########
        easy=Show.objects.get(id=idd)
        easy.title = tit
        easy.save()
        easy.network = net
        easy.save()
        easy.release_date = rel
        easy.save()
        easy.desc = funde
        easy.save()
        # easy.title = tit
        # easy.save()
        return redirect(f'/shows/{easy.id}')

def delete(reqest,idr):
    instance = Show.objects.get(id=idr)
    instance.delete()
    return redirect("/shows")