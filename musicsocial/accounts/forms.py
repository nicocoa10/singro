from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets
from django import forms

from django.utils.safestring import mark_safe


# class HorizRadioRenderer(forms.RadioSelect.renderer):
#     """ this overrides widget method to put radio buttons horizontally
#         instead of vertically.
#     """

#     def render(self):
#         """Outputs radios"""
#         return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


GENRE_CHOICES = [
    ('edm', 'Dance/EDM'),
    ('rock', 'Rock'),
    ('pop', 'Pop'),
    ('hiphop', 'Hip Hop'),
]


class UserCreateForm(UserCreationForm):
    # THIS HELPS WITH CHANGING THE ATTRIBUTES LIKE CLASS
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}), help_text='Letters, digits and @/./+/-/_ only.')

    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))

    favorite_genre = forms.CharField(widget=forms.RadioSelect(choices=GENRE_CHOICES, attrs={
                                     'class': 'custom-radio-list '}))

    password1 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'type': 'password', }), help_text='<ul><li>Your password can’t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can’t be a commonly used password.</li><li>Your password can’t be entirely numeric.</li></ul>')
    password2 = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', 'type': 'password'}), help_text='Enter the same password as before, for verification.')

    class Meta:
        fields = ('username', 'email',
                  'password1', 'password2', 'favorite_genre')
        model = get_user_model()

    # setting labels for the fields above (like next to the label)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ''
        self.fields['email'].label = ''
        self.fields['password1'].label = ''
        self.fields['password2'].label = ''
        self.fields['favorite_genre'].label = 'Pick your identifying genre: '
