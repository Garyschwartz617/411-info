from django.shortcuts import render
from .models import Person
from django.http import Http404
# Create your views here.
def homepage(request):
    return render(request,'index.html')

def phone(request,wrd):
    try:
        prs =Person.objects.get(phonenumber = wrd)
        index = {'person': prs}
        return render(request,'phone.html', index)
    except Person.DoesNotExist:
        raise Http404


def name(request,wrd):
    try:
        prs =Person.objects.get(name = wrd)
        index = {'person': prs}
        return render(request,'phone.html', index)
    except Person.DoesNotExist:
        raise Http404
            