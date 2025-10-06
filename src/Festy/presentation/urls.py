from django.urls import path
from Festy.presentation.views.view_artist import artist_list, artist_create, artist_detail, artist_update, artist_delete

urlpatterns = [
    path('list_artist/',artist_list, name='list_artist'),
    path('create_artist/',artist_create, name='create_artist'), 
    path('detail_artist/<int:artist_id>/', artist_detail, name='detail_artist'),
    path('update_artist/<int:artist_id>/', artist_update, name='update_artist'),
    path('artist_delete/<int:artist_id>/', artist_delete, name='delete_artist'), 
]