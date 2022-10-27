from django.conf import settings
from django.templatetags.static import static
from django.urls import path, include

from my_music_app_exam.music import views

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('album/', include([
        path('add/', views.add_album, name='add-album'),
        path('details/<int:album_id>/', views.show_album_details, name='album-details'),
        path('edit/<int:album_id>/', views.edit_album, name='edit-album'),
        path('delete/<int:album_id>/', views.delete_album, name='delete-album'),
    ])),
    path('profile/', include([
        path('details/', views.show_profile_details, name='profile-details'),
        path('delete/', views.delete_profile, name='delete-profile'),
    ])),
]
