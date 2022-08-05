from django import forms
from news.models import News
# from news.models import Category

# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150)
#     content = forms.CharField()
#     is_published = forms.BooleanField()
#     category = forms.ModelChoiceField(queryset=Category.objects.all())

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets ={
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        'photo': forms.FileInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'})
        }