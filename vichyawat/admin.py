from django.contrib import admin
from vichyawat.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = 'date'
