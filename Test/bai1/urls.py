from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('sanpham/',views.sanpham),
    path('chungtoi/',views.chungtoi),
    path('sanpham/<int:book_id>/',views.bookdetail),
    path('dangnhap/',views.login),
    path('publisher/new/',views.publishernew),
    path('publisher/<int:publisher_id>/',views.publisheredit),
]