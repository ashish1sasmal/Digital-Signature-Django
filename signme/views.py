from django.shortcuts import render,redirect
from base64 import b64decode
from .models import *
from django.core.files.base import ContentFile
from django.http import HttpResponse
import base64


def home(request):

    if request.method == "POST":


        image_b64 = request.POST.get('canva') # This is your base64 string image
        format, imgstr = image_b64.split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=request.POST.get('username')+'.' + ext)
        # print(data)
        # data_uri = data
        #
        # header, encoded = data_uri.split(",", 1)
        # data = b64decode(encoded)
        # print(request.FILES.get('file'))
        print(data)
        d = Signuser(username=request.POST.get('username'),stamp=data)
        d.save()

        # with open("media/"+request.POST.get('username')+".jpg", "wb") as f:
        #     f.write(data)
        print('image save')
        loc=str(d.stamp)
        return render(request,'signme/index.html',{"loc":loc})
    else:
        return render(request,'signme/home.html')
