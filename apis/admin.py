from django.contrib import admin
from apis.models import Movie,Genre,Language
# Register your models here.

admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Language)