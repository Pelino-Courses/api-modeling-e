from django.contrib import admin
from .models import *

admin.site.register(category) 
@admin.register(event_managment)
class event_managmentAdmin(admin.ModelAdmin):
    list_display = ('title','start_date', 'end_date', 'category')
    list_filter = ('title', 'location', 'category')
    search_fields = ('title', 'description')
    
@admin.register(speaker_management) 
class speaker_managemenAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'phone_number','linkedin', 'twitter')
    list_filter = ('name','email_address', 'phone_number')
    search_fields = ('name', 'email_address')
    
@admin.register(participant_management) 
class participant_managementAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_address', 'phone_number')
    list_filter = ('name', 'events_attending')
    search_fields = ('name', 'events_attending')
@admin.register(schedule_management) 
class schedule_management(admin.ModelAdmin):
    list_display =('event_managment', 'start_time', 'end_time', 'topic', 'speaker_management')
    list_filter = ('event_managment', 'topic')
    search_fields = ('topic', 'speaker_managment')
    
@admin.register(event_payment)
class event_payment(admin.ModelAdmin):
    list_display = ('participant_management', 'event_managment', 'amount_paid', 'payment_method', 'payment_status')
    list_filter = ('amount_paid', 'payment_date', 'payment_status')
    search_fields = ('participant_management', 'event_managment')