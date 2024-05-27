from django.shortcuts import render
from .forms import Register
# Create your views here.
def register(request):
    form=Register()
    data={'form':form}
    return render(request,'form.html',context=data)
