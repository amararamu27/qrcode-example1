from django.shortcuts import render,redirect
import qrcode as image


def openQrcode(request):
    return render(request,'qrcode_text.html')


def createQRImage(request):
    text = request.POST.get('t1')
    image.make(text).save(r'app1/static/images/qrcode1.jpg')
    if text == None:
        return render(request,'direct.html')
    else:
        return render(request,'welcome.html')
