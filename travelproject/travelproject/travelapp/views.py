from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    objs=Team.objects.all()
#     return render(request,"home.html")
# def about(request):
    return render(request,"index.html",{'result':obj,'res':objs})

# def addition(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     addi=x+y
#     subt=x-y
#     mult=x*y
#     divi=x/y
#
#     return render(request,"result.html",{'result':addi,'sub':subt,'div':divi,'mul':mult})
