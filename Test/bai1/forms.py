from django import forms

from .models import Publisher


class FormLogin(forms.Form):
    username = forms.CharField(label='tài khoản', min_length=6, max_length=20,
                               widget=forms.TextInput(attrs={'placeholder': 'Tên dăng nhập'}))
    password = forms.CharField(label='Mật khẩu', min_length=8,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Nhập Mật khẩu'}))
class FormPublisher(forms.ModelForm):
    class Meta:
        model=Publisher
        fields="__all__"
