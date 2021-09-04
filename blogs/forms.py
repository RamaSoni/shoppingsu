from django import forms
from .models import Author, Post

class BlogForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content", "status"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the title here..."
            }),
            "content": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the content here..."
            }),
            "status": forms.Select(attrs={
                "class": "form-control"
            }),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["full_name", "hobbe"]
        widgets = {
            "full_name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the full_name here..."
            }),
            "hobbe": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the hobbe here..."
            }),
        }


class AuthorLoginForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control"}))
