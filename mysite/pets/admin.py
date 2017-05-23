from django.contrib import admin

from .models import Choice, Pet


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['pet_name']}),
        ('Date information', {'fields': ['when_born'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('pet_name', 'when_born')
    list_filter = ['when_born']
    search_fields = ['pet_name']

admin.site.register(Pet, PetAdmin)