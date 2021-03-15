from django import forms
from .models import Post, Category

category_choice = Category.objects.all().values_list('name', 'name')
category_choice_list = []
for item in category_choice:
    category_choice_list.append(item)

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'category', 'body')
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type your title'}),
            'author':forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'postCreator', 'type':'hidden'}), # This is the author input. The value is automatically entered useing javascript in the front end and the text box is hidden so that the user can't edit it.,
            # 'author':forms.Select(attrs={'class':'form-control'}), # This is a select field to select users. we cannot use this so we use the text field which is hidden and gives the user value automatically.
            'category':forms.Select(choices = category_choice_list ,attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your blog here'}),            
        }


class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body') # author field is removed because we don't need it
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Type your title'}),
            # 'author':forms.Select(attrs={'class':'form-control'}), # we don't need to edit the author again and again so we don't need author field
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Type your blog here'}),            
        }