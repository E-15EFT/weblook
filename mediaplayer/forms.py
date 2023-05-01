from django import forms

from .models import UploadMovie


class UploadMovieForm(forms.ModelForm):
    class Meta:
        model = UploadMovie
        fields = ["title", "thumbnail", "description", "movie"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "thumbnail": forms.FileInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "movie": forms.FileInput(
                attrs={"class": "form-control", "accept": "video/*"}
            ),
        }
