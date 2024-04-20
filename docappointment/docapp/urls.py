from django.contrib import admin
from django.urls import path
from django.urls import path,include
from docappointment import settings
from django.conf.urls.static import static
from . import views
app_name='docapp'

urlpatterns = [
    

    path('api/add_doctors', views.add_doctors,name='add_doctors'),
    path('api/getdoctors', views.getdoctors,name='getdoctors'),
    path('api/checkdocavailability/<int:id>', views.checkdocavailability,name='checkdocavailability'),
    path('api/getdocdetail/<int:id>', views.getdocdetail,name='getdocdetail'),
    path('api/Bookappointment/', views.Bookappointment,name='Bookappointment'),

]