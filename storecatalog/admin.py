from django.contrib import admin
from .models import Book, Genre , Publisher

# registering the class models
admin.site.register(Book)
admin.site.register(Genre) 
admin.site.register(Publisher)
