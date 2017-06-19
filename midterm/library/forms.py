from django import forms
from library.models import Media

class MediaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the media name.")

    class Meta:
        model = Media
        fields = ('title', )
