#!/usr/bin/env python
import os
import django

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'kmk.settings')
django.setup()

from django.contrib.auth.models import User

def create_admin_user(username, email, password):
    # Check if user already exists
    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists!")
        return False
    
    # Create superuser
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"Admin user '{username}' created successfully!")
        print(f"   Username: {username}")
        print(f"   Password: {password}")
        print(f"   Email: {email}")
        return True
    except Exception as e:
        print(f"Error creating admin user: {e}")
        return False

if __name__ == '__main__':
    print("Creating custom admin users...")
    
    # Common admin usernames that might be used
    admin_users = [
        ('admin', 'admin@kmk.sch.id', 'admin123'),
        ('administrator', 'admin@kmk.sch.id', 'admin123'),
        ('root', 'root@kmk.sch.id', 'root123'),
        ('superuser', 'super@kmk.sch.id', 'super123'),
        ('kmk_admin', 'admin@kmk.sch.id', 'kmk123'),
    ]
    
    for username, email, password in admin_users:
        create_admin_user(username, email, password)
        print()
