from django.urls import path, include

from Online_library_app.library import views

urlpatterns = [
    path('', views.show_home_page, name='home'),
    path('add/', views.add_new_book, name='add-book'),
    path('edit/<int:book_id>/', views.edit_book, name='edit-book'),
    path('delete/<int:book_id>/', views.delete_book, name='delete-book'),
    path('details/<int:book_id>/', views.show_book_details, name='book-details'),
    path('profile/', include([
        path('', views.show_profile_details, name='profile-details'),
        path('edit/', views.edit_profile, name='edit-profile'),
        path('delete/', views.delete_profile, name='delete-profile'),
    ])),
]
