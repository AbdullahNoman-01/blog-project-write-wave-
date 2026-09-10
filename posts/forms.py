from django import forms
from .import models
class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'content', 'image', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Write your comment...",
                    "rows": 4,
                }
            )
        }