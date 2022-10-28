from django.urls import path, include

from GamesPlayAppExam.gameapp import views

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('profile/', include([
        path('create/', views.create_profile, name='create-profile'),
        path('details/', views.show_profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
    ])),
    path('dashboard/', views.show_dashboard, name='dashboard'),
    path('game/', include([
        path('create/', views.create_game, name='create-game'),
        path('details/<game_id>/', views.show_game_details, name='game-details'),
        path('edit/<game_id>/', views.edit_game, name='edit-game'),
        path('delete/<game_id>/', views.delete_game, name='delete-game'),
    ])),
]
