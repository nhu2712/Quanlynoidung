# Generated by Django 5.1.3 on 2024-11-10 07:42

import admin_custom.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_custom', '0003_room_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('spa', 'Spa'), ('restaurant', 'Nhà hàng'), ('barcoffee', 'Bar&Coffee')], max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=admin_custom.models.get_image_upload_path_service)),
            ],
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'permissions': [('can_view_employee_post', 'Can view employee post'), ('can_create_employee_post', 'Can create employee post'), ('can_edit_employee_post', 'Can edit employee post'), ('can_delete_employee_post', 'Can delete employee post')]},
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=admin_custom.models.get_image_upload_path_room),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=admin_custom.models.get_image_upload_path_post)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': [('can_view_post', 'Can view post'), ('can_create_post', 'Can create post'), ('can_edit_post', 'Can edit post'), ('can_delete_post', 'Can delete post')],
            },
        ),
    ]
