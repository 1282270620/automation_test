from django.shortcuts import render,HttpResponse

# Create your views here.
import datetime
from blog import models

def cur_time(request):
    times = datetime.datetime.now()
    return render(request, "cur_time.html",{"abc":times})

def userinfo(req):
    if req.method=="POST":
        u = req.POST.get("username",None)
        s = req.POST.get("sex",None)
        e = req.POST.get("email",None)
        #user={"username":username,"sex":sex,"email":email}
        #user_list.append(user)
        #models.UserInfo.objects.create(username = u,sex = s,email = e,)
    return render(req,"index.html")
