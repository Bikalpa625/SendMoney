from django.urls import path,include
from sendmoney import views as sendmoneyview
from . import views

urlpatterns = [
    path('', sendmoneyview.homepage, name='sendmoney-homepage'),
    
    
]
