from django.shortcuts import render, redirect , get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  
from django.contrib import messages 
from django.contrib.auth.models import User 
from .models import Employee, Room


# Create your views here.

def admin_dashboard(request):
    return render(request, 'admin/home.html')
def admin_customer(request):
    employees = Employee.objects.all()
    return render(request, 'admin/customer.html', {'employees': employees})
def admin_employee(request):
    employees = Employee.objects.all()
    return render(request, 'admin/employee.html', {'employees': employees})
def admin_room(request):
    if request.method == 'POST':
        # Xử lý việc tạo phòng mới
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price_per_night = request.POST.get('price_per_night')
        status = request.POST.get('status')
        image = request.FILES.get('image')
        Room.objects.create(
            room_number=room_number,
            room_type=room_type,
            price_per_night=price_per_night,
            status=status,
            image=image
        )
        return redirect('admin_room')

    # Hiển thị danh sách phòng
    rooms = Room.objects.all()
    return render(request, 'admin/room.html', {'rooms': rooms})
def admin_service(request):
    return render(request, 'admin/service.html')
def admin_post(request):
    return render(request, 'admin/post.html')

def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    messages.success(request, 'Phòng đã được xóa thành công.')
    return redirect('admin_room')

def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        room.room_number = request.POST.get('room_number')
        room.room_type = request.POST.get('room_type')
        room.price_per_night = request.POST.get('price_per_night')
        room.status = request.POST.get('status')

        if 'image' in request.FILES:
            room.image = request.FILES['image']

        room.save()
        messages.success(request, 'Phòng đã được cập nhật thành công.')
        return redirect('admin_room')

    return render(request, 'admin/edit_room.html', {'room': room})