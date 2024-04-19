from django.urls import path,include
from sendmoney import views as sendmoneyview

urlpatterns = [
    path('', sendmoneyview.homepage, name='sendmoney-homepage'),
  

]
