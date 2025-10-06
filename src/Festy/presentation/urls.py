from django.urls import path
from Festy.presentation.views.view_artist import artist_list, artist_create
from Festy.presentation.views.view_concert import concert_list, concert_create, concert_update, concert_delete, concert_detail
from Festy.presentation.views.view_artist import artist_list, artist_create, artist_detail, artist_update, artist_delete

urlpatterns = [
    #artist urls
    path('list_artist/',artist_list, name='list_artist'),
    path('create_artist/',artist_create, name='create_artist'),
    path('detail_artist/<int:artist_id>/', artist_detail, name='detail_artist'),
    path('update_artist/<int:artist_id>/', artist_update, name='update_artist'),
    path('artist_delete/<int:artist_id>/', artist_delete, name='delete_artist'), 


    #concert urls
    path('list_concert/',concert_list, name='list_concert'),
    path('create_concert/',concert_create, name='create_concert'),
    path('detail_concert/<int:concert_id>/', concert_detail, name='detail_concert'),
    path('update_concert/',concert_update, name='update_concert'),
    path('delete_concert/',concert_delete, name='delete_concert'), 


]