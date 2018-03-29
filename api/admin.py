from django.contrib import admin
from django.utils.translation import ugettext as _
from .models import (
    Film,
    Person
)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    pass

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass
