from django import forms
from news.models import News
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Ваше сообщение',
                               widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10}))
    captcha = CaptchaField(label='Введите текст с картинки')





class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        # 'username': forms.TextInput(attrs={'class': 'form-control'}),
        # 'email': forms.EmailInput(attrs={'class': 'form-control'}),
        # 'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        # 'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }




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
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control'}),
        'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        'photo': forms.FileInput(attrs={'class': 'form-control'}),
        'category': forms.Select(attrs={'class': 'form-control'})
        }