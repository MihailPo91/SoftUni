from django.shortcuts import render, redirect

from Online_library_app.library.forms import CreateProfileForm, CreateBookForm, DeleteProfileForm
from Online_library_app.library.models import Profile, Book


def show_home_page(request):
    profile = Profile.objects.all().first()

    if profile:

        all_books = Book.objects.all()
        context = {
            'all_books': all_books,
            'profile': profile
        }
        return render(request, 'home-with-profile.html', context=context)
    else:
        if request.method == 'GET':
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context=context)


def add_new_book(request):
    if request.method == 'GET':
        form = CreateBookForm()
    else:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'add-book.html', context=context)


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'GET':
        form = CreateBookForm(instance=book, initial=book.__dict__)
    else:
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form': form
    }
    return render(request, 'edit-book.html', context=context)


def show_book_details(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'book-details.html', context=context)


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request, 'delete_book.html')


def show_profile_details(request):
    profile = Profile.objects.all().first()
    context = {
        'profile': profile
    }
    return render(request, 'profile.html', context=context)


def edit_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'GET':
        form = CreateProfileForm(instance=profile, initial=profile.__dict__)
    else:
        form = CreateProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    context = {
        'form': form
    }
    return render(request, 'edit-profile.html', context=context)


def delete_profile(request):
    profile = Profile.objects.all().first()
    if request.method == 'GET':
        form = DeleteProfileForm(instance=profile, initial=profile.__dict__)
    else:
        profile.delete()
        return redirect('home')
    context = {
        'form': form
    }
    return render(request, template_name='delete-profile.html', context=context)
