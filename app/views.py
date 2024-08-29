from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
#returning string as response By FBV

def string_byfbv(request):
    return HttpResponse('string_byfbv')

#returning string as response By CBV

class StringByCbv(View):
    def get(self,request):
        return HttpResponse('StringByCbv')

def fbvfile(request):
    return render(request,'fbvfile.html')


class CbvFile(View):
    def get(self,request):
        return render(request,'CbvFile.html')


def isbyfbv(request):
    ESFO=StudentMF()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('CReated')
        else:
            return HttpResponse('Invalid')
    return render(request,'isbyfbv.html',d)



class ISByCbv(View):
    def get(self,request):
        ESFO=StudentMF()
        d={'ESFO':ESFO}
        return render(request,'ISByCbv.html',d)
    def post(self,request):
        SFDO=StudentMF(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('CReated')
        else:
            return HttpResponse('Invalid')
    







class HtmlByTV(TemplateView):
    template_name='HtmlByTV.html'

























