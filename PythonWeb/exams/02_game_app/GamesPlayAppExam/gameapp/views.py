from django.shortcuts import render, redirect

from GamesPlayAppExam.gameapp.forms import ProfileForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from GamesPlayAppExam.gameapp.models import Profile, Game


def show_home_page(request):
    profile = Profile.objects.all().first()
    context = {
        'profile': profile
    }
    return render(request, 'home-page.html', context=context)


def create_profile(request):
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
    return render(request, 'create-profile.html', context=context)


def show_profile_details(request):
    profile = Profile.objects.all().first()
    all_games = Game.objects.all()
    try:
        average_rating = sum([game.rating for game in all_games]) / len(all_games)
    except ZeroDivisionError:
        average_rating = 0
    context = {
        'profile': profile,
        'all_games': all_games,
        'average_rating': average_rating,
    }
    return render(request, 'details-profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile, initial=profile.__dict__)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'form': form,
        'profile': profile
    }
    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.all().first()
    all_games = Game.objects.all()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile, initial=profile.__dict__)
    else:
        all_games.delete()
        profile.delete()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'delete-profile.html', context=context)


def show_dashboard(request):
    all_games = Game.objects.all()
    profile = Profile.objects.all().first()
    context = {
        'all_games': all_games,
        'profile': profile
    }
    return render(request, 'dashboard.html', context=context)


def create_game(request):
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'create-game.html', context=context)


def show_game_details(request, game_id):
    game = Game.objects.get(id=game_id)
    context = {
        'game': game
    }
    return render(request, 'details-game.html', context=context)


def edit_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'GET':
        form = GameEditForm(instance=game, initial=game.__dict__)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'edit-game.html', context=context)


def delete_game(request, game_id):
    game = Game.objects.get(id=game_id)
    if request.method == 'GET':
        form = GameDeleteForm(instance=game, initial=game.__dict__)
    else:
        game.delete()
        return redirect('dashboard')
    context = {
        'form': form
    }
    return render(request, 'delete-game.html', context=context)

