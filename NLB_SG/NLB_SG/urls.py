# 6 make url patterns
from django.contrib import admin
from django.urls import path

from SG_Short_Stories import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name='home'),
    path('books/<int:id>/', views.book_detail, name='book_detail'),
]
