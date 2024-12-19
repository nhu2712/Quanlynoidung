from django import forms
from .models import BaiViet, BaiVietChuyenMuc, ChuyenMuc
class BaiVietForm(forms.ModelForm):
    class Meta:
        model = BaiViet
        exclude = ['NguoiTao']
