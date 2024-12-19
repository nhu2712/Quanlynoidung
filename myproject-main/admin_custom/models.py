# models.py
import os
import uuid
from django.contrib.auth.models import User
from django.db import models

def get_image_upload_path(instance, filename):
    # Tạo tên file ngẫu nhiên bằng UUID và giữ nguyên phần mở rộng của file gốc
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join('room_images/', filename)  # Lưu vào thư mục 'room_images' bên trong 'media'

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
        ('available', 'Available'),
        ('occupied', 'Occupied'),
        ('maintenance', 'Maintenance'),
    ]

    room_number = models.CharField(max_length=10, unique=True)
    room_type = models.CharField(max_length=100)  # Ví dụ: "Deluxe", "Standard", "Suite"
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=ROOM_STATUS_CHOICES, default='available')
    image = models.ImageField(upload_to=get_image_upload_path, null=True, blank=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.room_type}"
