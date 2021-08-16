from django.urls import path

from .views import homepage,phone,name

urlpatterns = [
    
    path('', homepage),
    path('phone/<str:wrd>', phone),
    path('name/<str:wrd>', name),
   
    
]