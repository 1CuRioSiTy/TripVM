from django import forms
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        labels = {
            'username': ('用户名'),
            'email': ('邮箱'),
            'password': ('密码'),
        }