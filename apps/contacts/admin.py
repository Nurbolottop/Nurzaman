from django.contrib import admin
from apps.contacts import models
# Register your models here.

class ContactFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

################################################################################################################################################################################

class MessagesFilterAdmin(admin.ModelAdmin):
    list_filter = ('name', 'email','phone' )
    list_display = ('name', 'email','phone')
    search_fields = ('name', 'email','phone')

################################################################################################################################################################################

admin.site.register(models.Messages, MessagesFilterAdmin)
admin.site.register(models.Contact, ContactFilterAdmin)
