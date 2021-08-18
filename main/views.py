from django.shortcuts import render,redirect
from .models import Person
from django.http import Http404
from .forms import *
from phonenumber_field.formfields import PhoneNumberField
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

def frm(request):
    if request.method == 'GET':
        form1 = NumberForm()
        form2 = NameForm()
       
        
    elif request.method == 'POST':
        form1 = NumberForm(request.POST)
        form2 = NameForm(request.POST)
        
        if form1.is_valid():
            f = form1.cleaned_data
            f = f['phonenumber']
            return redirect('phone', wrd=f)
        elif form2.is_valid():
            f = form2.cleaned_data
            f = f['name']
            print(f)
            return redirect(f'name',wrd=f)    
    return render(request, 'todo.html', {'form1':form1,'form2': form2})
        
            