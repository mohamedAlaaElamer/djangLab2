from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
def stdview(request):
    return HttpResponse("Hello World")
def iti_insert(req):
    return render(req,'iti/insert.html')
def iti_update(req):
    return render(req,'iti/update.html')
def iti_delete(req):
    return HttpResponseRedirect('/student')
def home(req):
    return render(req,'index.html')