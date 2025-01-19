from django.contrib import admin
from .models import Entry, EntryType, Response


@admin.register(EntryType)
class EntryTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'friendly_name',
    )
    prepopulated_fields = {'name': ('friendly_name',)}


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'entry_type',
        'create_date',
    )
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    list_display = (
        'entry',
        'author',
        'create_date',
        'approved',
    )
