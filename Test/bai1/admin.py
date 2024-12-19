from django.contrib import admin
from .models import Book, Publisher, Contributor, BookContributor
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(BookContributor)
# Register your models here.
