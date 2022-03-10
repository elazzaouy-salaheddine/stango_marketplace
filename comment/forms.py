from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    body = forms.CharField(widget= forms.Textarea
                           (attrs={'placeholder':'Enter your review'}))
    custemer_email = forms.EmailField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter Email'}))
    custemer_name = forms.CharField(widget= forms.TextInput
                           (attrs={'placeholder':'Enter your name'}))
    class Meta:
        model = Comment
        exclude = ['is_active','review']