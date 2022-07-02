"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

import trainee
from student.views import *
from staff.views import *
from report1.views import *
from user.views import *
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', stdview),
    path('insert/',iti_insert ),
    path('update/',iti_update ),
    path('delete/',iti_delete ),
    path('staff/', staff_view),
    path('resp/', staff_res) ,
    path('upd/', staff_upd),
    path('del/', staff_del),
    path('stdrep/', report_view),
    path('staffrep/', staff_view),
    path('mainrep/', course),
    path('home/', home),
    path('login/',login,name='Login'),
    path('Register/',Register,name='Register'),
    path('trainee/',include('trainee.urls'))
]
