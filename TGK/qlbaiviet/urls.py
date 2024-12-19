from django.urls import path
from .import views
urlpatterns = [
    path ('xembaiviet/<int:idbaiviet>/', views.xembaiviet,name='xembaiviet'),
    path ('dsbaiviet/<int:idchuyenmuc>/',views.dsbaiviet),
    path ('suabaiviet/',views.suabaiviet),
    path ('suabaiviet/<int:pk>/', views.suabaiviet),
]
