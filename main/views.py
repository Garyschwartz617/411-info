from django.shortcuts import render
from .models import Person
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def phone(request,wrd):
    prs =Person.objects.get(phonenumber = wrd)
    index = {'person': prs}
    return render(request,'phone.html', index)

def name(request,wrd):
    prs =Person.objects.get(name = wrd)
    index = {'person': prs}
    return render(request,'phone.html', index)    