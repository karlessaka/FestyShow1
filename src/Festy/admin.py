from django.contrib import admin
from .metier.model.models import *

# Register your models here.
class AdministratorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_staff', 'is_active')
    ordering = ('username',)

class ArtistAdmin(admin.ModelAdmin):
    list_display = ('Full_name', 'bio', 'style', 'email', 'link')
    search_fields = ('Full_name', 'style')
    list_filter = ('Full_name','style')
    ordering = ('Full_name',)

class ConcertAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_time', 'location', 'artist', 'seats_available')
    search_fields = ('location', 'artist__Full_name', 'title')
    list_filter = ('location',)
    ordering = ('date_time',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('concert', 'user_name',)
    search_fields = ('concert', 'user_name',)
    list_filter = ('booking_date',)
    ordering = ('booking_date',)
    


#Register your models here.
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Concert, ConcertAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Administrator, AdministratorAdmin)
