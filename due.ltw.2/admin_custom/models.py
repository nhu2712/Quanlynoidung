# models.py
import os
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_image_upload_path_room(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('room_images/', filename)


class EmployeePermission(models.TextChoices):
    ADMIN = 'admin', _('Admin')
    CONTENT_MANAGER = 'content_manager', _('Content Manager')
    EDITOR = 'editor', _('Editor')


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    permission = models.CharField(
        max_length=20, choices=EmployeePermission.choices, default=EmployeePermission.EDITOR)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view_employee_post", "Can view employee post"),
            ("can_create_employee_post", "Can create employee post"),
            ("can_edit_employee_post", "Can edit employee post"),
            ("can_delete_employee_post", "Can delete employee post"),
        ]


class Room(models.Model):
    ROOM_STATUS_CHOICES = [
        ('available', 'Có sẵn'),
        ('occupied', 'Đang sử dụng'),
        ('maintenance', 'Đang sửa chữa'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    room_number = models.CharField(max_length=10, unique=True)
    # Ví dụ: "Deluxe", "Standard", "Suite"
    room_type = models.CharField(max_length=100)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20, choices=ROOM_STATUS_CHOICES, default='available')
    description = models.TextField()
    image = models.ImageField(
        upload_to=get_image_upload_path_room, null=True, blank=True)
    created_at_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"


def get_image_upload_path_service(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('service_images/', filename)


class Service(models.Model):
    SERVICE_CATEGORY_CHOICES = [
        ('spa', 'Spa'),
        ('restaurant', 'Nhà hàng'),
        ('barcoffee', 'Bar&Coffee'),
        ('gym', 'Dịch vụ phòng tập'),
    ]

    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=50, choices=SERVICE_CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(
        upload_to=get_image_upload_path_service, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.category}"


def get_image_upload_path_post(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('post_images/', filename)


class Post(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Chờ duyệt'),
        ('approved', 'Đã duyệt'),
        ('rejected', 'Từ chối'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to=get_image_upload_path_post, null=True, blank=True)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return self.title

    class Meta:
        permissions = [
            ("can_view_post", "Can view post"),
            ("can_create_post", "Can create post"),
            ("can_edit_post", "Can edit post"),
            ("can_delete_post", "Can delete post"),
        ]


class Offer(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(
        upload_to=get_image_upload_path_post, null=True, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.title} ({self.discount_percentage}% off)"

    class Meta:
        permissions = [
            ("can_view_offer", "Can view offer"),
            ("can_create_offer", "Can create offer"),
            ("can_edit_offer", "Can edit offer"),
            ("can_delete_offer", "Can delete offer"),
        ]


class Comment(models.Model):
    post = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"


class CommentPost(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="post_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
