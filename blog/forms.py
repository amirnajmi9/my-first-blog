from django import forms

from .models import post

class PostForm(forms.ModelForm):

    class Meta:
        model = post
        fields = ('title', 'body','image','user','daste')
class codeform(forms.Form):
	number = forms.CharField(max_length = 5 )
