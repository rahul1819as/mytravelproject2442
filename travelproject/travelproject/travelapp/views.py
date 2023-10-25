from django.shortcuts import render
from.models import Place,Plc
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    obj2=Plc.objects.all()
    return render(request,'index.html',{'result':obj,'result1':obj2})