from django.contrib import admin
from django.urls import path
from django.urls import re_path
from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    re_path('^adoptions/(\d+)/',views.pet_detail,name='pet_detail'),
]
