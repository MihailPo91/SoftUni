from django import forms

from GamesPlayAppExam.gameapp.models import Profile, Game


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['email', 'age', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class GameCreateForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'category': forms.Select(choices=Game.GAME_CATEGORIES),
            'rating': forms.NumberInput()
        }


class GameEditForm(GameCreateForm):
    class Meta:
        model = Game
        fields = '__all__'
        widgets = {
            'category': forms.Select(choices=Game.GAME_CATEGORIES),
            'rating': forms.NumberInput()
        }


class GameDeleteForm(GameEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(ProfileEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
