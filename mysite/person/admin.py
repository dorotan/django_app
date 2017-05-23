from django.contrib import admin
from .models import Person


class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['first_name']}),
        ('Date information', {'fields': ['last_name'], 'classes': ['collapse']}),
    ]

admin.site.register(Person, PersonAdmin)
