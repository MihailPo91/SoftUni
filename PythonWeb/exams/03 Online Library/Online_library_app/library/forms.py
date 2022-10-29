from django import forms

from Online_library_app.library.models import Profile, Book


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Last Name',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'URL'
            })
        }


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class DeleteProfileForm(CreateProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
