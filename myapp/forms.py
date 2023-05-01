from django import forms
from .models import video

class video_form(forms.ModelForm):
    class Meta:
        model=video
        fields=('Moviesname','video')