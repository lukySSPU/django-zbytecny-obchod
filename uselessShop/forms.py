from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'] = forms.CharField(widget=forms.HiddenInput(), initial=user.username)
        else:
            self.fields['username'] = forms.CharField(max_length=30)
