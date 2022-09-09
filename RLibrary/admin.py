from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ("username", "titleName","pageRead","state")
    list_filter = ("username","titleName")

admin.site.register(Book, BookAdmin)