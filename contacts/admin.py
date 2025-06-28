from django.contrib import admin

from . import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('id','first_name','last_name', 'phone',)
    ordering = ('-id',)
    list_filter = ('created_it',)
    search_fields = ('id', 'first_name', 'last_name')
    list_per_page = 10 
    # list_editable =  ('first_name', 'last_name',)