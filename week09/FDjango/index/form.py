from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    # 密码长度需大于8位
    password = forms.CharField(widget=forms.PasswordInput, min_length=9)
