from django import forms


class CommentTextForm(forms.Form):
    comment_text = forms.CharField(label='Comment', widget=forms.Textarea)