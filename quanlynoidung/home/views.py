from django.shortcuts import render, redirect , get_object_or_404
from admin_custom.models import Room, Post, Service, Comment, Offer, CommentPost

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login  
from django.contrib import messages 
from django.contrib.auth.models import User 



# Create your views here.

def get_home(request):
    return render(request, 'home.html')
def get_about(request):
    return render(request, 'about.html')
def get_event(request):
    events = Post.objects.filter(status="approved")
    return render(request, 'event.html', {'events': events})
def get_room(request):
    rooms = Room.objects.all() 
    return render(request, 'room.html', {'rooms': rooms})
def get_contact(request):
    return render(request, 'contact.html')
def get_service(request):
    services = Service.objects.all() 
    return render(request, 'service.html', {'services': services})
def get_gift(request):
    offers = Offer.objects.all() 
    return render(request, 'gift.html', {'offers': offers})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        user = User.objects.create_user(username=username, password=password)
        user.save()
        
        login(request, user)
        messages.success(request, 'Registration successful.')
        return redirect('home') 
    
    return render(request, 'register.html')

def add_comment(request):
    if request.method == "POST":
        content = request.POST.get('content')
        room_id = request.POST.get('room_id')
        if content and room_id:
            room = Room.objects.get(id=room_id)
            Comment.objects.create(post_id=room.id, content=content, author=request.user)
            return redirect('room_detail', room_id=room.id)
    return redirect('room_list')

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    comments = Comment.objects.filter(post_id=room.id).order_by('-created_at')

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if the user is not authenticated
        
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post_id=room.id, content=content, author=request.user)
            return redirect('room_detail', room_id=room.id)  # Redirect to the same room page

    return render(request, 'room_detail.html', {'room': room, 'comments': comments})

def get_room_suite():
    room = get_object_or_404(Room, id=room_id)
    comments = Comment.objects.filter(post_id=room.id).order_by('-created_at')

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post_id=room.id, content=content, author=request.user)
            return redirect('room_detail', room_id=room.id)

    return render(request, 'room_detail.html', {'room': room, 'comments': comments})

def get_room_deluxe():
    room = get_object_or_404(Room, id=room_id)
    comments = Comment.objects.filter(post_id=room.id).order_by('-created_at')

    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post_id=room.id, content=content, author=request.user)
            return redirect('room_detail', room_id=room.id)

    return render(request, 'room_detail.html', {'room': room, 'comments': comments})

def rooms_by_type(request, room_type):
    rooms = Room.objects.filter(room_type__iexact=room_type)  
    return render(request, 'rooms_by_type.html', {'rooms': rooms, 'room_type': room_type})

def user_logout(request):
    try:
        request.session.flush()
        logout(request)
    except Exception as e:
        pass  # Hoặc ghi log nếu cần
    return redirect('home')

def event_detail(request, id):
    # Lấy thông tin sự kiện
    event = get_object_or_404(Post, id=id)
    # Lấy danh sách bình luận theo thứ tự mới nhất trước
    comments = CommentPost.objects.filter(post=event).order_by('-created_at')

    if request.method == "POST":
        # Nếu người dùng đã gửi bình luận
        if not request.user.is_authenticated:
            return redirect('login')

        content = request.POST.get('content')  # Lấy nội dung bình luận từ form
        if content:
            # Tạo bình luận mới
            CommentPost.objects.create(
                post=event,
                author=request.user,
                content=content
            )
            return redirect('event_detail', id=id)  # Làm mới trang sau khi thêm bình luận

    return render(request, 'event_detail.html', {'event': event, 'comments': comments})