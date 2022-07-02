from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
def staff_view(request):
    return HttpResponse("Hello World")
def staff_res(r):
    return JsonResponse({'name':'Mohamed'})
def staff_upd(r):
    return JsonResponse({'name':'Ahmed'})
def staff_del(req):
    return HttpResponseRedirect('/staff')
