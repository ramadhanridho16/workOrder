from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Report

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'w-full py-4 px-6 rounded-xl',
    }))


INPUT_CLASS = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('jam', 'jenis_pekerjaan', 'pengguna', 'pelaksana', 'status', 'keterangan')
        widgets = {
            'jam': forms.DateInput(attrs={
                'type': 'date',
                'class': INPUT_CLASS
            }),
            'pekerjaan': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'pengguna': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'pelaksana': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'status': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'keterangan': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ('jenis_pekerjaan', 'pengguna', 'pelaksana', 'status', 'keterangan')
        widgets = {
            'pekerjaan': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'pengguna': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'pelaksana': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'status': forms.Select(attrs={
                'class': INPUT_CLASS
            }),
            'keterangan': forms.Textarea(attrs={
                'class': INPUT_CLASS
            }),
        }