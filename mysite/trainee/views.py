from django.shortcuts import render

# Create your views here.
from user.models import MyUser


def listtrainee(req):
        users = MyUser.objects.all()
        context = {}
        context['users'] = users
        return render(req, 'trainee/list.html', context)
  #  return render(req,'trainee/list.html')

def update(req):
    return render(req,'trainee/update.html')
