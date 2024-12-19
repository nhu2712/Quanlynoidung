from django.contrib import admin
from django.urls import path
from home import views as home
from admin_custom import views as admin_custom
from django.contrib.auth.decorators import login_required, user_passes_test
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('admin_dashboard/', admin_custom.admin_dashboard, name='admin_dashboard'), 
    path('admin_dashboard/customers', admin_custom.admin_customer), 
    path('admin_dashboard/employees', admin_custom.admin_employee), 
    path('admin_dashboard/rooms', admin_custom.admin_room, name='admin_room'), 
    path('admin_dashboard/services', admin_custom.admin_service), 
    path('admin_dashboard/posts', admin_custom.admin_post), 
    path('room/edit/<int:room_id>/', admin_custom.edit_room, name='edit_room'),
    path('room/delete/<int:room_id>/', admin_custom.delete_room, name='delete_room'),

    path('', home.get_home, name='home'),
    path('contact', home.get_contact),
    path('about', home.get_about),
    path('event', home.get_event),
    path('room', home.get_room),
    path('room/<int:room_id>/', home.room_detail, name='room_detail'),  

    path('login/', home.user_login, name='login'),
    path('register/', home.user_register, name='register'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)