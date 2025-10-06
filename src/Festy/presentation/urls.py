from django.urls import path
from Festy.presentation.views.view_artist import artist_list, artist_create
from Festy.presentation.views.view_booking import booking_list, booking_create, booking_detail, booking_update, booking_delete

urlpatterns = [
    path('list_artist/',artist_list, name='list_artist'),
    path('create_artist/',artist_create, name='create_artist'), 
    path('list_booking/', booking_list, name='list_booking'),
    path('create_booking/', booking_create, name='create_booking'),
    path('detail_booking/<int:booking_id>/', booking_detail, name='detail_booking'),
    path('update_booking/<int:booking_id>/', booking_update, name='update_booking'),
    path('delete_booking/<int:booking_id>/', booking_delete, name='delete_booking'),
]