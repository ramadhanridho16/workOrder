from django import forms

from .models import Report

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