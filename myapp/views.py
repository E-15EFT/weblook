from http.client import HTTPResponse
from django import http
from django.shortcuts import render

from .models import video
from .forms import video_form
from django.contrib import messages

# from .models import video

# Create your views here.
import random
import time
from agora_token_builder import RtcTokenBuilder
from django.http import JsonResponse



 
  

# Create your views here.
def getToken(request):
    appId = '76598159eca7474a9c50514cc3913b9d'
    appCertificate = "17e1b76f533e4363a5cef8f4498b95a3"
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSeconds = 3600 * 24
    currentTimeStamp = (time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid':uid}, safe=False)

    
def index(request):
    return render(request,'home.html')

def inter(request):
    return render(request,'interface.html')

def font(request):
    return render(request,'landing.html')
def about(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_video = video.objects.filter(Moviesname__icontains=q)
    else:

        all_video=video.objects.all()
    if request.method == "POST":
        form=video_form(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your video is successfully posted, Now click here : ")
    else:
        form=video_form()
    return render(request,'about.html',{"form":form,"all":all_video})

def room(request):
    return render(request,'room.html')

def lobby(request):
    return render(request, 'lobby.html')

def token(request):
    return render(request, 'token.html')

