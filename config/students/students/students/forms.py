
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "name",
            "roll",
            "age",
            "course",
            "email",
            "phone",
        ]

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter student name"
            }),
            "roll": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter roll number"
            }),
            "age": forms.NumberInput(attrs={
                "class": "form-control",
                "min": "1"
            }),
            "course": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter course"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter phone number"
            }),
        }
      
