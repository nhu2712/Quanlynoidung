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
    path('admin_dashboard/users-profile.html',
         admin_custom.profile, name='profile'),
    path('admin_dashboard/employees',
         admin_custom.admin_employee, name='manage_employees'),
    path('admin_dashboard/employees/add/',
         admin_custom.create_employee, name='add_employee'),
    path('admin_dashboard/rooms', admin_custom.admin_room, name='admin_room'),
    path('admin_dashboard/services',
         admin_custom.admin_service, name='admin_service'),
    path('admin_dashboard/services/delete/<int:service_id>/',
         admin_custom.delete_service, name='delete_service'),
    path('admin_dashboard/services/edit_service/<int:service_id>/',
         admin_custom.edit_service, name='edit_service'),
    path('admin_dashboard/gifts', admin_custom.admin_gift, name='admin_gift'),
    path('admin_dashboard/gifts/delete/<int:gift_id>/',
         admin_custom.delete_gift, name='delete_gift'),
    path('admin_dashboard/gifts/edit_gift/<int:gift_id>/',
         admin_custom.edit_gift, name='edit_gift'),
    path('admin_dashboard/posts', admin_custom.admin_post, name='admin_post'),
    path('admin_dashboard/posts/delete/<int:post_id>/',
         admin_custom.delete_post, name='delete_post'),
    path('admin_dashboard/posts/edit_post/<int:post_id>/',
         admin_custom.edit_post, name='edit_post'),
    path('admin_dashboard/posts/aprrove/<int:post_id>/',
         admin_custom.approve_post, name='approve_post'),

    path('room/edit/<int:room_id>/', admin_custom.edit_room, name='edit_room'),
    path('room/delete/<int:room_id>/',
         admin_custom.delete_room, name='delete_room'),

    path('', home.get_home, name='home'),
    path('service', home.get_service, name='service'),
    path('about', home.get_about, name='about'),
    path('event', home.get_event, name='event'),
    path('event/<int:id>/', home.event_detail, name='event_detail'),
    path('gift', home.get_gift, name='gift'),
    # path('room/suite', home.get_room_suite, name='room_list_suite'),
    # path('room/deluxe', home.get_room_deluxe, name='room_list_deluxe'),
    path('room', home.get_room, name='room_list'),
    path('room/<int:room_id>/', home.room_detail, name='room_detail'),
    path('login/', home.user_login, name='login'),
    path('register/', home.user_register, name='register'),
    path('add-comment/', home.add_comment, name='add_comment'),
    path('room/<str:room_type>/', home.rooms_by_type, name='rooms_by_type'),
    path('logout/', home.user_logout, name='logout'),  # Đường dẫn logout

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
