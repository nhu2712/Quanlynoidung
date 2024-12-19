from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Employee, Room, Service, Post, Offer, EmployeePermission
from .decorators import check_employee_permission
from .controllers import get_permission_context_by_permission


# ----------------- Home Dashboard ----------------- #

@login_required
def admin_dashboard(request):
    total_posts = Post.objects.count()
    total_employees = Employee.objects.count()
    total_rooms = Room.objects.count()
    total_services = Service.objects.count()
    total_offers = Offer.objects.count()
    context = {
        'user': request.user,
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'total_posts': total_posts,
        'total_employees': total_employees,
        'total_rooms': total_rooms,
        'total_services': total_services,
        'total_offers': total_offers,
    }
    return render(request, 'admin/home.html', context)


# ----------------- Manage Employees ----------------- #

@login_required
@check_employee_permission([EmployeePermission.ADMIN])
def admin_employee(request):
    employees = Employee.objects.all()

    if request.method == "POST":
        # Xử lý cập nhật quyền
        employee_id = request.POST.get("employee_id")
        employee_permission = request.POST.get("employee_permission")
        action = request.POST.get("action")

        # Find employee by id
        employee = get_object_or_404(Employee, id=employee_id)

        if action == "add_employee":
            ...
        elif action == "change_permission":
            employee.permission = employee_permission
            employee.save()
            messages.success(
                request, f"Đã cập nhật quyền của {employee.user.username} thành {employee_permission}.")
        elif action == "remove_employee":
            employee.user.delete()
            employee.delete()
            messages.success(request, "Nhân viên đã được xóa thành công.")
        else:
            messages.error(request, "Hành động không hợp lệ.")

        return redirect("manage_employees")

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        "employees": employees,
        'permission_options': EmployeePermission.choices
    }
    return render(request, "admin/employee.html", context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN])
def create_employee(request):
    if request.method == "POST":
        username = request.POST.get("add-employee-username")
        email = request.POST.get("add-employee-email", "")
        password = request.POST.get("add-employee-password")
        permission = request.POST.get("add-employee-permission")
        position = request.POST.get("add-employee-position", "Staff")
        department = request.POST.get("add-employee-department", "IT")

        if not username or not password:
            messages.error(
                request, "Tên người dùng và mật khẩu không được để trống.")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Tên người dùng đã tồn tại.")

        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            Employee.objects.create(
                user=user, permission=permission, position=position, department=department)
            messages.success(request, "Nhân viên đã được tạo thành công.")
    return redirect("manage_employees")


# ----------------- Manage Rooms ----------------- #

@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def admin_room(request):
    if request.method == 'POST':
        # Xử lý việc tạo phòng mới
        room_number = request.POST.get('room_number')
        room_type = request.POST.get('room_type')
        price_per_night = request.POST.get('price_per_night')
        status = request.POST.get('status')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Room.objects.create(
            room_number=room_number,
            room_type=room_type,
            price_per_night=price_per_night,
            status=status,
            description=description,
            image=image,
            author=request.user
        )
        return redirect('admin_room')

    # Hiển thị danh sách phòng
    rooms = Room.objects.all()

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'rooms': rooms
    }
    return render(request, 'admin/room.html', context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def delete_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    room.delete()
    messages.success(request, 'Phòng đã được xóa thành công.')
    return redirect('admin_room')


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def edit_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    if request.method == 'POST':
        room.room_number = request.POST.get('room_number')
        room.room_type = request.POST.get('room_type')
        room.price_per_night = request.POST.get('price_per_night')
        room.status = request.POST.get('status')
        room.description = request.POST.get('description')
        if 'image' in request.FILES:
            room.image = request.FILES['image']

        room.save()
        messages.success(request, 'Phòng đã được cập nhật thành công.')
        return redirect('admin_room')

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'room': room
    }
    return render(request, 'admin/room.html', context)


# ----------------- Manage Services ----------------- #


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def admin_service(request):
    if request.method == 'POST':
        # Xử lý việc tạo dịch vụ mới
        name = request.POST.get('name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        Service.objects.create(
            name=name,
            category=category,
            price=price,
            description=description,
            image=image,
            author=request.user
        )
        messages.success(request, 'Dịch vụ đã được tạo thành công.')
        return redirect('admin_service')

    # Hiển thị danh sách dịch vụ
    services = Service.objects.all()

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'services': services
    }
    return render(request, 'admin/service.html', context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def delete_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    service.delete()
    messages.success(request, 'Dịch vụ đã được xóa thành công.')
    return redirect('admin_service')


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def edit_service(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == 'POST':
        service.name = request.POST.get('name')
        service.category = request.POST.get('category')
        service.price = request.POST.get('price')
        service.description = request.POST.get('description')

        if 'image' in request.FILES:
            service.image = request.FILES['image']

        service.save()
        messages.success(request, 'Dịch vụ đã được cập nhật thành công.')
        return redirect('admin_service')

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'service': service
    }
    return render(request, 'admin/service.html', context)


# ----------------- Manage Posts ----------------- #


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def admin_post(request):
    if request.method == 'POST':
        # Xử lý việc tạo bài đăng mới
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user  # Lấy người dùng hiện tại làm tác giả
        image = request.FILES.get('image')
        Post.objects.create(
            title=title,
            content=content,
            author=author,
            image=image,
            status='pending',
        )
        messages.success(request, 'Bài đăng đã được tạo thành công.')
        return redirect('admin_post')

    # Hiển thị danh sách bài đăng
    posts = Post.objects.all()

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'posts': posts
    }
    return render(request, 'admin/post.html', context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Bài đăng đã được xóa thành công.')
    return redirect('admin_post')


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def edit_post(request, post_id):
    """
    Chỉnh sửa bài đăng và cập nhật trạng thái (status).
    """
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        # Cập nhật các thông tin từ form
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.status = request.POST.get('status')

        # Nếu có ảnh mới được tải lên
        if 'image' in request.FILES:
            post.image = request.FILES['image']

        # Lưu bài đăng
        post.save()

        # Thêm thông báo thành công
        messages.success(request, 'Bài đăng đã được cập nhật thành công.')
        return redirect('admin_post')

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'post': post
    }
    return render(request, 'admin/post.html', context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER])
def approve_post(request, post_id):
    print(request.POST.get('status'))
    post = get_object_or_404(Post, id=post_id)
    status = request.POST.get('status')
    post.status = status
    post.save()
    messages.success(request, 'Bài đăng đã được duyệt thành công.')
    return redirect('admin_post')


# ----------------- Manage Gifts ----------------- #


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def admin_gift(request):
    if request.method == 'POST':
        # Handle offer creation
        title = request.POST.get('title')
        description = request.POST.get('description')
        discount_percentage = request.POST.get('discount_percentage')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        image = request.FILES.get('image')

        Offer.objects.create(
            title=title,
            description=description,
            discount_percentage=discount_percentage,
            start_date=start_date,
            end_date=end_date,
            image=image,
            author=request.user
        )
        messages.success(request, 'Offer has been created successfully.')
        return redirect('admin_gift')

    # Display the list of offers
    offers = Offer.objects.all()

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'offers': offers
    }
    return render(request, 'admin/gift.html', context)


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def delete_gift(request, gift_id):
    offer = get_object_or_404(Offer, id=gift_id)
    offer.delete()
    messages.success(request, 'Offer has been deleted successfully.')
    return redirect('admin_gift')


@login_required
@check_employee_permission([EmployeePermission.ADMIN, EmployeePermission.CONTENT_MANAGER, EmployeePermission.EDITOR])
def edit_gift(request, gift_id):
    offer = get_object_or_404(Offer, id=gift_id)

    if request.method == 'POST':
        offer.title = request.POST.get('title')
        offer.description = request.POST.get('description')
        offer.discount_percentage = request.POST.get('discount_percentage')
        offer.start_date = request.POST.get('start_date')
        offer.end_date = request.POST.get('end_date')
        if 'image' in request.FILES:
            offer.image = request.FILES['image']

        offer.save()
        messages.success(request, 'Offer has been updated successfully.')
        return redirect('admin_gift')

    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
        'offer': offer
    }
    return render(request, 'admin/gift.html', context)


# ----------------- Profile ----------------- #


@login_required
def profile(request):
    context = {
        'permission_context': get_permission_context_by_permission(request.user.employee.permission),
        'user': request.user,
    }
    return render(request, 'admin/users-profile.html', context)
