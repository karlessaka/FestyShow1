from django.urls import path
from Festy.presentation.views.view_artist import artist_list, artist_create

urlpatterns = [
    path('list_artist/',artist_list, name='list_artist'),
    path('create_artist/',artist_create, name='create_artist'), 
]