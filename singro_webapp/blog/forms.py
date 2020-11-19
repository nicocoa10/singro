from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        # This is where we define widgets . we pass as attributes the class that will affect the widget
        # the class specified are our own classes , except for the textarea widget , it contains two css and javascript classes that we will later add

        widgets = {
            'title': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent '}),

        }




class CommentForm(forms.ModelForm):


    class Meta():
        model = Comment
        fields = fields = ('author','text')

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent '}),

        }

#Add widgets : Allow us to add widgets of the forms such as buttons ,textarea etc
#goes inside the meta class
#adding widgets will allow us to edit them in css , for example its color , margin , etc