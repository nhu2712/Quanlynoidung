from django.contrib import auth
from django.db import models
from pkg_resources import require

class ChuyenMuc(models.Model):
    Ten=models.CharField(max_length=200)
    def __str__(self):
        return self.Ten
class BaiViet(models.Model):
    TieuDe = models.CharField(max_length=250)
    NoiDung=models.TextField(null=True, blank =True)
    NgayTao=models.DateField()
    NguoiTao= models.ForeignKey(auth.get_user_model(),
        on_delete=models.CASCADE)
    ChuyenMuc=models.ManyToManyField(ChuyenMuc,through='BaiVietChuyenMuc')
    def __str__(self):
        return self.TieuDe
class BaiVietChuyenMuc(models.Model):
    ThuTu=models.IntegerField()
    BaiViet=models.ForeignKey(BaiViet,on_delete=models.CASCADE)
    ChuyenMuc=models.ForeignKey(ChuyenMuc,on_delete=models.CASCADE)
    def __str__(self):
        return self.ThuTu



# Create your models here.
