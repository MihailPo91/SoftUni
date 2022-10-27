from django.shortcuts import render, redirect

from my_music_app_exam.music.forms import ProfileForm, AlbumForm, AlbumEditForm, AlbumDeleteForm
from my_music_app_exam.music.models import Profile, Album


def show_home_page(request):
    profile = Profile.objects.all().first()
    if profile:
        all_albums = Album.objects.all()
        context = {
            'all_albums': all_albums,
            'profile': profile
        }
        return render(request, template_name='home-with-profile.html', context=context)
    else:
        if request.method == 'GET':
            form = ProfileForm()
        else:
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {
            'form': form
        }
        return render(request, template_name='home-no-profile.html', context=context)


def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name='add-album.html', context=context)


def show_album_details(request, album_id):
    album = Album.objects.get(id=album_id)
    context = {
        'album': album
    }
    return render(request, template_name='album-details.html', context=context)


def edit_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'GET':
        form = AlbumEditForm(instance=album, initial=album.__dict__)
    else:
        form = AlbumEditForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name='edit-album.html', context=context)


def delete_album(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'GET':
        form = AlbumDeleteForm(instance=album, initial=album.__dict__)
    else:
        album.delete()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name='delete-album.html', context=context)


def show_profile_details(request):
    profile = Profile.objects.all().first()
    all_albums = Album.objects.all()
    context = {
        'profile': profile,
        'all_albums': all_albums,
    }
    return render(request, template_name='profile-details.html', context=context)


def delete_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'POST':
        profile.delete()
        return redirect('home')
    return render(request, template_name='profile-delete.html')
