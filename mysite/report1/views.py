from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.
def report_view(request):
    return HttpResponse("list students")
def staff_view(request):
    return HttpResponse("list staff")
def course(request):
    response = HttpResponse('click bellow to view main report')
    response.write('</br><a href="#">main report</a>')
    return response