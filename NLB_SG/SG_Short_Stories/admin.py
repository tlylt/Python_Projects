# 3 after loading csv, make admin
# 4 make superuser by createsuperuser
# 5 make admin page more informative

from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'language', 'download_link']
