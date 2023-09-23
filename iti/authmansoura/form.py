from django import forms
from .models import Myaccount
from students.models import *


class updateprofile(forms.ModelForm):
    class Meta:
        model = Myaccount
        fields = '__all__'


class Newbookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'returnTime']
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly'}),
            'description': forms.TextInput(attrs={'readonly': 'readonly'}),
            'returnTime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
