from django.urls import path

from .views import homepage,phone,name,frm

urlpatterns = [
    
    path('', homepage),
    path('phone/<str:wrd>', phone,name='phone'),
    path('name/<str:wrd>', name,name='name'),
    path('forms', frm)
   
    
]