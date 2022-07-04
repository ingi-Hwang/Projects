from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
#
def Home(request):
    return render(request, 'community/home.html')


def Date(request):
    if request.method == 'POST':
        #db 저장할때
        user = Input()
        user.startperiod = request.POST['date']  # input에 name으로 받아야 값을 받을수 있음
        user.endperiod = request.POST['date2']
        user.startime = request.POST['time']

        user.area = request.POST['local']

        user.save() #데이터에 저장
        print("성공")


        return render(request, 'community/date.html',{'data':user})

    else:
        user = Users.objects.all()

        return render(request, 'community/date.html',{'data':user})