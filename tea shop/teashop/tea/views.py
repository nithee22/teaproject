from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import tea 


def home(request):
    Tea=tea.objects.all()
    for t in Tea:
        print(t)
    return render(request,'home.html',{'tea':Tea})
