from django.contrib import admin

from .models import BaiViet, BaiVietChuyenMuc, ChuyenMuc

# Register your models here.
admin.site.register(BaiViet)
admin.site.register(BaiVietChuyenMuc)
admin.site.register(ChuyenMuc)

