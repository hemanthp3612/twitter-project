from django import forms

from .models import Tweet


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
    def clean_content(self):
        MAX_TWEET_LENGTH = 240
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.validationError("This tweet is too long")
        return content
