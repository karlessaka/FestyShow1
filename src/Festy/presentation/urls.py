from django.urls import path
from Festy.presentation.views.view_artist import artist_list, artist_create
from Festy.presentation.views.view_concert import concert_list, concert_create, concert_update, concert_delete

urlpatterns = [
    path('list_artist/',artist_list, name='list_artist'),
    path('create_artist/',artist_create, name='create_artist'),
    path('list_concert/',concert_list, name='list_concert'),
    path('create_concert/',concert_create, name='create_concert'),
    path('update_concert/',concert_update, name='update_concert'),
    path('delete_concert/',concert_delete, name='delete_concert'), 

]